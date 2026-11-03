#pragma once
#include "sinilab_licensing.hpp"
#include <string>
namespace sinilab {
struct HttpReply {unsigned status=0;bool transportFailed=true;std::string body;};
// Windows-only, HTTPS with platform TLS validation. Never print response bodies.
HttpReply activateBridge(const std::string& product,const std::string& installation,const std::string& licenceKey,
                         const std::string& application,const std::string& applicationVersion,const std::string& productVersion);
// Strictly require a successful Bridge response and a nonempty refresh credential.
bool parseActivationCredential(unsigned status,bool transportFailed,const std::string& body,std::string& credential);
HttpReply refreshBridge(const std::string& product,const std::string& installation,const std::string& credential);
// All fields encrypted together with user-scoped Windows DPAPI; no plaintext fallback.
struct StoredState {std::string product,installation,credential;std::int64_t lastOnlineUnix=0;bool revoked=false;std::string collaboratorName;};
bool saveState(const StoredState& state);
bool loadState(const std::string& product,StoredState& state);
// Never automatically activate or consume a seat.
Snapshot refreshExisting(StoredState& state, LicensingPolicy& policy, bool& contactedBridge, bool explicitRefresh = false);
} // namespace sinilab
