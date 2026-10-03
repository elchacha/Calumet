# Calumet — Changelog

## v13.1 — 2026-10-03

### New screens

No new screens in this release.

### Improvements

**Orgs Configuration**
- The window no longer opens flattened when only a few orgs are configured.

**Dep Graph**
- The build button reads "Compute from org" when the org has no graph yet.
- A sandbox that displays its linked production graph no longer offers to build its own.
- A custom metadata type that points to another one (Metadata Relationship field) now appears as a relationship in the data model.

**General**
- Menu entries no longer end with "...", which read as cut-off labels (Dep Graph Tools and sharing menus, Description Debt, License).
- The record deletion confirmation (SOQL screens) is now in English, and its Cancel button is no longer green.

---

## v13 — 2026-10-03

### New screens

No new screens in this release.

### Signed updates

- Every update is now checked against a digital signature before anything is installed: a file that does not match exactly is refused, and an interrupted update rolls back to your current version.

### Security

- Excel files are now read and written with Apache POI 5.5.1, which fixes known vulnerabilities in Excel file reading.
- The Salesforce sign-in only listens on your own machine and rejects forged sign-in replies; XML files are read without external entities; a refreshed token is never written in clear text when no master key is set; shared dependency-graph packages can no longer write outside their folder.

### Improvements

**Empty Roles** (formerly UserRoles)
- See when each role was emptied and created and what still references it, run a free check without the dependency graph, and get warnings before deleting.

**User Access Score**
- Assign / UnAssign asks for confirmation on a production org before writing.

**Object Limits**
- Sorted by usage % by default, with red / orange / yellow / green badges.

**RecordTypeUsage**
- The number of queries is announced before extraction, with a choice to read or extract, a progress bar, automatic reading per org, failed objects listed, and an Export to json that includes the definitions.

**Fields Not Used**
- Exclusive Graph refs filters, a counter that says what it hides, and an Export to json.

**UnusedApexMethod / Object Relations**
- Results now open in an interactive page; unused methods are grouped by class, with exclusive filters, and a double-click opens the class.

**All Relations**
- The Legacy SOQL option is gone (the fast extraction does the same); one reference is shown, then "+N more".

**Dep Graph**
- Roles are now linked to the sharing rules, queues, groups, approval processes and alerts that use them; field links on Event/Task fields declared on Activity are no longer lost.
- References window: all columns visible and centred, full names, and the Active column only appears when a row is inactive.

**General**
- Calumet uses about 10% less memory on large orgs.
- Three rarely used screens were retired: SoqlCounter, RemoverHelper and FlexiPagesConditionalRules.
- Org Discovery: a shorter confirmation dialog.

---

## v12.3 — 2026-10-01

### New screens

**Analytics** — the reports, dashboards, folders and report types of a production org, in a
step-by-step path: see what nobody runs, archive abandoned dashboards first, then reports, then
hide unused report types. Each step comes with a ready-to-copy instruction for your AI assistant,
and reports can be downloaded in a resumable background run.

### Improvements

**CustomFields Usage**
- The API usage estimate opens in a clear window: a gauge of your 24-hour API limit, the detail per object, and objects already analysed left out of the total.
- A floating monitor follows the analysis: org, one progress bar per object (listing ids, then analysing), record counts, why an object was skipped, and a Stop button; you are warned when the machine is busy.
- The monitor now shows the download of record ids for each object, instead of bars that froze near the end.
- Objects already analysed are skipped before their record ids are downloaded, not after.
- Large objects download much faster: pages of record ids no longer wait 5 seconds each.
- File contents (ContentVersion and other file fields) are never read, so file objects no longer download every file.
- When you start an analysis, you are warned about selected objects with few custom fields, and can remove them or go on.
- The Progress and Records columns of the monitor now sort correctly, and your sort is kept.

