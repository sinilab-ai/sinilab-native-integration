# Building native 3ds Max plugins with GitHub Actions

GitHub Actions is **optional**. An existing collaborator-owned Windows build pipeline is acceptable.

## Verified reference context

The Phase 3.2e RC1 archive describes Windows GitHub Actions run #86 at commit `397e00a` as successful for the SDK/reference build. The reference used Windows 2022 runners, MSVC v142 and the Autodesk 3ds Max 2024 SDK. This is **historical test evidence**, not an approval for a public reusable workflow.

## AI assistant checklist

1. Create or use a **private** collaborator-owned source repository; do not publish proprietary plugin source.
2. Confirm target 3ds Max versions and version-matched Autodesk SDKs.
3. Use approved SDK release artefacts and their documented headers/libraries. Never assume the public documentation repository contains them.
4. Provision Autodesk SDK dependencies lawfully through secured build secrets or a compliant internal cache. Never commit SDK installers, private download URLs or credentials.
5. Configure matching MSVC/CMake settings; compile `.dlu`/`.dlo` binaries as appropriate for the plugin.
6. Inspect build logs and artefacts. Run tests; install and verify in the actual supported 3ds Max versions.
7. Build the collaborator-branded EXE installer and validate its behaviour separately.

## Publication gate

No executable workflow is included in this documentation candidate. The Phase 3.2e test workflow references a TEST-named installer and a private Autodesk SDK URL secret; publishing it unchanged would be misleading. A reusable, sanitised workflow must be built and verified against an approved SDK distribution before release.
