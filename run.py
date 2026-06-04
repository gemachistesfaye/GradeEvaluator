import os
from app import app

# Ensure the working directory is the project root for relative imports
if __name__ == "__main__":
    # Use the Flask development server; set DEBUG based on environment variable
    debug_mode = os.getenv("FLASK_DEBUG", "1") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug_mode)
