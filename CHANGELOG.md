# Calumet — Changelog

## v11.3 — 2026-07-18

### New screens
No new screens in this release.

### Improvements

**CustomFields Usage**
- Sort the analysed-objects list by name, record count or date, with a one-click direction toggle.
- The progress bar reappears when you return to the screen while a mass analysis is still running.
- A "delete ids after analysis" option frees disk by removing the record-id files once a run finishes.
- Publish the computed analysis to the org and load it back on another machine to share results without re-running.
- The API-usage confirmation popup no longer cuts off its last line.

### General
- Fixed an intermittent freeze where switching screen categories could stop screen switching until a restart.

---

## v11.2 — 2026-07-03

### New screens
No new screens in this release.

### Improvements

**Tab chooser**
- The tab picker popup now has a category filter bar to quickly narrow the list of screens by category.

**SOQL**
- Multiline queries are now handled correctly in query backup, autocomplete and syntax highlighting.

**DataSeeding**
- Exporting now requires a configuration directory: a clear guard with a red message prevents runs that would otherwise fail.
- The export guard dialog was redesigned for readability.

### General
- Metadata retrieve polling now uses a capped exponential backoff (about a 34-minute ceiling), reducing load during long retrieves.

---

## v11.1 — 2026-06-21

### DataSeeding
- Disabling automations now also covers Validation Rules and Workflow Rules via a unified metadata deploy pipeline — the backup ZIP is the single source of truth for the pre-disable state.
- Check Status now shows how many flows, triggers, validation rules and workflow rules are pending restore when the org is disabled.
- The import progress table now shows how many records were actually inserted when errors occurred (e.g. 7030/7381), making partial imports easier to assess.

### General
- Fixed the org selector losing its displayed name after a config reload (e.g. after a deploy or org edit).

---

## v11 — 2026-06-13

### New screens
- **PermSet Overlap** — Compare two or more permission sets side by side and identify redundant or conflicting permissions across your org.

### Object Activity
- Objects with dependencies now show a Dependencies column — click any row to load its Tooling API dependency list on demand.
- Status badge filter buttons (Active / Stale / Empty) appear above the list for instant narrowing. Last Modified column is sorted by default. Object name is shown in bold.

### User Access Score
- Six-component score breakdown (Field, Setup, Custom and more) is now shown directly in the detail panel.
- Configurable weight profiles let you re-score users instantly without re-extracting data.
- Effective (deduplicated) scores now drive ranking and color coding.
- Permission-set names in the detail table are clickable links that open the record in Salesforce.

### ComparePermissionSet
- Permission-set XML files are now reused from the toolingCache populated by the Permission Set Dump screen, skipping a redundant Metadata API download when data is already available.

### Permission Set Dump / Popup
- Duplicate and missing permission set components that were previously silent are now extracted correctly.
- Checkboxes in the popup replaced with visual emoji indicators.
- The permission-set description is now shown in the popup header.
- Underlined, single-click column names open the corresponding Salesforce record directly.
- Double-click on field/object rows opens the correct section in Salesforce setup.
- The Settings URL in the popup is now clickable.

### Object History
- The rename popup now pre-fills the current name for faster edits, with a Clear button to start fresh.

### TestClass
- Hide checkboxes are now mutually exclusive (hiding one set un-hides the other).
- A Package.xml button lets you export passing classes as a deployment package.
- Delete Selected is disabled when nothing is selected.

### ChangeTracker
- A single "Use Cache" checkbox replaces the previous options; the cache date is now color-coded by age.

### DataSeeding
- A Related Objects button lets you select objects related to the seed object for inclusion in a seeding run.
- A Main column scopes relation traversal from the seed object.
- An interactive Tutorial button opens a step-by-step guided tour.

### General
- The application now adapts its minimum size to the screen, preventing content clipping on small screens. The top bar is scrollable when the window is very narrow.
- Auto-update now uses GitHub Releases as the primary channel, ensuring reliable delivery of future updates.
- GitHub Actions workflow added for cross-platform packaging — produces self-contained Windows/Linux ZIPs with bundled Java.
- Local Maven repository committed to source control — enables CI builds without manual dependency setup.
- SQLite JDBC library (sqlite-jdbc 3.49.1.0) added.
- Fixed a crash on first launch when setting up the keystore: the popup now opens and saves correctly.

---

## v10.10 — 2026-05-20

### General
- Fixed a regression where the tab description panel (title, "?" button, description text) stopped displaying after upgrading from v10.x. The migration runner was re-applying v9.x migrations on every v10.x upgrade due to a version comparison bug, which overwrote the descriptions file with an outdated version.
- Fixed the migration runner to use file-position-based ordering instead of string comparison, preventing any future re-application of already-applied migrations.

---

## v10.5 — 2026-05-20

### General
- Tab help descriptions now load correctly when running from a fresh JAR installation, without requiring a previous installation.

---

## v10.4 — 2026-05-20

### Control
- A new Permission Set merge popup lets you compare and selectively copy permissions between two permission sets, with color-coded status badges, row highlights, and a Take All button.
- Fixed a regression that prevented double-clicking a Salesforce record link in the merge popup from opening it in the browser.
- The diff count for permission set files now accurately reflects only meaningful changes (whitespace-only differences are no longer counted).

### Relations
- Metadata cache is now initialized correctly on the first extract, preventing empty columns when no cache exists yet.

---

## v10.3 — 2026-05-08

### General
- Internal stability fixes and dependency updates.

---

## v10.2 — 2026-04-28

### General
- OAuth authentication flow fixed (ServerSocket and SimpleHttpServer compatibility).
- JVM argument fix for HTTP server module.

---

## v10.1 — 2026-04-14

### General
- OAuth hotfix applied.

---

## v10.0 — 2026-04-01

### General
- Major version release with new features and improvements.

---

## v9.9 — 2026-02-01

### General
- Stability improvements and bug fixes.

---

## v9.8 — 2025-12-01

### General
- Stability improvements and bug fixes.

---

## v9.7 — 2025-10-01

### General
- Stability improvements and bug fixes.

---
