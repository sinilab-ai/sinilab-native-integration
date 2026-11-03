# Release notes — v1.0

**Authorised scope:** public distribution of the compiled SDK and PluginRegistry libraries, public headers, approved Sinilab.ai branding and collaborator integration instructions. No private source or Autodesk SDK included.

**Evidence:** GitHub Actions run #3 on `test-final-delivery-v1-0` succeeded (2m 17s), with packaged static libraries, generated specification metadata and branded Windows EXE. Earlier Stage 12.1 Windows test confirmed installation, Licensed status, Create Cube operation, uninstall removing Installed In 2024 while retaining entitlement.

**Important limitation:** This release is a **validated reference kit**, not a claim that every third-party product is already certified. Compiled libraries remain version/toolset-specific. Use MSVC v142 x64 with 3ds Max 2024 for this reference.

**Known technical debt:** GitHub Actions uses version tags for third-party actions rather than immutable commit SHA pins. Review and pin dependencies before production automation. The reference workflow retains 2024/Create Cube-specific build paths and must be adapted to the collaborator's real plugin.

**Security:** The release package was statically inspected for private implementation source and obvious credential patterns. This is not a formal binary security audit or ABI compatibility certification.
