# Signature Ed25519 des JARs Calumet

Ce guide couvre la mise en place complète de la vérification d'intégrité
des JARs téléchargés par l'Updater, à l'aide d'une signature Ed25519.

**À faire sur le poste de release (maison) — une seule fois pour la génération des clés,
puis à chaque release pour la signature.**

---

## Prérequis

- OpenSSL ≥ 1.1.1 (Ed25519 support)
- Java 25 (déjà utilisé par le projet)
- Bash ou Git Bash

Vérification :
```bash
openssl version          # OpenSSL 1.1.1 ou supérieur
java -version            # Java 25
```

---

## Étape 1 — Génération de la paire de clés (une seule fois)

```bash
# Dans un répertoire sécurisé, PAS dans le repo Git
mkdir ~/calumet-keys && cd ~/calumet-keys

# Génère la clé privée Ed25519
openssl genpkey -algorithm Ed25519 -out calumet_private.pem

# Extrait la clé publique
openssl pkey -in calumet_private.pem -pubout -out calumet_public.pem
```

### Règles absolues pour la clé privée

- **Ne jamais committer `calumet_private.pem` dans Git**
- La garder dans `~/calumet-keys/` sur le poste de release uniquement
- Faire une sauvegarde chiffrée (clé USB, gestionnaire de mots de passe)

---

## Étape 2 — Extraire la clé publique pour Updater.java

```bash
# Affiche la clé publique encodée en base64 (format X.509/DER)
openssl pkey -in ~/calumet-keys/calumet_public.pem -pubout -outform DER | base64 -w 0
```

La commande produit une chaîne sur une ligne, par exemple :
```
MCowBQYDK2VwAyEA7mzHkRsFpBN6e8wX3hPQr1sVkJDq2YtLOcUiBAzmXpA=
```

**Copier cette valeur** : elle sera hardcodée dans `Updater.java` à l'étape 4.

---

## Étape 3 — Script de release

Créer le fichier `~/calumet-keys/sign-release.sh` :

```bash
#!/bin/bash
# Usage : ./sign-release.sh /chemin/vers/Calumet.jar
# Produit : sha256.txt et signature.b64 à afficher dans lastVersion

set -e

JAR="$1"
PRIVATE_KEY="$HOME/calumet-keys/calumet_private.pem"

if [ -z "$JAR" ] || [ ! -f "$JAR" ]; then
  echo "Usage: $0 /path/to/Calumet.jar"
  exit 1
fi

# 1. Calcule le SHA-256 (bytes bruts)
echo "Computing SHA-256..."
openssl dgst -sha256 -binary "$JAR" > /tmp/calumet.sha256.bin

# 2. Affiche le hash hex (pour [sha256] dans lastVersion)
SHA256_HEX=$(openssl dgst -sha256 "$JAR" | awk '{print $2}')
echo "SHA-256 : $SHA256_HEX"

# 3. Signe le hash avec la clé privée Ed25519
echo "Signing..."
openssl pkeyutl -sign \
  -inkey "$PRIVATE_KEY" \
  -rawin \
  -in /tmp/calumet.sha256.bin \
  -out /tmp/calumet.sig.bin

# 4. Encode la signature en base64 (pour [sig] dans lastVersion)
SIG_B64=$(base64 -w 0 /tmp/calumet.sig.bin)
echo "Signature: $SIG_B64"

# 5. Affiche les 2 lignes à ajouter dans lastVersion
echo ""
echo "=== Lignes à ajouter dans lastVersion ==="
echo "[sha256]${SHA256_HEX}[/sha256]"
echo "[sig]${SIG_B64}[/sig]"

# Nettoyage
rm -f /tmp/calumet.sha256.bin /tmp/calumet.sig.bin
```

```bash
chmod +x ~/calumet-keys/sign-release.sh
```

---

## Étape 4 — Format `lastVersion` mis à jour

Après avoir exécuté `sign-release.sh`, le fichier `lastVersion` sur GitHub
doit avoir ce format :

```
[update]dist/CalumetGui-10.8.jar[/update]
[sha256]e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855[/sha256]
[sig]MCowBQYDK2VwAyEA7mzHkRsFpBN6e8wX3hPQr1sVkJDq2YtLOcUiBAzmXpA=...[/sig]
[exe]dist/Calumet.exe[/exe]
```

