#!/usr/bin/env python3
"""Consumer preflight: no fixture SKU or plugin binary names hard-coded."""
import json,re
from pathlib import Path
from importlib.machinery import SourceFileLoader
root=Path(__file__).resolve().parents[1]
meta=json.loads((root/'metadata/product-metadata.json').read_text(encoding='utf-8'))
assert re.fullmatch(r'[A-Za-z0-9_-]{1,96}',meta['product_code'])
assert meta['registration_product_code']==meta['product_code']
assert meta['target_application']=='3ds Max'
assert meta['integration_type']=='Host + Sinilab.ai Licensing'
assert meta['built_max_versions']==['2024'], 'Current distributed installer is 2024-only'
for rel in ['sdk/lib/x64/sinilab_native_sdk.lib','sdk/include/sinilab_licensing.hpp',
            'registry/lib/x64/sinilab_plugin_registry.lib','registry/include/plugin_registry.hpp',
            'registration/generic_registration.cpp','installer/installer_template.iss.in']:
    assert (root/rel).is_file(),rel
for f in root.rglob('*'):
    if f.is_file() and f.name in ('plugin_registry.cpp','sinilab_native_sdk.cpp'):
        raise RuntimeError('Private implementation source included: '+str(f))
identity=SourceFileLoader('identity',str(root/'registration/generate_identity.py')).load_module()
identity.generate(meta)
installer=SourceFileLoader('installer',str(root/'installer/generate_installer.py')).load_module()
iss=installer.generate(meta,(root/'installer/installer_template.iss.in').read_text(encoding='utf-8'))
assert meta['product_code'] in iss
print('CONSUMER PREFLIGHT PASSED (2024 template; Windows compilation not performed)')