**DataSeeding**
- The free version now seeds up to 10,000 records per run (was 1,000), and a free license is available on request; the export warns you when the volume exceeds the limit.
- A plan that no longer matches the Start query is flagged in red; changing the Start query asks first, then clears the plan and the exports derived from it.
- Redesigned Config step (numbered cards, Save & Next) and a Legends window explaining the columns, limits and buttons.

**Orgs Configuration**
- A red PROD badge and a Production / Sandbox / Unknown filter; an org linked to a production is now recognised as a sandbox.

**SFDX**
- The org list fills itself at startup when the sf CLI is installed.

**Access & Provenance**
- A Details button on account cards lists every login of the period; login times get filters and a reading guide; server-side OAuth hops no longer count as a country.

**Automation Radar / Flow Migration / Object Activity**
- "Start AI session" works in a folder of your own and reads the dependency graph in place; an Open folder button sits beside every AI prompt.

**Dep Graph**
- More accurate links to profiles (lookup filters, formulas, page visibility rules); the Dashboards view moved to the new Analytics screen.

**General**
- Tab chooser: tabs sorted alphabetically, a new Seeding filter, and licensed screens are hidden without a license.
- Calumet now only contacts Salesforce and GitHub: charts are bundled in the app, and the connection test probes github.com instead of google.com.
- One field no longer shows two overlapping suggestion lists; button labels no longer end with "…".
- SOQL autocomplete suggests standard objects again on installed versions, the "Default queryable objects" window is no longer empty, and rebuilding an Apex debug log works again.
- Settings: the "Use restrictive connected App" option is gone; new installs always use the restrictive connected app (an install that had unticked it keeps its setting, so existing connections keep working).
- Security hardening: audit pages can no longer run code coming from org data; the OAuth sign-in checks the server certificate name; archives can no longer write outside their folder; on Linux the browser is opened without going through a shell.
- The in-app help pages no longer contain real customer data.

---

## v12.2 — 2026-09-29

### New screens

**Metadata Bundle** — build a deployable package from a few seed components: Calumet proposes
their neighbours from the dependency graph, grouped by type, you include or exclude each one
(reversibly), preview the package.xml live, then generate the package and retrieve it. A manual
add covers types the graph does not model (queue routing, presence and messaging configs,
embedded services, Apex test suites).

### Improvements

**Access & Provenance**
- Daily connection monitoring: an org can be monitored once a day automatically, without being
  opened; the "Collect now" button is gone.
- "Refresh API callers" says what it does, and is hidden for orgs already monitored daily.
- Countries: hover a country code for its full name and the account's login history (days, IPs);
  unapproved countries show in red; a popup lists every country seen with an "Approved" checkbox;
  accounts can be filtered by country.
- New "Two countries, one day" signal. Hovering a same-day entry details that day (countries, IPs,
  apps, statuses), and "Show login times" fetches the exact login timeline from the org.
- A period slider narrows the analysis window; actor cards on config changes can be pinned open;
  each signal badge has its own colour.

**Deploy**
- Pre and Post destructive changes each get their own tab (only the first one found was shown).
- The deployment reason is saved per project and pre-filled the next time the project is opened.
- A "Preview changes" button goes straight to the diff against the target org.
- The failure report separates component failures, test failures and coverage warnings, each
  counted.

**Description Debt**
- Glossary: a new "Ask AI" step hands every unjudged acronym to your AI CLI (one line to paste),
  and a "Review" step loads its answer. What the model read in the org is offered for one-click
  confirmation; what it only knows from general knowledge arrives as a hypothesis you accept or not.
- Glossary > Ask AI: a long list is worked in blocks of 40 (one sub-agent per block when your CLI
  has them) and the answer file is saved after every block — a stopped session no longer loses
  everything, and the last acronyms get the same care as the first.
- Glossary > Ask AI: steps 2 and 4 say they become available once step 1 has written the
  instructions; "Load the AI answer" is now step 5 (step 6 goes to Review), and both stay greyed
  until the model has written its answer.
