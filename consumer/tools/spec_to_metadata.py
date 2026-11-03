#!/usr/bin/env python3
"""Strict Sinilab.ai Integration Specification -> build metadata adapter.
The Integration Specification is authoritative for identity; build facts come from compiled outputs.
"""
import argparse, json, re
from pathlib import Path

FIELDS = {
    "collaborator": ("Collaborator",),
    "product": ("Product",),
    "product_code": ("Product Code", "SKU"),
    "target_application": ("Target Application",),
    "integration_type": ("Integration Type",),
    "variation": ("Variation",),
    "category": ("Category",),
}
SKU = re.compile(r"[A-Za-z0-9_-]{1,96}\Z")
FILE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\Z")
YEAR = re.compile(r"20[0-9]{2}\Z")

def parse_spec(text):
    found = {}
    # Explicit markdown field lines only. Never infer missing identity from filename or prose.
    for line in text.splitlines():
        match = re.match(r"^\s*(?:[-*]\s*)?(?:\*\*)?([A-Za-z][A-Za-z ]+?)(?:\*\*)?\s*:\s*(.*?)\s*$", line)
        if not match:
            continue
        label, value = match.group(1).strip().lower(), match.group(2).strip()
        if label in ("product code", "sku"):
            # Live website format: `sku` (authoritative WooCommerce SKU).
            # Do not silently accept arbitrary trailing text or multiple codes.
            quoted = re.fullmatch(r"`([^`]+)`(?:\s*\(authoritative WooCommerce SKU\))?", value)
            if quoted:
                value = quoted.group(1)
            elif "`" in value or "(" in value or ")" in value:
                raise ValueError("Invalid Product Code annotation")
        else:
            value = value.strip("`").strip()
        for key, aliases in FIELDS.items():
            if label in [a.lower() for a in aliases]:
                if not value or value.lower() in {"n/a", "none", "tbd"}:
                    raise ValueError(f"Empty or placeholder field: {key}")
                if key in found and found[key] != value:
                    raise ValueError(f"Conflicting {key} values")
                found[key] = value
    required = ("collaborator", "product", "product_code", "target_application", "integration_type")
    missing = [k for k in required if k not in found]
    if missing:
        raise ValueError("Missing Integration Specification fields: " + ", ".join(missing))
    if not SKU.fullmatch(found["product_code"]):
        raise ValueError("Invalid Product Code; do not alter the authoritative SKU")
    if found["target_application"] != "3ds Max":
        raise ValueError("Only 3ds Max supported in this candidate")
    if found["integration_type"] != "Host + Sinilab.ai Licensing":
        raise ValueError("Requires Host + Sinilab.ai Licensing")
    return found

def assemble(spec, build):
    required = ("product_version", "binary_filename", "helper_filename", "readme_filename", "built_max_versions")
    for key in required:
        if key not in build:
            raise ValueError(f"Missing build evidence: {key}")
    for key in ("binary_filename", "helper_filename", "readme_filename"):
        if not isinstance(build[key], str) or not FILE.fullmatch(build[key]):
            raise ValueError(f"Unsafe filename: {key}")
    years = build["built_max_versions"]
    if not isinstance(years, list) or not years or len(years) != len(set(years)) or any(not isinstance(y,str) or not YEAR.fullmatch(y) for y in years):
        raise ValueError("Invalid built_max_versions")
    if years != ["2024"]:
        raise ValueError("Stage 13.1 candidate supports validated 2024 only")
    if not isinstance(build["product_version"],str) or not build["product_version"].strip():
        raise ValueError("Missing product version")
    forbidden = set(FIELDS) | {"registration_product_code", "max_version"}
    if forbidden.intersection(build):
        raise ValueError("Build evidence must not override Integration Specification identity")
    return {**spec, **build, "registration_product_code": spec["product_code"], "max_version": years[0]}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--spec", required=True)
    p.add_argument("--build-evidence", required=True)
    p.add_argument("--output", required=True)
    args=p.parse_args()
    spec=parse_spec(Path(args.spec).read_text(encoding="utf-8"))
    build=json.loads(Path(args.build_evidence).read_text(encoding="utf-8"))
    result=assemble(spec,build)
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
if __name__=="__main__":
    main()
