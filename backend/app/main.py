"""
Backend application entry point.
Run the FastAPI package through ``backend.app.main``.
"""

import os
import sys


# Ensure package imports resolve consistently when invoked from the repository root
# (for example: ``mypy backend``) and from inside the backend package.
_backend_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _backend_root not in sys.path:
    sys.path.insert(0, _backend_root)

from backend.app.factory.application import create_application  # noqa: E402

app = create_application()
