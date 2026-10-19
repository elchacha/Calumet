# Ce qui manque à depGraph — constats tirés de l'analyse Agent Autonome

Document du 2026-10-07 pour l'outil qui génère l'export Calumet (graphe `C:\pro\depgraph\depgraph`, audits, sources `mdapi`). Il liste ce que j'ai dû chercher dans les sources, faute de le trouver dans le graphe, puis des idées utiles que cette analyse n'a pas exigées, puis des défauts de qualité du graphe.

**Comment lire.** Chaque manque a : ce qu'on cherchait, ce que le graphe donnait, ce que j'ai fait à la place, et une proposition. Les chiffres sont ceux de l'export de ChronopostProd (graphe du 2026-10-06). Les propositions sont des pistes : l'effort de réalisation n'a pas été évalué.

## Synthèse

| # | Manque | Ce que cela m'a coûté ici | Priorité suggérée |
|---|---|---|---|
| A1 | Valeur écrite et condition d'une écriture | Trouvaille centrale (statut `Fermé` sans enquête) obtenue seulement en lisant le code | haute |
| A2 | Condition d'un appel de méthode | Idem : l'envoi du mail dépend d'un `if` invisible | haute |
| A3 | « Quels composants faut-il avec celui-ci ? » (fermeture de déploiement) | Manifest incomplet détecté à la main | haute |
| A4 | Placement précis dans les pages | « Au-dessus des jalons » invisible | moyenne |
| A5 | Pages Visualforce → champs via variables d'itération | Un lecteur de `Visuel__c` raté | moyenne |
| A6 | Rapports individuels | 43 types de rapport, aucun rapport réel | moyenne |
| A7 | Ressource statique d'une formule rattachée à l'objet, pas au champ | Impact d'un changement d'icône non traçable | moyenne |
| A8 | Droits requis par un composant (chaîne LWC → Apex → champs → profils) | Calcul fait à la main | haute |
| A9 | Page et layout réellement affichés pour un profil | Combinaison manuelle de plusieurs fichiers | moyenne |
| A10 | Références par chaîne littérale (modèle d'email, adresse expéditeur) | Aucun lien du code vers le modèle d'email | moyenne |
| A11 | Type d'effet : envoi d'email, publication d'événement, appel externe | `uses` mélange tout | moyenne |
| A12 | Volumétrie par créateur et par période | Un chiffre clé hors graphe | moyenne |
| A13 | Comparaison avec une sandbox | Écarts PFI / prod relevés à la main | basse |
| C1 | Identifiants de nœuds incohérents entre fichiers | Requêtes vides au premier essai | haute |
| C2 | Identifiants qui ne diffèrent que par la casse | 2 493 doublons apparents | haute |

## A. Manques rencontrés pendant l'analyse

### A1. Valeur écrite et condition d'une écriture

- **Ce que je cherchais :** dans quel état un dossier Agent Autonome est créé.
- **Ce que le graphe donne :** `AgentAutonomeHandler -- writes --> field:Case.Status` (inféré). Rien sur la valeur ni sur la condition.
- **Ce que le code dit :** `cs.Status = request.inquery != null ? 'En cours Chronopost' : 'Fermé'`. Un dossier sans enquête est donc créé **fermé**. C'est la raison pour laquelle le mail de confirmation promet un suivi qui n'existera pas.
- **Proposition :** sur les arêtes `writes`, ajouter les attributs optionnels `value` (littéral ou expression telle qu'écrite) et `guard` (condition qui l'entoure, en texte), plus `line`. Même sans interpréter l'expression, les afficher suffit.
- **Lien avec le README :** le README dit déjà que le graphe ne capture ni quand ni sous quelle condition. Ce point propose de capturer au moins le texte, sans le comprendre.

### A2. Condition d'un appel de méthode

- **Ce que je cherchais :** quand le mail et le PDF sont-ils déclenchés.
- **Ce que le graphe donne :** `AgentAutonomeHandler -- calls --> ApexMethod:…`. L'appel à `sendMailOrSMS` est présent, sans la condition `if (request.inquery != null)`.
- **Proposition :** même attribut `guard` sur les arêtes `calls`, et un drapeau `in_loop` / `in_try` / `async` (appel dans une boucle, un `try`, un contexte asynchrone). `in_loop` est déjà utile pour le scan « SOQL dans une boucle » de `performance.json`.

### A3. Fermeture de déploiement

- **Ce que je cherchais :** « si je déploie ces composants, de quoi ont-ils besoin qui n'est ni en prod ni dans le lot ? »
- **Ce que j'ai dû faire :** repérer à la main que le layout `Case-Case_SC` référençait `Conversation_Summary_SC__c` et `Conversation_Summary_Display__c` (absents de la prod), que la formule `Visuel__c` appelait `/resource/AgentAutonome` (absente du manifest), que la page console référençait `caseHeaderPanel` (absent du manifest).
- **Proposition :** un calcul « fermeture » : entrée = liste de composants (un manifest), sortie = dépendances sortantes absentes de la prod **et** du lot. Le graphe de prod a déjà tout pour la partie « absent de la prod » ; il suffit d'accepter un lot en entrée et de lire ses fichiers.

### A4. Placement précis dans les pages

- **Ce que je cherchais :** « le résumé s'affiche-t-il au-dessus des jalons dans la page console ? »
- **Ce que le graphe donne :** `FlexiPage:Case_Console_LEX_page -- places --> LWC:…` et des arêtes `displays` / `visibility` vers des champs. Ni la région, ni l'ordre, ni l'onglet, ni la valeur de la règle de visibilité (par exemple « statut différent de Fermé »).
- **Proposition :** attributs sur `places` : `region`, `index`, `parent` (onglet ou section), `label`. Sur `visibility` : l'opérateur et la valeur de la règle.

### A5. Pages Visualforce → champs via variables d'itération

- **Ce que je cherchais :** tout ce qui lit `Case.Visuel__c`.
- **Ce que le graphe donne :** 33 pages Visualforce sur 214 ont des arêtes vers des champs (`displays`). `InfosSurLaLT` n'en a aucune, alors que `<apex:inputField value="{!dossier.Visuel__c}"/>` la relie à ce champ.
- **Cause probable :** `dossier` est la variable d'une table (`var="dossier"` sur une liste fournie par le contrôleur). La résolution demande de suivre la liste vers le type du contrôleur.
- **Proposition :** résoudre `var=` vers le type de la collection du contrôleur ; à défaut, créer une arête « inférée » `page -> Objet.Champ` quand le texte `{!x.Champ__c}` apparaît et que `Champ__c` n'existe que sur un objet de la liste. Aussi : `$ObjectType.Case.Fields.Visuel__c.Label`.

### A6. Rapports individuels

- **Ce que le graphe donne :** 43 types de rapport exposent `Visuel__c` (arêtes `exposes`). On ne sait pas quels **rapports** l'utilisent, ni en colonne, filtre ou regroupement.
- **Piste :** `stale_reports.json` connaît déjà les rapports par l'API (dernière exécution, dossier). Ajouter leurs colonnes, filtres et regroupements permettrait des arêtes `rapport -> champ` avec le rôle, et de mesurer l'impact réel (rapport utilisé la semaine dernière ou jamais).

### A7. Ressource statique d'une formule

- **Ce que le graphe donne :** 111 arêtes `static_resource` partent d'`Object:…` (par exemple `Object:Case -- static_resource --> StaticResource:IconeDemandeDocument`), **aucune d'un champ**. La formule `TypeDossierIcone__c` (qui contient `IMAGE("/resource/…/IconeDemandeDocument")`) n'est pas reliée à la ressource.
- **Proposition :** rattacher l'arête au champ formule. Cela répond à « quelles formules cassent si je renomme cette ressource ? » (c'est l'enjeu du nom `AgentAutonome` / `AgentAutonomeIcon` dans ce projet).
- **Extension utile :** pour chaque formule, ajouter les indicateurs `spans_relationship` (traverse un objet lié, par exemple `CreatedBy.FirstName`), `result_type` et la longueur. Cela permet de signaler d'office qu'un champ formule est non indexable, ce que j'ai dû déduire.
- **Déjà bien fait :** `formula_depends_on` existe et résout les relations (par exemple `Case.Activite_Createur__c -> Case.CreatedById` et `User.GRC_Activite__c`).

### A8. Droits requis par un composant

- **Ce que je cherchais :** « quels profils échoueront à ouvrir `caseHeaderPanel` ? »
- **Ce que j'ai dû faire :** suivre à la main LWC → méthode Apex → champs de la requête (`WITH SECURITY_ENFORCED`) → droits de champ de chaque profil qui voit la page. Le graphe a chaque maillon (`calls_apex`, `reads`, `fls_read`, `access`) mais pas la chaîne assemblée.
- **Proposition :** un calcul « droits requis » par composant, avec en attribut de classe `sharing` (with / without), `enforces_fls` (`WITH SECURITY_ENFORCED`, `WITH USER_MODE`, `stripInaccessible`), et en sortie les profils qui manquent d'un droit. Ce serait l'un des calculs les plus utiles pour les déploiements de composants Lightning.

### A9. Page et layout réellement affichés

- **Ce que je cherchais :** « quelles pages montrent les champs du layout `Case-Case_SC` ? »
- **Ce que j'ai dû faire :** combiner l'affectation des pages par application (`assigns`), la présence de `force:detailPanel` dans la page, et `layout_assignments.tsv`. Dans ce TSV, les lignes `RecordType:…` n'ont pas de profil : on ne sait pas lire si c'est un profil × type ou un type seul.
- **Proposition :** un calcul dérivé « page effective » (profil, application, type d'enregistrement, format) → page et layout, avec une arête dérivée `FlexiPage -- renders_layout --> layout` quand `force:detailPanel` est présent. Clarifier la colonne manquante du TSV.

### A10. Références par chaîne littérale

- **Ce que le graphe donne :** `AgentAutonomeHandler -- reads --> field:EmailTemplate.DeveloperName`. L'information « quel modèle d'email » (`'Agent_Autonome_Notification_creation_dossier'`) est dans le code mais pas dans le graphe. De même l'adresse expéditeur (`OrgWideEmailAddress`) et l'`Entitlement` nommé `'Appel Chronopost'`.
- **Proposition :** quand un littéral d'un `WHERE DeveloperName = '…'` correspond à un nœud connu (modèle d'email, type d'enregistrement), créer l'arête vers ce nœud, source `dynamic`. Les types d'enregistrement ont déjà ce traitement (`rt_set`) ; l'étendre aux modèles d'email, étiquettes, métadonnées personnalisées et pages.
- **Cas voisin (métadonnées personnalisées pilotant le comportement) :** le survol ajouté dans ce projet lit des enregistrements `CompactLayoutOverlayField__mdt` dont les valeurs sont des noms de champs (`Field_API_Name__c = Conversation_Summary__c`). Aujourd'hui `MappingLeonard__mdt` n'a que des arêtes `uses` depuis les classes, sans les enregistrements. Traiter les enregistrements comme des nœuds, avec des arêtes vers les champs ou classes cités dans leurs valeurs, rendrait ces configurations visibles.

### A11. Type d'effet

- **Ce que le graphe donne :** `AgentAutonomeHandler -- uses --> Object:Agent_Autonome_Pdf_Generation__e`, du même type que `uses --> Object:Entitlement` (une lecture).
- **Ce que je voulais voir :** que le handler *publie* un événement, *envoie un email*, *appelle un service externe* (`calls_credential` existe et marche bien).
- **Proposition :** des types d'arête explicites : `publishes_event` (`EventBus.publish`), `sends_email` (`Messaging.sendEmail`, avec le modèle si résolu comme en A10), `enqueues` (déjà présent : le trigger `PDFGenerationTrigger` pointe vers `PlatformEventPDFGeneration`), `callout`. L'inventaire « tout ce qui peut écrire à un client » (ordres de grandeur d'envois, doublons de notification avec les règles de workflow) deviendrait une simple requête.

### A12. Volumétrie par créateur et par période

- **Ce que je cherchais :** combien de dossiers par jour crée l'Agent Autonome (pour le volume d'emails et pour la formule non indexable).
- **Ce que le graphe donne :** `data_skew.json` (propriétaire, avec seuil de 10 000) : 348 358 tâches, 213 535 comptes, etc. pour « Léonard AA », mais aucune ligne pour les dossiers et aucune notion de période. Le chiffre de 368 000 dossiers vient du journal du projet.
- **Proposition :** pour les objets à forte volumétrie, ajouter le nombre d'enregistrements **par créateur** (`CreatedById`) et **par mois**. Les quotas d'organisation (emails par jour, appels de service) seraient un bon complément, s'ils sont lisibles par l'API.

### A13. Comparaison avec une sandbox

- **Ce que j'ai fait :** retrieve de la page console en PFI, comparée à la prod. Résultat : 4 écarts sans rapport avec le projet (résumé d'email, liste liée des plans d'action, règle de visibilité, deux propriétés).
- **Proposition (basse priorité) :** un mode « différence » : donner deux retrieves (prod et sandbox) et obtenir les composants modifiés avec, pour les pages Lightning, le détail par région. Utile avant de déployer un composant de page depuis une sandbox.

## B. Idées utiles que cette analyse n'a pas exigées

- **Valeurs de liste de choix comme nœuds.** Qui écrit, lit ou teste `Status = 'Fermé'` : code, flux, règles de workflow, règles de validation. Cela donnerait la machine à états du dossier (le README signale déjà que « plusieurs écrivains peuvent être des transitions légitimes ») et la liste de ce qui se déclenche quand un dossier devient fermé ou résolu. Les règles de workflow `Resolu` et `En cours Chronopost` ont des critères sur le statut dans les sources (`Case.workflow`) ; ils ne sont pas reliés aux écritures du code.
- **Inventaire des communications sortantes vers les clients.** Alertes de workflow (21 `email_alert`, 159 `email_template` dans le graphe), flux, Apex, avec événement déclencheur et destinataire. Détecter les doublons de notification (c'est le risque du point 2 de l'analyse).
- **Classes sans classe de test.** Une classe sans test ne passe pas un déploiement en production (75 %). Les arêtes `calls` des tests existent ; un rapport « classes sans test qui les appelle » est un calcul simple. Je l'ai fait à la main pour deux contrôleurs.
- **Utilisateurs d'intégration et ce qu'ils créent.** Relier un point d'entrée (`RestEndpoint`, application connectée) → permission set → utilisateurs, et le profil des objets créés par cet utilisateur. Cela aurait validé la règle « créé par Léonard AA » (point 7 de l'analyse) sans dépendre du nom.
- **Chaînes de composants Lightning avec leurs propriétés.** `lwc383InforSurLaLt` passe `overlay-config-name="Dossiers"` à `lwcTable` ; une arête `child` porterait les valeurs d'attributs passées.
- **Effet d'un style partagé.** Savoir quels écrans réutilisent un composant `child` est déjà possible ; ajouter, pour chacun, les pages qui l'hébergent et l'application associée (j'ai assemblé `places` + `assigns` à la main pour le point 6).
- **Cartographie des icônes et ressources statiques** (images dans formules, composants, pages) : qui utilise quelle ressource, avec la version.

