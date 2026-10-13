"""Validate the iOS 16+ RootHide deployment and package metadata."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
makefile = (root / "Makefile").read_text()
prefs_makefile = (root / "Preferences/Makefile").read_text()
control = (root / "control").read_text()
workflow = (root / ".github/workflows/build.yml").read_text()
info = (root / "Preferences/Resources/Info.plist").read_text()

assert "iphone:clang:latest:16.0" in makefile
assert "iphone:clang:latest:16.0" in prefs_makefile
assert "firmware (>= 16.0)" in control
assert "firmware (<< 16.0)" not in control
assert "Version: 0.7.50-roothide" in control
assert "<string>0.7.50</string>" in info
assert "iPhoneOS16.5.sdk" in workflow
assert "iPhoneOS15.6.sdk" not in workflow
print("Verified iOS 16+ deployment target, dependencies, SDK and synchronized version")
