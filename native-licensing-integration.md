# Native Licensing Integration — Engineering Reference

**Status:** Documentation draft v0.1 — review before publication  
**Basis:** Sinilab.ai Native C++ SDK Phase 3.2e RC1 archive (reference commit `397e00a`)  
**Scope:** Windows native C++ plugins for Autodesk 3ds Max; validated example targets 3ds Max 2024.

> **Release boundary:** Phase 3.2e RC1 is functionally validated but is **not a locked production SDK release**. This page describes interfaces found in the supplied archive; it does not provide a standalone buildable SDK or authorise use of unreviewed binaries.

## 1. Start with the Integration Specification

The collaborator creates their Sinilab.ai product and generates an Integration Specification from **Licence + Integration**. The engineering assistant must use that specification as the source of truth for:

- Collaborator and product identity.
- Target application and supported versions.
- Integration Type (**Host Only** or **Host + Sinilab.ai Licensing**).
- Exact **Product Code**, taken from the authoritative WooCommerce product or variation SKU.

Do not copy the Create Cube demo SKU into another collaborator's plugin. Inspect the existing source, build system, licensing arrangements and installer before making changes. **Host Only** must not silently introduce Sinilab.ai licensing.

## 2. Public SDK interfaces identified in RC1

The archive exposes these C++ headers:

| Header | Relevant interface | Purpose |
| --- | --- | --- |
| `include/licensing_client.hpp` | `sinilab::LicensingClient` | UI-independent licensing client constructed with the exact Product Code. |
| `include/sinilab_licensing.hpp` | `sinilab::Snapshot`, `sinilab::Status` | Licensing result and permitted/blocked state. |
| `include/plugin_registry.hpp` | `sinilab::PluginRegistry`, `sinilab::PluginRecord` | Plugin discovery and installation metadata; **not** entitlement. |

`LicensingClient` provides `open()`, `check(bool explicitRefresh = false)`, `current()`, `hasStoredActivation()` and `verifiedCollaboratorName()`. Its header also exposes an explicit-consent `activate(...)` operation; collaborators should use the existing shared **Sinilab.ai Plugin Licensing** application for customer activation rather than creating another activation interface.

`Snapshot` contains `status`, `allowed` and `reason`. **Only permit a protected operation when the SDK returns `allowed == true`.** Do not infer entitlement from registry entries, cached UI text or the presence of a licence key.

### Illustrative integration pattern (not a drop-in production example)

```cpp
#include "licensing_client.hpp"

// Product Code comes from this product's Integration Specification.
sinilab::LicensingClient licensing("YOUR_PRODUCT_SKU");

// At an appropriate lifecycle point, load an existing protected activation.
licensing.open();

// Check immediately before a protected operation.
const sinilab::Snapshot result = licensing.check();
if (!result.allowed) {
    // Block the protected operation; present suitable guidance using result.reason.
    return;
}

// Perform the collaborator's existing protected operation here.
```

This is a conceptual call sequence grounded in the RC1 header, **not** a complete 3ds Max plugin or a verified integration for another product. The final code must account for the plugin's lifecycle, error handling, UI thread and the approved SDK build/link configuration.

## 3. Runtime rules

- The Sinilab.ai Bridge is the licensing authority.
- A successful online validation is cached for **15 minutes**; refresh when required.
- After a qualifying network interruption, a previously validated licence can remain usable for **up to 24 hours after the last successful online validation**.
- Explicit rejection or revocation must not be treated as a network outage.
- Revocation blocks protected operations; restored entitlement permits recovery through normal validation.
- Stored activation credentials are protected per Windows user using DPAPI; another Windows account may need its own activation and available seat.
- Never automatically activate, consume a new seat or silently reactivate a released device.

Do not implement a second Bridge client, local key store, independent offline policy or replacement activation UI.

## 4. Discovery and installation

`PluginRegistry` records product identity and installed 3ds Max versions. RC1 uses machine-wide HKLM registration for installed products; registration requires appropriate installer permissions. **Discovery is not proof of licensing.**

The collaborator owns the version-specific native plugin binaries and Windows EXE installer. Build against the matching Autodesk 3ds Max SDK. Keep existing working build and installer arrangements where possible; GitHub Actions and the Create Cube project are optional examples, not mandatory workflows. Do not distribute Autodesk SDK files or package native binaries as MAXScript MZP files.

The installer must install compatible plugin files and registration metadata only. It must not replace or uninstall the shared Plugin Licensing application. Uninstallation removes the plugin and registration, **not** the customer's licence or activation. The licensing application may need a manual **Refresh** before the displayed **Installed In** field updates.

## 5. Engineering assistant checklist

1. Confirm the product's Integration Type, Product Code and target 3ds Max versions.
2. Inspect the collaborator's current source, build process and installer.
3. Obtain the **approved, complete SDK distribution** and build instructions from Sinilab.ai; this documentation page alone is insufficient for compilation.
4. Integrate the official SDK public interface and gate every protected operation on `Snapshot.allowed`.
5. Compile each supported plugin binary with the matching Autodesk SDK and verified toolchain.
6. Package a collaborator-branded Windows EXE installer, preserving an existing functioning installer where possible.
7. Test no activation, valid activation, cache refresh, network-only offline grace, revocation, recovery, Windows Standard User operation, uninstall and reinstall.
8. Verify the product's own installer is the customer download; Sinilab.ai supplies eligible shared licensing components separately.
9. Exclude SDK development sources, secrets, test credentials, internal workflows and Autodesk SDK files from customer downloads.

## 6. Availability and publication boundary

The public integration repository currently provides guidance only. **The complete approved SDK, exact binary/linking instructions and reusable example workflows are not yet published here.** Do not claim that an assistant can complete a production integration using this document alone.

Before making this page authoritative, Sinilab.ai must approve the distributable SDK interface/package and provide a stable versioned release location. The private SDK development repository must remain private.
