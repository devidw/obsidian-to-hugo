import obsidian_to_hugo 
from datetime import datetime
import sys

def get_current_he_calver() -> str:
    """
    12023.01.01
    """
    date = datetime.now()
    return datetime.strftime(date.today(), "1%Y.%m.%d")

old_version = obsidian_to_hugo.__version__
new_version = get_current_he_calver()

if old_version == new_version:
  print("version already today")
  sys.exit(0)

for path in ["./src/obsidian_to_hugo/__init__.py", "./pyproject.toml"]:
  with open(path, "r") as f:
    filedata = f.read()
  filedata = filedata.replace(old_version, new_version)
  with open(path, "w") as f:
    f.write(filedata)