## C. Qualité du graphe

### C1. Identifiants de nœuds incohérents entre fichiers

Un même composant a deux identifiants selon le fichier : `class:AgentAutonomeHandler` dans `xref_fields_java.json` (arêtes sur les champs), `ApexClass:AgentAutonomeHandler` dans `xref_component_java.json` (arêtes `calls`, `uses`, `calls_credential`, `rt_set`). De même `page:` / `VisualforcePage:`, `trigger:` / `ApexTrigger:`, `lwc:` / `LWC:`, `flexipage:` / `FlexiPage:`.

**Conséquence vécue :** ma première requête `from == "class:AgentAutonomeHandler"` n'a rendu que des arêtes de champs, aucune des arêtes de composants ; j'ai cru à des absences. Le README donne un exemple avec `Object:Case`, qui est cohérent, mais l'exemple « Apex » demande de connaître la règle.

**Proposition :** un identifiant canonique unique (`ApexClass:X`) dans tous les fichiers, ou à défaut une table d'alias dans `graph-meta.json`.

### C2. Identifiants qui ne diffèrent que par la casse

Dans les deux fichiers d'arêtes principaux, **2 493** identifiants existent sous deux casses (par exemple `ApprovalProcess:DPRP__c.DPRP_approval` et `approvalProcess:DPRP__c.DPRP_approval`). Dans les arêtes du handler : `Case.Id` et `Case.id`, `account.PersonEmail` (inféré) et `Account.PersonEmail` (déterministe), `GRC_Enquete__c.Id` et `GRC_Enquete__c.id`.

