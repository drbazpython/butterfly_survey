# Use this file to run locally
from app import app
if __name__ == '__main__':
    app.run_server(debug=True, port=5500)