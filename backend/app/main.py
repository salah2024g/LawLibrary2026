import os
import sys

BACKEND_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "")
if BACKEND_ROOT not in sys.path:
    sys.path.insert(0, BACKEND_ROOT)

from app.factory.application import create_application  # noqa: E402

app = create_application()
