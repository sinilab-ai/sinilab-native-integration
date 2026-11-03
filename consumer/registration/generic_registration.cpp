// Generic product-bound helper. Requires an approved redistributable PluginRegistry implementation.
// The product identity is generated from the authoritative Integration Specification.
#include "plugin_registry.hpp"
#include "product_identity.generated.hpp"
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    if (argc != 2 && argc != 3) return 2;
    const std::string action = argv[1];
    const sinilab::PluginRecord product{
        sinilab_product::product_code,
        sinilab_product::collaborator,
        sinilab_product::product,
        sinilab_product::version
    };
    sinilab::PluginRegistry registry;
    bool ok = false;
    if (action == "add" && argc == 2) {
        auto updated = product;
        for (const auto& existing : registry.discover()) {
            if (existing.productCode == product.productCode && existing.collaborator == product.collaborator)
                updated.installedIn = existing.installedIn;
        }
        ok = registry.registerPlugin(updated);
    } else if ((action == "add-version" || action == "remove-version") && argc == 3) {
        const std::string year = argv[2];
        bool supported = false;
        for (const char* candidate : sinilab_product::built_max_versions)
            if (year == candidate) supported = true;
        if (!supported) {
            std::cerr << "Unsupported or unbuilt 3ds Max version\n";
            return 2;
        }
        ok = action == "add-version"
            ? registry.addInstallation(product.productCode, year)
            : registry.removeInstallation(product.productCode, year);
    } else {
        // Full product deletion intentionally not exposed to installers.
        std::cerr << "Unsupported operation\n";
        return 2;
    }
    return ok ? 0 : 1;
}