**Conséquence :** un comptage « qui lit `Account.PersonEmail` » en comparant les chaînes exactes manque la moitié ; le README recommande de compter des triplets distincts, mais pas de normaliser la casse. J'ai dû mettre en minuscules à chaque requête.

**Proposition :** normaliser à l'écriture (casse du nom d'API tel que défini dans l'org, résolu par la liste des objets et champs connus).

### C3. Task et Activity

Les écritures du handler sur une tâche sont tantôt `field:task.Subject`, tantôt `field:Activity.Objet_SC__c` (`Task` et `Activity` désignent le même objet pour les champs partagés). Une requête sur `Task` rate les champs notés `Activity`.

**Proposition :** résoudre `Activity` vers `Task` ou `Event` quand le contexte est connu (ici `Task todo = new Task()`).

### C4. Accents perdus dans deux fichiers sources

Sur 6 906 fichiers texte de `mdapi`, deux contiennent le caractère de remplacement `U+FFFD` : `objects/Case.object` (18 occurrences, par exemple les valeurs de liste « Téléphonie » écrites `T?l?phonie`) et `objects/InteractionClient__c.object` (1). Les fichiers sont en UTF-8 valide : la perte vient de la chaîne d'extraction ou de l'org elle-même. Les autres fichiers (par exemple `Case.workflow`) ne sont pas touchés.

