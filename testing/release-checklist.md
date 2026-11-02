# Native plugin licensing and release checklist

Complete the following with the collaborator's actual product, SKU and target 3ds Max version. Record build IDs, screenshots, logs and outcomes.

- [ ] Confirm Integration Specification identity, product/variation SKU and integration type.
- [ ] Confirm all protected operations are denied without valid entitlement.
- [ ] Compile and load the plugin in every supported 3ds Max version.
- [ ] Install EXE with elevated privileges and confirm discovery/Installed In version.
- [ ] Confirm plugin operation with a valid activation.
- [ ] Confirm licence release/revocation blocks protected operations after authoritative revalidation.
- [ ] Confirm valid reactivation/recovery restores access without automatic seat acquisition.
- [ ] Test 15-minute cache and qualifying 24-hour network-only grace; confirm grace expiry blocks access.
- [ ] Confirm an explicit Bridge denial is never treated as an offline network failure.
- [ ] Test Standard User operation with separate per-user activation state.
- [ ] Test uninstall: plugin binaries and installation metadata removed, entitlement preserved.
- [ ] Refresh shared Plugin Licensing application if Installed In initially shows stale data after uninstall.
- [ ] Test reinstall, supported-version selection, running-3ds-Max warning and UI branding.
- [ ] Confirm customer download contains only the collaborator's delivery files, not development SDKs, secrets or tests.
- [ ] Make a test purchase and verify separate platform requirements, Plugin Licensing application and customer Read Me for eligible products.
- [ ] Record final approved commit, CI run, artefact hashes and manual test results before declaring production release.