---

## Étape 5 — Modifications de `Updater.java`

### 5a. Imports à ajouter en tête de fichier

```java
import java.security.KeyFactory;
import java.security.MessageDigest;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;
```

### 5b. Constante clé publique (remplacer la valeur par celle de l'étape 2)

```java
// Coller ici la sortie de :
// openssl pkey -in calumet_public.pem -pubout -outform DER | base64 -w 0
private static final String PUBLIC_KEY_B64 =
    "MCowBQYDK2VwAyEA7mzHkRsFpBN6e8wX3hPQr1sVkJDq2YtLOcUiBAzmXpA=";
```

### 5c. Méthode de vérification (à ajouter dans Updater)

```java
private static void verifyJarSignature(File jarFile) throws Exception {
    // 1. SHA-256 du JAR téléchargé
    MessageDigest digest = MessageDigest.getInstance("SHA-256");
    byte[] jarHash = digest.digest(Files.readAllBytes(jarFile.toPath()));

    // 2. Signature depuis le fichier lastVersion
    String sigB64 = data.substring(
        data.indexOf("[sig]") + 5,
        data.indexOf("[/sig]")
    ).trim();
    byte[] sigBytes = Base64.getDecoder().decode(sigB64);

    // 3. Reconstruction de la clé publique Ed25519
    byte[] keyBytes = Base64.getDecoder().decode(PUBLIC_KEY_B64);
    PublicKey publicKey = KeyFactory.getInstance("Ed25519")
        .generatePublic(new X509EncodedKeySpec(keyBytes));

    // 4. Vérification de la signature
    Signature sig = Signature.getInstance("Ed25519");
    sig.initVerify(publicKey);
    sig.update(jarHash);
    if (!sig.verify(sigBytes)) {
        throw new SecurityException(
            "JAR signature verification FAILED - aborting update"
        );
    }
    log("Signature Ed25519 OK.");
}
```

### 5d. Appel dans `main()` — après le download, avant le move

```java
// Remplacer le bloc existant :
log("Download OK  : " + tempFile.length() + " bytes");

// Par :
log("Download OK  : " + tempFile.length() + " bytes");
verifyJarSignature(tempFile);   // <-- ajout ici
```

---

## Étape 6 — Test de vérification manuelle

Avant de déployer, tester que la signature fonctionne :

```bash
# Signer un JAR test
./sign-release.sh /path/to/Calumet.jar

# Vérification manuelle avec openssl
openssl dgst -sha256 -binary /path/to/Calumet.jar > /tmp/test.bin
openssl pkeyutl -verify \
  -pubin -inkey ~/calumet-keys/calumet_public.pem \
  -rawin \
  -in /tmp/test.bin \
  -sigfile /tmp/calumet.sig.bin
# Attendu : "Signature Verified Successfully"
```

---

## Workflow release complet

```
1. mvn clean install -pl CalumetGui        ← build le JAR
2. ./sign-release.sh target/Calumet.jar    ← génère sha256 + signature
3. Copier les 2 lignes [sha256] et [sig]   ← dans lastVersion sur GitHub
4. Pousser le JAR et lastVersion           ← via git push ou upload GitHub
```

---

## Extension possible : signer aussi les ZIPs de libs

`UpdateLibs.java` télécharge des ZIPs (`libs92.zip`, `libs94.zip`, etc.)
sans vérification. Le même mécanisme peut s'appliquer :
- Ajouter `[libsig-v92]...[/libsig-v92]` dans `lastVersion`
- Vérifier dans `UpdateLibs.downloadAndExtract()` avant d'extraire

Non prioritaire si les ZIPs de libs ne changent qu'à chaque version majeure.

---

## Résumé de sécurité

| Menace | Protégé ? |
|---|---|
| MITM sur le download | ✅ La signature ne peut pas être forgée sans la clé privée |
| Remplacement du JAR sur GitHub | ✅ Idem |
| Remplacement de `lastVersion` seul | ✅ La signature serait invalide sans le bon JAR |
| Remplacement de `lastVersion` + JAR | ✅ Impossible sans la clé privée |
| Remplacement local de `Calumet.jar` après install | ⚠️ Non couvert (l'Updater ne tourne qu'au moment de la mise à jour) |
| Compromission du poste de release | ❌ Hors scope — protéger la clé privée |
