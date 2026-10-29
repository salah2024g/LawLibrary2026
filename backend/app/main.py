import os
import sys

# Ensure CI resolves modules rooted at backend/ the same way as local execution.
BACKEND_ROOT = os.path.join(os.getcwd(), "backend")
if BACKEND_ROOT not in sys.path:
    sys.path.insert(0, BACKEND_ROOT)

from backend.app.factory.application import create_application  # noqa: E402

app = create_application()