- Glossary > Review: "Risk" is renamed "Impact" with Confidence right beside it; the Status column
  is gone, leaving room for Evidence; the import report opens tall enough to read without
  scrolling.
- Glossary > Review: once every packet is empty, search, legend and decision buttons step aside
  (Save stays while something is unsaved; opening Settled brings them back). A Cancel button beside
  Save drops unsaved changes; on Settled the decision buttons only show once an edit needs saving.
- Glossary > Hypothesis: rows arrive ticked — untick what you doubt. Accepting with every row still
  ticked asks first and names the high-impact ones.
- The glossary can be published to and pulled from a shared store in the org, so a team shares its
  decisions; conflicting decisions are listed at publish time instead of being resolved silently.
- An acronym's occurrences in Apex and Flows open as text; acronyms seen only in developer tags
  (signatures, debug-log prefixes) are flagged as noise.
- The built-in AI suggestion loop for field classification was retired from this screen; AI help now
  goes through your AI CLI.

**Dep Graph**
- New "Apex Clones" view: groups of duplicated Apex code (production, test-only, literal copies).
- New "Dashboards" view: which dashboards are reachable and how, with search, verdict filters and
  a live progress indicator.

**Object Activity**
- AI-assisted deletion review shows a Details popup with the exact pre/post/package.xml proposed,
  warns about orphaned package.xml entries and email templates that would survive a deletion,
  applies safe mechanical source cleanups (formula, lookup filter, layout) itself, and survives
  closing and reopening Calumet.
- A deletion batch is checked against the dependency graph before the AI review, so the AI only
  covers genuine blind spots.

**History**
- Two backups can be compared with each other, not only a backup against the org.
- The search filter matches what the table shows (name, author, date); other fields need an
  explicit prefix.

**SOQL**
- On narrow screens the "Saved queries / Export" block hides behind a toggle button instead of
  truncating every label.
- Records are deleted from the Id column only; Delete/Backspace no longer deletes while you type in
  a cell.
- A cancelled query no longer keeps showing "Fetching x / y" over the next one.

**Validation Rules**
- Extraction runs in the background with a progress bar instead of freezing the window.

**Relations**
- Type badges filter exclusively (click = only that type, click again = all).
- All Relations / Relations by Object: the primary master of a junction object shows as
  "Junction (P)", and junction parents are flagged "Controlled by".

**Logs**
- "Create / Update" stays disabled until a debug level, duration and entity name are entered.

**Org Discovery**
- Objects and Apex classes are no longer ranked in the same top list, and each count says what it
  counts.

**AI assistant connection**
- The connect popup has Quick start and Help tabs: one ready-to-copy sentence per use case (guided
  audit, one-off question) instead of a long brief to paste.

**General**
- Tabs renamed: "Profiles Editor" is now "Profile Changes", and the seed-to-package screen shows as
  "Metadata Bundle" (it was wrongly titled "Compare 2 Profiles").
- Windows, multi-screen: Calumet is now Per-Monitor DPI aware (declared in Calumet.exe). Moving the
  window to a screen with a different display scale (e.g. 100 % -> 150 %) no longer leaves the
  toolbar, the Org selector or its menu misplaced — the window is re-created at the right scale
  (brief flicker).

### Fixes

- Compare 2 Profiles/PermSets: the "Compare 2 Profiles" sub-tab had lost its title and description,
  and a stack trace was logged at startup.
- Per-record Tooling queries (validation rules, workflow rules, flows...) no longer open one
  connection per record — they could time out on large sandboxes and silently return an incomplete
  list.
- Validation Rules: extracting twice no longer lists every rule twice.
- FlexiPages filter rules: extraction crashed when the cache held a deleted or non-record page.
- Soql tab could open completely blank on a 150 % screen (corrupted emoji image cache) — the cache
  is now repaired automatically at startup.
- Calumet config window: the Security section was cut off at the bottom; "Manage default queryable
  objects..." failed with "Stage already visible".
