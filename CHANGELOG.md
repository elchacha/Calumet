# Calumet — Changelog

## v11.6 — 2026-08-02

### New screens
- **Org Discovery** — a 6-view analysis hub that reads the dependency graph to give an overall picture of the org: state of play, architecture, security posture, performance, migration and a unified technical-debt register, with an A–F Org Health Score.
- **Automation Radar** — an execution map per object and event showing where Flows, triggers, workflow rules and processes overlap or conflict, split into five focused views instead of one dense page.
- **Flow Migration** — a prioritized, risk-ranked migration plan for workflow rules and processes that reach end of life.
- **Permission Blast** — shows who actually loses (or gains) access before you change a profile or permission set.
- **License Right-Sizing** — tells you which seat each user actually needs, based on what they really use.

### Improvements

**Dep Graph**
- A sandbox can now display its linked production graph live, and sandboxes link themselves automatically; the interface is fully in English.
- The viewer opens on the Explorer, hides empty sections, and its payload is 73% lighter, so it renders far faster and no longer re-renders on every restart.
- You can open the exact source file and line of a reference directly in your IDE from the viewer.
- New "alive only through tests" signal, an Orphan tests view, test-only clusters and the option to hide test classes; the signal is also surfaced in Fields Not Used, CustomFields Usage and Object Activity.
- Security analysis now covers field-level security and per-operation CRUD, and Apex references to platform events are no longer missed.
- A stale graph cache now announces itself instead of silently returning outdated results.

**SOQL**
- Records can now be edited directly in the result table, including mass-setting a value on several rows, with picklist-aware editing and validation before saving.
- A new "All fields" toggle for SELECT *, and a cleaner toolbar, autocomplete and editing experience.

**Picklists**
- Usage is now shown with graduated badges and a centered value matrix; copy-paste from the tables works again.

**Search**
- The Usage column is split into Direction and Relation, with a pivot-search button, usage badges and a proper loading state.

**PermissionSet**
- The screen no longer freezes when you open it, the history is easier to read, and the audit-history popup gained a Name column and more width.

**User Access Comparison / User Access Score**
- New actions on permission sets, a merge assistant, scoped facts (tabs, apps, record types), and clicking a row now adds the user to the comparison instead of replacing the selection.

**All Relations**
- The Reference column is no longer truncated: a popup lists the full set of references, enriched with graph data.

**Logs**
- A filter-list popup, toggleable type badges with soft highlighting, and a rebuilt filter popup in the analysis window.

**Deployment**
- The post-deploy security check is now a readable table with an AI prompt and an alert on newly created permission sets, and it no longer floods the output with INVALID_TYPE/INVALID_FIELD messages.

**Comparison**
- Lines that only differ by indentation are no longer reported as changed.

**CustomFields Usage**
- Standard picklist fields are now analysed too, so unused values are detected on them as well.

**HistoryStorage**
- Evolution badges are now graded and keep their colors outside the IDE.

**Control**
- "Use Cache" is unchecked automatically when the window is opened after the cache was built.

### General
- Every text field in every screen now has a clear "x" button.
- Switching orgs is much faster: the screens that did synchronous work now load in the background instead of freezing the interface.
- Tabs were renamed and re-described from a single source, with multi-category filtering and no more Dev/Admin segmentation.
- Aggregate queries are safe on Large Data Volume orgs, and data skew / relation power analysis was added.

---

## v11.5 — 2026-07-22

### New screens
No new screens in this release.

### Improvements

**PermissionSet**
- The last-modified date is now taken from the org audit trail, and a per-permission-set History popup shows who changed what over the past six months (built in the background so it opens instantly).

**Logs**
- The debug-log analyser was reworked: a non-blocking popup, a statistics bar summarising log entry types, and a smoother tree view.
- The Status column no longer stretches when a failure message is long.

**FlexiPage Diff**
- Modified cards now show a visible expand chevron and highlight the exact inline differences, with a force-refresh option.
- Fixed encoding glitches (dashes/ellipses) in the diff output.

**Control**
- You can open a component-level FlexiPage diff popup directly from the Control table.

**Fields Not Used**
- Field references are now read from the Dep Graph instead of re-querying the org, making the screen faster and consistent with the other analysis screens.

**Field Catalog**
- The top panel and column headers now stay pinned while you scroll the catalog.

### General
- An Intel (x86-64) macOS build is now available in addition to Apple Silicon — both Mac types are now covered. Windows and Linux are unchanged.

---


## v11.4 — 2026-07-18

### New screens
No new screens in this release.

### Improvements

**Dep Graph**
- Link confidence is now shown as colored badges with a star rating, and every reference carries a colored dot indicating how it was detected — proven, heuristic or dynamic.
- The dependants counter now counts each component once, instead of being inflated when the same component is detected through several methods.
- Groups you expand by hand now stay open when you toggle a filter.
- Dependency detection is more accurate: custom buttons and links, New-action Lightning component overrides, SOQL sort clauses and Flow record-lookup field mappings are now traced.

**Calumet Config**
- A new "Anonymize metadata names (Demo mode)" option masks object, field and class names during live demos.

**General**
- A macOS build is now available, alongside Windows and Linux.

---


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

**Dep Graph & Storage Evolution**
- Fixed a crash that could close the application when opening these screens.

**Field Catalog**
- The Standard, Managed and Formula filters now start unchecked by default.

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
