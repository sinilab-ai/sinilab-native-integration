# Sinilab.ai Native C++ Integration Kit — v1.0

**Release scope:** 3ds Max 2024 native C++ reference integration, independently built and Windows runtime-tested with Create Cube. This is a developer integration kit, **not** a customer download or a pre-certified installer for arbitrary plugins.

## Start here

1. Copy your complete authoritative **Licence + Integration → Product Integration → Integration Specification** into `consumer/metadata/integration-specification.md`. The exact WooCommerce Product Code (SKU) must remain unchanged.
2. Replace the Create Cube example with your collaborator-owned native C++ plugin. Use only the supplied public licensing API and enforce entitlement before protected operations. Do not create your own Bridge client, key storage or activation UI.
3. Update `consumer/metadata/build-evidence.json` using **actual compiled output names**, real plugin version and supported 3ds Max versions. This file is not a second product-identity form.
4. Configure your **private** GitHub Actions repository with the secret `AUTODESK_MAX2024_SDK_URL`, pointing to your authorised Autodesk SDK MSI. The reference workflow uses MSVC v142 and Windows 2022. Do not commit Autodesk SDK packages or credentials.
5. Run the reference workflow or adapt your existing build. Test licensing, installation, revocation/recovery and uninstall on your own product before distributing its installer.

## Included

- Compiled Sinilab.ai SDK and PluginRegistry static libraries and public headers
- Specification-to-metadata parser, tests, and build preflight
- 3ds Max 2024 Create Cube source/CMake reference
- Generic registration helper and metadata generator
- Approved generic Inno Setup sidebar artwork and installer generator
- Windows GitHub Actions reference workflow

## Boundaries

- Only the Create Cube **2024 reference** has been independently compiled and Windows runtime-tested. Other products, Autodesk versions and installer technologies need their own testing.
- Collaborators own their installer, source, release cadence and supported Max versions. Preserve an existing working installer rather than imposing Inno Setup.
- Plugin uninstall removes plugin and discovery registration, **not** licensing entitlement.
- The Sinilab.ai Plugin Licensing application and customer Read Me are delivered separately by the platform; do not ship developer libraries, headers or guides to customers.
- Never distribute private SDK/registry implementation sources, Autodesk SDK archives, credentials or customer licence keys.

See `RELEASE_NOTES.md` for validation and limits.
