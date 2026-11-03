# Sinilab.ai Native C++ Plugin Integration Specification

## Product
- Collaborator: Collaborator Demo
- Product: Native Licensing Test
- Target Application: 3ds Max
- Product Code: `collaborator_demo_native_test` (authoritative WooCommerce SKU)
- Integration Type: Host + Sinilab.ai Licensing

## Engineering requirements
- Integrate only the collaborator-owned native plugin; do not modify the Sinilab.ai licensing Bridge or shared licensing application.
- Preserve the plugin's existing functionality, installer, build process and UI.
- Build compiled 3ds Max plugin binaries against the matching Autodesk SDK and version; use a collaborator-managed Windows EXE installer to select supported 3ds Max versions. Do not package native plugins as MAXScript MZP files.
- For licensing, use the official Sinilab.ai Native Licensing SDK public API, registering the exact Product Code and enforcing entitlement before protected operations. Do not implement a separate Bridge client, licence key store or activation interface.
- Respect existing 15-minute validation, 24-hour network-only offline grace, authoritative revocation and recovery rules.
- Supply human-readable build instructions, dependency versions and automated tests. GitHub Actions and CMake are supported examples, not mandatory tooling.
- An optional native starter project and AI-ready guidance may be used, but human-written C++ and existing build pipelines are equally supported.
- Do not include development SDK sources or guides in customer downloads.

## Installer identity and branding
- Treat **Collaborator Demo** as the named product author and primary installer identity; never substitute the generic word "Collaborator" for their actual name.
- Use **Native Licensing Test** as the product identity. Derive the collaborator and product names from the authoritative values above; do not ask the collaborator to re-enter them or hard-code them into bitmap artwork.
- Preserve a collaborator's existing functioning installer, branding, installer technology and layout. The collaborator owns their EXE installer, supported 3ds Max version selection and updates.
- If a new installer or branding refresh is needed, the validated Phase 3.2e RC1 pattern is an available reference: a reusable, generic dark-colour sidebar, runtime text labels for collaborator name, product name and platform, and a smaller official **Licensed by Sinilab.ai** footer. No collaborator-specific artwork is required.
- In an Inno Setup implementation, use transparent `TLabel` controls over the generic sidebar image for dynamic text. Do not use opaque `TNewStaticText` overlays, which caused white rectangles in the tested build. Do not assume the same control API exists in other installer technologies.
- Keep the official Sinilab.ai identity secondary. Use only supplied approved Sinilab.ai assets; do not generate, redraw or substitute its logo. Do not impose Inno Setup or the example artwork on existing collaborator installers.
- Use the actual plugin version and supported 3ds Max versions from collaborator build metadata and tested binaries; do not infer them from the product name or assume all Max versions are supported.
- The installer must install only the compatible native binaries and the required product registration metadata, and must not change the shared Sinilab.ai licensing runtime, Bridge, customer licence keys or activation state.
- Uninstalling the plugin must remove its binaries and installation metadata without deactivating or releasing its licence. Do not add an uninstall control to the shared licensing application.
- Test installer compilation, welcome and finished page rendering, correct product identity, supported-version installation, product discovery, licensed plugin operation, uninstall and reinstall. Do not claim the installer validated until those tests pass.

## Delivery
- Collaborator supplies their plugin installer and maintains plugin versions and updates.
- Sinilab.ai provides the shared Plugin Licensing application and customer Read Me as separate platform entitlements for licensed native products, once the platform product has been configured and tested.
- Do not claim a production installer or supported SDK API exists beyond the supplied official SDK files.
