#pragma once
#include "live_bridge.hpp"
#include <string>

namespace sinilab {
// UI-independent, Windows-only SDK facade. It never requests a new seat.
// A host application calls check() before granting access to a licensed feature.
class LicensingClient {
public:
    explicit LicensingClient(std::string productCode);
    // Loads a DPAPI-protected activation created by a trusted integration.
    // Returns false if none exists or the saved state is invalid.
    bool open();
    // Refreshes only when required. No user interaction, console, or key entry.
    Snapshot check(bool explicitRefresh = false);
    // Explicit, UI-driven activation; consent must be true. Never auto-reactivate.
    // On success the DPAPI credential is persisted before access is granted.
    Snapshot activate(const std::string& licenceKey, const std::string& installationId,
                      bool consent, const std::string& application,
                      const std::string& applicationVersion, const std::string& productVersion);
    Snapshot current() const;
    bool hasStoredActivation() const;
    // Last verified Bridge store name; empty until the Bridge supplies metadata.
    std::string verifiedCollaboratorName() const;
private:
    std::string product_;
    StoredState state_;
    LicensingPolicy policy_;
    bool loaded_ = false;
};
} // namespace sinilab
