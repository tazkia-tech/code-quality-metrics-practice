# Jalankan app dari direktori project root:
# python3 after_app/run.py
import os
import sys

# pastikan folder after_app di sys.path agar "import app" menemukan package yang benar
this_dir = os.path.dirname(os.path.abspath(__file__))  # .../after_app
if this_dir not in sys.path:
    sys.path.insert(0, this_dir)

from app import create_app

app = create_app()

if __name__ == '__main__':
    # debug True cocok untuk development; matikan saat production
    app.run(host='127.0.0.1', port=5000, debug=True)
