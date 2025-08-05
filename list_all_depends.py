#!/usr/bin/env python3

import os
import ast

def find_all_depends(project_path):
    depends_set = set()
    for module_name in os.listdir(project_path):
        module_path = os.path.join(project_path, module_name)
        if not os.path.isdir(module_path):
            continue
        manifest_path = os.path.join(module_path, '__manifest__.py')
        if not os.path.exists(manifest_path):
            continue
        with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
            manifest_data = manifest_file.read()
        try:
            manifest_dict = ast.literal_eval(manifest_data)
            depends_list = manifest_dict.get('depends', [])
            depends_set.update(depends_list)
        except Exception as e:
            print(f"Fel vid läsning av {manifest_path}: {e}")
    return sorted(depends_set)

# Exempel på användning:
project_path = '/usr/share/odoo-industry'  # Ändra till din projektmapp
all_depends = find_all_depends(project_path)
print("Unika depends-moduler i hela projektet:")
print("\n".join(all_depends))

