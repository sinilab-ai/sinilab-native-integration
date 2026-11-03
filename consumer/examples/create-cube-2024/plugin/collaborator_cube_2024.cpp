// Phase 3.0b: independently authored Autodesk 3ds Max 2024 Utility plug-in.
// The utility creates one native box when opened, but only after the Sinilab
// licensing SDK grants access. No Autodesk SDK files are distributed here.
#include <max.h>
#include <istdplug.h>
#include <utilapi.h>
#include <windows.h>
#include "collaborator_cube_gate.hpp"

namespace {
HINSTANCE g_module = nullptr;
constexpr int kLicensingIconResource = 101;

// Thread-local CBT hook applies the existing Sinilab.ai application icon to
// the standard Windows message-box title bar; message text/buttons unchanged.
LRESULT CALLBACK LicensingMessageHook(int code, WPARAM wp, LPARAM lp) {
    if (code == HCBT_ACTIVATE) {
        HWND dialog = reinterpret_cast<HWND>(wp);
        HICON iconSmall = static_cast<HICON>(LoadImageW(g_module,
            MAKEINTRESOURCEW(kLicensingIconResource), IMAGE_ICON, 16, 16, 0));
        HICON iconLarge = static_cast<HICON>(LoadImageW(g_module,
            MAKEINTRESOURCEW(kLicensingIconResource), IMAGE_ICON, 32, 32, 0));
        if (iconSmall) SendMessageW(dialog, WM_SETICON, ICON_SMALL, reinterpret_cast<LPARAM>(iconSmall));
        if (iconLarge) SendMessageW(dialog, WM_SETICON, ICON_BIG, reinterpret_cast<LPARAM>(iconLarge));
    }
    return CallNextHookEx(nullptr, code, wp, lp);
}
void ShowLicensingWarning(HWND owner, const std::string& reason) {
    HHOOK hook = SetWindowsHookExW(WH_CBT, LicensingMessageHook, nullptr, GetCurrentThreadId());
    MessageBoxA(owner, reason.c_str(), "Sinilab.ai Plugin Licensing", MB_OK | MB_ICONWARNING);
    if (hook) UnhookWindowsHookEx(hook);
}
constexpr Class_ID kCubeUtilityId(0x6c7b2310, 0x16a54b92);
class CubeUtility final : public UtilityObj {
public:
    void BeginEditParams(Interface* ip, IUtil*) override {
        if (!ip) return;
        created_ = false;
        std::string explanation;
        const bool allowed = sinilab::demo::tryCreateCube(gate_, [&] {
            // Autodesk's built-in Box primitive, not a custom geometry implementation.
            auto* object = static_cast<Object*>(
                ip->CreateInstance(GEOMOBJECT_CLASS_ID, Class_ID(BOXOBJ_CLASS_ID, 0)));
            if (!object) return;
            INode* node = ip->CreateObjectNode(object);
            if (node) {
                node->SetName(_T("Sinilab Licensed Cube"));
                ip->SelectNode(node);
                ip->RedrawViews(ip->GetTime());
                created_ = true;
            }
        }, explanation);
        if (!allowed) {
            ShowLicensingWarning(ip->GetMAXHWnd(), explanation);
        } else if (!created_) {
            MessageBoxA(ip->GetMAXHWnd(), "Could not create the 3ds Max Box primitive.",
                        "Create Cube", MB_OK | MB_ICONERROR);
        }
    }
    void EndEditParams(Interface*, IUtil*) override {}
    void DeleteThis() override {} // Static singleton owned by this module.
private:
    sinilab::demo::CubeGate gate_;
    bool created_ = false;
};
CubeUtility g_utility;
class CubeUtilityDesc final : public ClassDesc {
public:
    int IsPublic() override { return TRUE; }
    void* Create(BOOL) override { return &g_utility; }
    const MCHAR* ClassName() override { return _T("Sinilab Create Cube Test"); }
    const MCHAR* NonLocalizedClassName() override { return _T("Sinilab Create Cube Test"); }
    SClass_ID SuperClassID() override { return UTILITY_CLASS_ID; }
    Class_ID ClassID() override { return kCubeUtilityId; }
    const MCHAR* Category() override { return _T("Sinilab.ai Tests"); }
};
CubeUtilityDesc g_description;
}
extern "C" {
__declspec(dllexport) const MCHAR* LibDescription() { return _T("Sinilab.ai Licensed Cube Test"); }
__declspec(dllexport) int LibNumberClasses() { return 1; }
__declspec(dllexport) ClassDesc* LibClassDesc(int index) { return index == 0 ? &g_description : nullptr; }
__declspec(dllexport) ULONG LibVersion() { return VERSION_3DSMAX; }
__declspec(dllexport) ULONG CanAutoDefer() { return 1; }
}
BOOL WINAPI DllMain(HINSTANCE module, ULONG reason, LPVOID) {
    if (reason == DLL_PROCESS_ATTACH) g_module = module;
    return TRUE;
}
