#!/usr/bin/env python3
"""Generate compile-time product identity from AI-extracted Integration Specification metadata.
The JSON is an internal build intermediate, NOT a collaborator-facing configuration form.
"""
import argparse
import json
import re
from pathlib import Path

SKU = re.compile(r"[A-Za-z0-9_-]{1,96}\Z", re.ASCII)
YEAR = re.compile(r"20[0-9]{2}\Z", re.ASCII)

def cpp_literal(s):
    return json.dumps(s, ensure_ascii=True)

def generate(m):
    for field in ("collaborator", "product", "product_code", "product_version"):
        if not isinstance(m.get(field), str) or not m[field].strip():
            raise ValueError(f"Missing {field}")
    if not SKU.fullmatch(m["product_code"]):
        raise ValueError("Product Code must match registry-supported SKU: letters, digits, _ or -, max 96 characters; no normalisation")
    if m.get("target_application") != "3ds Max":
        raise ValueError("Target application must be 3ds Max")
    if m.get("integration_type") != "Host + Sinilab.ai Licensing":
        raise ValueError("Requires Host + Sinilab.ai Licensing")
    years = m.get("built_max_versions")
    if not isinstance(years, list) or not years or len(years) != len(set(years)) or any(not isinstance(y, str) or not YEAR.fullmatch(y) for y in years):
        raise ValueError("built_max_versions must be a unique nonempty list of verified build years")
    lines = ["// GENERATED FILE — DO NOT EDIT", "#pragma once", "namespace sinilab_product {"]
    for key, name in (("product_code", "product_code"), ("collaborator", "collaborator"), ("product", "product"), ("product_version", "version")):
        lines.append(f"inline constexpr const char* {name} = {cpp_literal(m[key])};")
    lines.append("inline constexpr const char* built_max_versions[] = {" + ", ".join(map(cpp_literal, years)) + "};")
    lines.append("} // namespace sinilab_product")
    return "\n".join(lines) + "\n"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--metadata", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    Path(args.output).write_text(generate(json.loads(Path(args.metadata).read_text(encoding="utf-8"))), encoding="utf-8")

if __name__ == "__main__":
    main()
