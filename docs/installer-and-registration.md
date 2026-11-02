# Installer and product registration

Native C++ plugins are delivered through a **collaborator-owned Windows EXE installer**. Keep a proven installer when it works; do not require collaborators to adopt the Create Cube test installer.

## Installer requirements

- Collaborator/product identity and artwork are primary. The authorised Sinilab.ai logo and “Licensed by Sinilab.ai” are secondary.
- Select only supported 3ds Max versions for which matching binaries have been built and tested.
- Install the native binary and product discovery metadata; do not install or modify the shared licensing application.
- Detect running 3ds Max and request manual closure before modifying plugin files.
- Uninstall removes the plugin binaries and its installation metadata, **not the licence entitlement**.
- Verify machine-wide discovery after elevated installation, including Standard User behaviour. Credentials remain per-user.

## Registry API verified in Phase 3.2e RC1

The public `PluginRegistry` header declares `registerPlugin`, `unregisterPlugin`, `addInstallation`, `removeInstallation` and `discover`. `PluginRecord` contains product code, collaborator, display name, version and installed-in information. Registration metadata does **not** grant access.

## Branding note

The historical Inno Setup reference used dynamic transparent `TLabel` text rather than opaque `TNewStaticText` controls to avoid white background blocks. Do not assume that Inno Setup control classes map directly to other installer frameworks.

**Status:** The supplied Phase 3.2e installer reference still uses TEST naming; it is not included as an approved public template. The separate Phase 3.2d installer archive is a test artefact, not a universal collaborator installer.
