# Publish to `sinilab-ai/sinilab-native-integration`

1. Create a new branch `release-native-integration-v1-0` in the existing public repository.
2. Upload the **contents** of this ZIP at the repository root. Do not upload the ZIP as a single repository file.
3. Review the resulting Git diff and confirm no credentials, private implementation source or Autodesk SDK files are present.
4. Open a pull request into `main`; merge after review.
5. Create GitHub Release tag `v1.0.0` and attach this ZIP, using `RELEASE_NOTES.md` as the release notes.
6. Verify a clean clone can access both static libraries, public headers, reference workflow and approved branding.

The ZIP is a **public release payload**. Its creation does not itself update GitHub.
