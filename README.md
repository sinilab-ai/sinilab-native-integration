# Sinilab.ai Native Plugin Integration

Official engineering guidance for collaborator-owned native C++ plugins integrating with Sinilab.ai licensing.

**Status: documentation candidate v0.2 — review before publishing.** The Phase 3.2e RC1 reference has completed functional testing, but its final production SDK release and public binary distribution have not been approved. This repository is not yet a standalone build kit.

## For collaborators

1. Create your product in the Sinilab.ai Collaborator Store and set its canonical SKU.
2. Open **Licence + Integration**, select your product and integration type, and copy the generated **Integration Specification**.
3. Give that specification and your existing plugin source to your preferred AI engineering assistant or developer.
4. Ask the assistant to follow [the engineering handover](docs/ai-assistant-handover.md) and [native integration guidance](docs/native-licensing-integration.md).
5. Test, package, upload and test-purchase your finished plugin before publishing.

You do not need to manually assemble SDK files to begin. Your engineering assistant will need access to the approved SDK build dependencies before compiling.

## Engineering resources

- [AI assistant handover](docs/ai-assistant-handover.md)
- [Native licensing integration](docs/native-licensing-integration.md)
- [Architecture and lifecycle](docs/licensing-lifecycle.md)
- [Build and GitHub Actions](docs/build-and-github-actions.md)
- [Installer and registration](docs/installer-and-registration.md)
- [Testing checklist](testing/release-checklist.md)
- [Release and publication gates](docs/release-and-publication.md)
- [Resource status and outstanding dependencies](RESOURCE_STATUS.md)

## Boundaries

Collaborators retain ownership of their plugins, source, build processes and installers. Sinilab.ai maintains the shared licensing system. Never modify the Bridge or shared licensing application; do not create a competing activation interface or key store. Native C++ plugins require version-matched Autodesk SDK builds and collaborator-owned Windows EXE installers, not MZP packages.

Do not include development SDK files or engineering resources in customer downloads. The Sinilab.ai Plugin Licensing application and customer Read Me are provided separately for eligible purchases.
