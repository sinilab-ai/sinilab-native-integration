#pragma once
#include <string>
#include <vector>

namespace sinilab {
// Discovery metadata only. Registry records never grant licensing entitlement.
struct PluginRecord {
    std::string productCode;
    std::string collaborator;
    std::string displayName;
    std::string version;
    // Display-only list of actual 3ds Max installations, e.g. "2025, 2026".
    std::string installedIn;
};

class PluginRegistry {
public:
    // Production root uses HKLM (machine-wide, administrator write required).
    // Custom roots use HKCU to preserve non-elevated isolated tests.
    explicit PluginRegistry(std::wstring root = L"Software\\Sinilab.ai\\PluginLicensing\\Products");
    bool registerPlugin(const PluginRecord& record) const;
    bool unregisterPlugin(const std::string& productCode) const;
    // Installer lifecycle: modify only the installed-version metadata.
    // Never changes licence keys, activations or Bridge state.
    bool addInstallation(const std::string& productCode, const std::string& maxYear) const;
    bool removeInstallation(const std::string& productCode, const std::string& maxYear) const;
    std::vector<PluginRecord> discover() const;
private:
    std::wstring root_;
};
}
