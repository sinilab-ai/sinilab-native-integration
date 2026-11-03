#!/usr/bin/env python3
"""Create a review-only Inno Setup script from Integration Specification-derived metadata."""
import argparse, json, re, uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def generate(data, template):
    required = ('collaborator','product','product_code','product_version','target_application','integration_type')
    for key in required:
        if not isinstance(data.get(key),str) or not data[key].strip():
            raise ValueError(f'Missing {key}')
    if data['target_application'] != '3ds Max' or data['integration_type'] != 'Host + Sinilab.ai Licensing':
        raise ValueError('Unsupported application/integration type')
    sku = data['product_code']
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,96}',sku):
        raise ValueError('Invalid canonical SKU')
    # Build metadata comes from the actual project; not from the Integration Specification.
    for key in ('binary_filename','helper_filename','readme_filename'):
        if not isinstance(data.get(key),str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,127}',data[key]):
            raise ValueError(f'Unsafe or missing build artefact filename: {key}')
    if data.get('max_version') != '2024':
        raise ValueError('Only validated 2024 template supported')
    if data.get('built_max_versions') != ['2024']:
        raise ValueError('Only built and verified 2024 version supported')
    if data.get('registration_product_code') != sku:
        raise ValueError('Registration helper SKU must match authoritative SKU')
    def quote(s):
        if any(c in s for c in ('"','\r','\n','{','}')): raise ValueError('Unsafe display value')
        return s
    values = {
        'CollaboratorName':quote(data['collaborator']),
        'ProductDisplayName':quote(data['product']),
        'ProductSubtitle':'2024',
        'AppName':quote(f"{data['collaborator']} - {data['product']} (2024)"),
        'AppVersion':quote(data['product_version']),
        'OutputBaseFilename':re.sub('[^A-Za-z0-9_-]','_',f"{sku}_2024_Setup"),
        'BinaryFilename':data['binary_filename'],
        'HelperFilename':data['helper_filename'],
        'ReadmeFilename':data['readme_filename'],
        'AppId':str(uuid.uuid5(uuid.NAMESPACE_URL,'https://sinilab.ai/native-installer/'+sku+'/3dsmax/2024')).upper(),
    }
    for k,v in values.items():
        template = template.replace('@'+k+'@',v)
    if re.search(r'@[A-Za-z]+@',template): raise ValueError('Unresolved template token')
    return template

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--metadata',required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    data=json.loads(Path(a.metadata).read_text(encoding='utf-8'))
    output=generate(data,(ROOT/'installer_template.iss.in').read_text(encoding='utf-8'))
    Path(a.output).write_text(output,encoding='utf-8')
if __name__=='__main__':main()
