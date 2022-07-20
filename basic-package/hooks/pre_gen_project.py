"""Hook is run before cookiecutter starts."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{cookiecutter.__pkg_import_name}}"


if not re.match(MODULE_REGEX, module_name):
    print(
        f"ERROR: The python module name '{module_name}' is not a valid "
        "Python module name. Please do not use a - and use _ instead"
    )

    # Exit to cancel project
    sys.exit(1)