- Change Tracker: a multi-second freeze the first time the screen was opened.
- Search, Debug, LastRecords, Formula: after a failed extraction these screens show an honest
  partial result instead of stale or misleading counts.
- PermissionSet: opening a permission set popup while its cache was still loading crashed.
- Profile Changes: label translation works again (it failed silently for most fields).
- The org's display language could stay stuck in English after a crash or with two Calumet
  processes on the same org.
- Object Activity / Dead Metadata: more accurate dependency graph (roll-up summary fields, objects
  never retrieved directly, custom console components, formula references, custom labels and
  layouts), so fewer false "dead" flags and safer deletion batches (report types, orphan fields,
  email template folders, approval processes).
- DataSeeding: the active configuration can no longer be switched while an export/import runs.
- Org score: the "Automation Conflicts" term, which measured zero on every org, no longer weighs on
  the score (the data is still shown).
- Confirmation popups are centred when they open and no longer leave the application waiting after
  they close.
- Errors that left a tab blank are now written to calumetTool.log.

### Notes

- Screen descriptions are refreshed on first launch (new tab titles, restored sub-tab description).

---

## v12.1 — 2026-09-16

### New screens

No new screens in this release.

### Improvements

**SOQL**
- The autocomplete suggestion list now opens right under the line you are typing on. It used to
  anchor to the top-left corner of the query panel, so on anything longer than one line it appeared
  far from the caret — and on a multi-monitor setup with different scaling it could open on another
  screen entirely.

**Compare 2 Profiles/PermSets**
- A third sub-tab, "Profile vs Permission Set", compares a profile against a permission set
  directly, alongside the existing Profile and Permission Set comparisons.

**Object Activity**
- "Ask AI" hands a deletion package to a model and brings its proposal back into the screen.
- "Build work package" produces a package again, and a source folder that looks empty no longer
  stops the screen from offering what there is to edit.

**Dead Metadata**
- The referents popup no longer repeats the same component several times when the graph knows it
  under more than one name (trigger, class and page aliases).

### Notes

- Screen descriptions are refreshed on first launch. The file had not been delivered since v11.8,
  so its newer entries were missing from installed copies.

---

## v12 — 2026-09-14

### New screens

No new screens in this release.

### Improvements

**General**
- **Linux downloads are back.** The previous release was published without any Linux package at all, so the Linux button on the download page led nowhere. Linux is built and published again.
- **Help panels read properly again.** On installs set up before March, the built-in help of 74 screens displayed garbled characters where bullet points belong. The corrected help text is delivered on first launch.

---

## v11.8 — 2026-09-14

### New screens

- **Description Debt** — see which objects and fields nobody ever documented, have descriptions drafted for you, review them inside Calumet, and push the accepted ones back to the org. It also keeps a glossary of your acronyms, so every proposal speaks your own business vocabulary.
- **Value Sets & Record Types** — an org-wide view of your picklist vocabularies: which value sets are exact duplicates of each other, which values a record type actually offers, and which fields consume each list.
- **Access & Provenance** — who really reaches your data, through which connected app or integration, how Calumet knows it, and what it cannot see. A daily collection builds a history that outlives your org's own log retention.
- **Dead Metadata** — the metadata nothing points at any more, from the verdict down to a ready-to-use deletion package, with a guided route and a record of what you decided.

"Compare 2 Profiles" is no longer a screen of its own: it is now the **Profile** sub-tab of **Compare 2 Profiles/PermSets**.

### Improvements

**Dep Graph**
- The build now tells you where it is: a progress bar with a readable step detail, per org, instead of a bar that stayed empty and looked frozen.
- The three optional retrieves run in parallel, so a full rebuild finishes sooner.
- The impact popup opens as a real window.
- The screen shows how far the documentation campaign has got, and what still needs a human.
- A new setting turns the dependency graph off, so you can see exactly what each screen loses without it.

