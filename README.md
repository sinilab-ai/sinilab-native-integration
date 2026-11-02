# Sinilab.ai Native Plugin Integration

**Official integration resources for collaborators, AI engineering assistants and developers building native C++ plugins licensed through Sinilab.ai.**

## Welcome

Sinilab.ai helps independent software creators bring their products to market while retaining ownership and control of their work.

This repository provides the technical guidance, approved examples and integration resources needed to connect collaborator-owned native C++ plugins to the Sinilab.ai licensing platform.

It is designed to support experienced C++ developers and creators using AI-assisted coding, including collaborators with little or no traditional programming experience.

**Initial supported application:** Autodesk 3ds Max, with version-specific native plugin builds.

## Getting Started

The recommended integration workflow begins on the Sinilab.ai website.

1. Create your product in your Sinilab.ai Collaborator Store.
2. Open **Licence + Integration** and select the appropriate integration type.
3. Review the product details and generate your **Integration Specification**.
4. Copy the specification into your preferred AI engineering assistant, alongside your existing plugin source code.
5. Ask your assistant to follow the official technical guidance in this repository.

Your AI assistant or developer should guide you through the integration, compilation, installer preparation and testing process.

You do not need to manually assemble SDK components or install Visual Studio simply to begin.

## Instructions for AI Engineering Assistants

When provided with a Sinilab.ai Integration Specification:

1. Treat the supplied specification as the authoritative source of product identity, target application, integration type and Product Code.
2. Examine the collaborator's existing source code, build process, installer and licensing arrangements before making changes.
3. Preserve the collaborator's existing functionality, user interface, branding and development workflow wherever possible.
4. Use only the approved Sinilab.ai Native Licensing SDK public interfaces and documented integration patterns.
5. Do not implement an alternative licensing service, licence key store, activation interface or direct Bridge client.
6. Enforce licence entitlement before protected plugin operations.
7. Use the correct Autodesk SDK and toolchain for each supported 3ds Max version.
8. Support GitHub Actions compilation when the collaborator does not have a local C++ development environment.
9. Retain or create a collaborator-owned Windows EXE installer for compatible native plugin binaries.
10. Guide the collaborator through installation, activation, revocation, recovery, uninstall and reinstall testing.

Do not assume that historical examples, experimental workflows or unreleased SDK interfaces are approved for production.

## Licensing Architecture

The Sinilab.ai licensing platform provides a shared licensing system for supported products.

The Native Licensing SDK is responsible for connecting collaborator-owned plugins to that system through its approved interfaces.

The established runtime behaviour includes:

- A 15-minute cached validation interval.
- A 24-hour offline grace period for qualifying network interruptions.
- Authoritative licence revocation and subsequent recovery.
- Per-user protected licensing credentials.
- Machine-wide plugin discovery where supported.

Collaborator plugins must not replace or independently reimplement these licensing mechanisms.

## Compilation and Installation

Native 3ds Max plugins require binaries compiled against the appropriate Autodesk SDK and supported application version.

Collaborators may use an existing working build environment or an approved GitHub Actions workflow.

Native plugins must be delivered through a collaborator-owned Windows EXE installer. Do not package compiled native plugins as MAXScript MZP installers.

The installer must preserve collaborator branding, install the correct version-specific binaries and registration metadata, and must not overwrite or uninstall the shared Sinilab.ai Plugin Licensing application.

Uninstalling a collaborator plugin must not automatically release or revoke the customer's licence.

## Customer Delivery

Collaborators provide and maintain their own product installer and plugin files.

For eligible licensed native products, Sinilab.ai separately provides the shared Plugin Licensing application and customer Read Me through the purchase and download workflow.

Development SDK files, internal engineering resources, build credentials and test materials must not be included in customer downloads.

## Repository Resources

This repository will progressively provide:

- Approved Native Licensing SDK integration documentation and public interfaces.
- Optional Create Cube demonstration project.
- GitHub Actions compilation examples.
- Collaborator-branded installer guidance.
- Licensing validation and release testing checklists.

**Resource availability:** The repository is being prepared. An example or integration resource should only be used once it has been published and identified as an approved release.

## Responsibilities

**Collaborators** own their plugin, source code, product identity, installer, compatibility testing and final release approval.

**AI engineering assistants and developers** implement the integration using the official specification and approved technical resources.

**Sinilab.ai** maintains the shared licensing platform, its integration requirements and the approved SDK resources.

## Project Status

This public repository is the official location for Sinilab.ai native plugin integration guidance.

The underlying SDK development repository remains private. Technical resources will be added incrementally following review and validation.

Do not treat this repository as a complete standalone SDK distribution until an approved SDK release and its dependencies have been published.

---

**Sinilab.ai — Supporting independent creators and their software.**
