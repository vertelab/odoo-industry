#!/usr/bin/env python3
import sys
import pprint
import os

all_depends = []
addons_path = "/usr/share/core-odoo/addons"

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} path/to/__manifest__.py")
    sys.exit(1)

manifest_files = sys.argv[1:]


for manifest_file in manifest_files:
    with open(manifest_file, "r", encoding="utf-8") as f:
        code = f.read()

    manifest_dict = eval(code, {"__builtins__": None}, {})

    depends = manifest_dict.get('depends', [])
    all_depends.extend(depends)


depends = list(set(all_depends))
depends.sort()
#pprint.pprint(depends)

addons_path = "/usr/share/core-odoo/addons"
ce_modules = [name for name in os.listdir(addons_path)
                     if os.path.isdir(os.path.join(addons_path, name))]

ee_modules = [name for name in all_depends if name not in ce_modules]
ee_modules = list(set(ee_modules))
ee_modules.sort()
pprint.pprint(ee_modules)
