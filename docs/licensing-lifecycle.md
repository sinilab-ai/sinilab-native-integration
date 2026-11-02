# Licensing architecture and lifecycle

**Source baseline:** Phase 3.2e RC1 repository public headers and release README; final production lock remains outstanding.

The Sinilab.ai Bridge is authoritative. The native SDK is the client-facing integration layer; a collaborator's plugin should use the SDK rather than its own HTTP client or licence storage.

- **Product identity:** exact WooCommerce SKU from the Integration Specification.
- **Access control:** check entitlement before protected operations; deny access when the SDK snapshot is not allowed.
- **Validation cache:** 15-minute cached validation; refresh according to SDK policy.
- **Network-only offline grace:** 24 hours from the last successful validation, subject to SDK rules. This is not permission to ignore revocation or treat an explicit denial as a network failure.
- **Revocation and recovery:** Bridge decisions govern access. Released/revoked states must block protected operations; recovery requires valid authorisation, not automatic seat acquisition.
- **Credential protection:** per-user DPAPI-protected local activation state; no collaborator-owned raw key store.
- **Discovery:** machine-wide registry metadata identifies installed products but **does not grant entitlement**.

The shared Sinilab.ai Plugin Licensing application manages customer activation. A plugin installer must not overwrite, uninstall or modify that application.
