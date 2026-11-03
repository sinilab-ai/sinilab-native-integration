import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
from spec_to_metadata import parse_spec,assemble
class Test(unittest.TestCase):
 def setUp(self):
  self.s=Path(__file__).resolve().parents[1]/"metadata"/"integration-specification.md"
  self.b={"product_version":"1","binary_filename":"A.dlu","helper_filename":"B.exe","readme_filename":"README.txt","built_max_versions":["2024"]}
 def test_valid(self):
  m=assemble(parse_spec(self.s.read_text()),self.b)
  self.assertEqual(m["registration_product_code"],"collaborator_demo_native_test")
 def test_missing_sku(self):
  with self.assertRaises(ValueError):parse_spec(self.s.read_text().replace("Product Code:","Missing Code:"))
 def test_conflicting_sku(self):
  with self.assertRaises(ValueError):parse_spec(self.s.read_text()+"\n- Product Code: other_sku\n")
 def test_wrong_integration(self):
  with self.assertRaises(ValueError):parse_spec(self.s.read_text().replace("Host + Sinilab.ai Licensing","Host Only"))
 def test_build_override(self):
  with self.assertRaises(ValueError):assemble(parse_spec(self.s.read_text()),dict(self.b,product_code="wrong"))
 def test_unverified_version(self):
  with self.assertRaises(ValueError):assemble(parse_spec(self.s.read_text()),dict(self.b,built_max_versions=["2025"]))
if __name__=="__main__":unittest.main()

class LiveWebsiteCases(unittest.TestCase):
 def setUp(self):
  self.s=(Path(__file__).resolve().parents[1]/"metadata"/"integration-specification.md").read_text()
 def test_exact_live_sku(self):
  self.assertEqual(parse_spec(self.s)["product_code"],"collaborator_demo_native_test")
 def test_ambiguous_annotation_rejected(self):
  with self.assertRaises(ValueError):parse_spec(self.s.replace("(authoritative WooCommerce SKU)","(another SKU)"))
 def test_second_backtick_code_rejected(self):
  with self.assertRaises(ValueError):parse_spec(self.s.replace("(authoritative WooCommerce SKU)","`another`"))