**Org Discovery**
- The landing page is a grid of selectable tiles instead of a list.
- A banner says where the org stands, and a complete audit can be launched from the screen.
- The sequence of steps is visible, including the one that has no button.
- Decisions you already recorded in Dead Metadata no longer count as open debt.

**Automation Radar**
- "Busiest saves" shows the top 5 with an inline diagram instead of a long list.
- The Objects view is a grid of clickable tiles, with the detail in a popup.
- A handler called from a trigger counts as a writer again, and the async view reads the radar's writers instead of guessing them.
- The nature of each side of a conflict is a column you can filter on.
- Two accuracy problems fixed: a guard was hiding 36 real cross-writes, and the test-class filter matched nothing — 45 undecidable rows removed.
- Verbose blocks moved behind a "Details" button, and timelines fill the available width.

**Flow Migration, Permission Blast, License Right-Sizing**
- Two-row toolbars, so labels stop being truncated.
- Permission Blast: field permissions left behind without their field are now detected, and two different problems are reported as two different findings instead of one.

**Fields Not Used, CustomFields Usage, Dead Metadata**
- Deletion proposals are far more careful: silence is no longer taken as consent (on a real org, 1 027 proposed deletions became 189), an entry point is never proposed just because nothing points at it, a layout is only removed with its object when that is certain, and a chain containing something undeletable is no longer treated as safe.

**Object Activity**
- The Delete Helper lets you tick exactly what you delete and see the relations instead of just a count.
- The reference table no longer truncates, and the toolbar offers one button at a time.

**Field Catalog**
- The keep score no longer grades fields nobody has ever looked at.
- The two different meanings of "required" no longer mix.

**Logs**
- Compare two logs side by side, auto-refresh, and purge the cache.
- The Apex call tree highlights exceptions in red and shows self-time, with a governor-limits panel.
- SOQL 101 reports real total rows and sorts by worst volume.
- A deletion refused by the org is now visible on screen.

**SOQL**
- An "Edit mode" toggle on the editor.
- Exporting a large result set is faster and uses far less memory.

**DataSeeding**
- The seeding path reads as a sequence of steps rather than a form.
- Upsert by External Id, a "Retry Failed" button, a replayable failed-record CSV, and an inline progress log.
- An exhausted API quota is reported as such instead of being retried as a temporary error.

**Unused Apex Methods**
- In production, every private method used to be reported as dead — fixed. When the analysis is incomplete, the tool now says so instead of answering anyway.

**Permission Set**
- Assignment date and real change date are separate columns, with a filter in days.

**Orgs and connections**
- Local folders for sandboxes that no longer exist on Salesforce can be deleted, and the orphan list opens straight from the result that found them.
- OAuth applications live in one global vault instead of being re-declared in every org.

### General

- The org health grade never travels without the base it was computed on ("B (8/12)", never a bare "B"), unknown data counts as neutral instead of perfect, and every dimension tile says which audits feed it.
- Connection robustness: connection setup and socket timeouts are bounded, any 2xx response counts as a success, a write is never silently replayed, and a single HTTP client is reused.
- Speed and memory: permission scans, access-log reading (800 MB of heap down to 16), metadata corpora and SOQL exports are now streamed instead of accumulated in memory.
- One visual convention across audit reports and popups: numeric columns centred, long columns wrap instead of truncating, two-row toolbars, and a calculation in progress is no longer announced as "nothing found".
- Org folders are migrated to a new layout automatically on first launch, one org at a time, so a failure costs one org and never the whole set.
- The conversational audit assistant now covers the whole route — what to do next, the deletion plan for dead metadata, the glossary, and the description campaign — so most of an audit can be run without opening a screen.
- A demo mode can serve a fully anonymised org, so Calumet can be shown without exposing any client data.

---

## v11.7 — 2026-08-03

### Improvements

**General**
- Self-healing library repair — the updater now checks every library the application declares and re-downloads any that is missing, so a partially updated install repairs itself on the next launch instead of failing to start.

**SOQL**
- The query editor recovers its syntax colouring on existing installations.

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