**Conséquence :** une comparaison de valeur de liste de choix ou de littéral avec accent échouera pour ces valeurs. À vérifier : est-ce l'org (valeurs réellement corrompues) ou l'export ?

### C5. Fichier TSV `layout_assignments.tsv`

Les lignes de type `RecordType:Case.Social` n'ont pas de profil associé (voir A9). La colonne qui manque probablement est le profil.

## D. Ce qui a bien fonctionné (à conserver)

- `xref_security_java.json` : arêtes `access` application ↔ profil, `fls_read` / `fls_edit` (champs standard `AccountId`, `ContactId`, `Origin` présents ; `Status`, obligatoire, n'a pas d'entrée), `class_access` : ont servi directement pour le périmètre des profils.
- `xref_component_java.json` : `child` et `places` pour trouver les hôtes de `lwcTable` en quelques lignes ; `assigns` pour relier application et page.
- `xref_fields_java.json` : `formula_depends_on` avec relations traversées (`CreatedById`, `User.x`) ; `reads` / `displays` / `exposes` pour la liste des lecteurs d'un champ.
- Les attributs `source` (`deterministic` / `inferred`) pour doser les affirmations.
- `data_skew.json` : volumes par propriétaire, qui ont validé que « Léonard AA » est un utilisateur dédié.
- Les fichiers `.md` accompagnant chaque JSON et la section « Known limit », qui ont évité des erreurs d'interprétation.
