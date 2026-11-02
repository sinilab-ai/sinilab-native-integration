# Release and publication boundaries

## Public integration documentation

The public repository is the discoverable home for collaborator-facing guidance. It may describe public interfaces and reference approved artefacts. It must not be treated as the private SDK source repository.

## Private SDK development

Keep internal implementation, Bridge adapters, protected state handling, unpublished tests, internal development logs and build secrets private. Do not copy the private repository wholesale.

## SDK release dependency

A real native integration needs actual approved SDK build files (headers plus linkable binaries or an explicitly authorised source distribution), versioned API documentation and dependency instructions. Choose a distribution model and verify it before calling this public repository a complete build kit.

## Release gates

1. Approve the SDK public API and distribution terms/licence.
2. Produce and verify a reproducible release build and checksums.
3. Sanitize optional GitHub Actions examples and remove any secret values, private URLs and historical TEST naming.
4. Validate installer examples and authorised branding against the approved baseline.
5. Publish only files approved for redistribution, with explicit versions and supported 3ds Max targets.
6. Update the Sinilab.ai website Integration Specification to link to the exact approved public resources.

Until those gates are complete, public documents must not claim production readiness.
