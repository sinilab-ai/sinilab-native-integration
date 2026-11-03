#pragma once
#include "licensing_client.hpp"
#include <string>

namespace sinilab::demo {
// The plugin must invoke this before every protected cube-creation operation.
// A registry entry or UI status alone is never evidence of entitlement.
inline constexpr const char* ProductCode = "collaborator_demo_native_test";

class CubeGate {
public:
    CubeGate() : client_(ProductCode) { client_.open(); }
    Snapshot checkBeforeCreate() { return client_.check(); }
private:
    LicensingClient client_;
};

// Called by the future Autodesk SDK-backed plugin only after checkBeforeCreate().allowed.
// This callback separation makes it impossible for the example gate to create a cube
// or claim Autodesk compatibility without an actual compiled 3ds Max plugin.
template<class CreateCube>
bool tryCreateCube(CubeGate& gate, CreateCube&& createCube, std::string& explanation) {
    const Snapshot result = gate.checkBeforeCreate();
    if (!result.allowed) {
        explanation = result.reason.empty() ? "Sinilab.ai licence validation required" : result.reason;
        return false;
    }
    createCube();
    explanation.clear();
    return true;
}
} // namespace sinilab::demo
