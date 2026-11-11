# Create a virtual environment
py -m venv .venv

# Install dependencies
pip install -r requirements.txt

# Start the dev server (http://127.0.0.1:8000)
py server.py runserver
# or from file server.py press "Run Python File"
