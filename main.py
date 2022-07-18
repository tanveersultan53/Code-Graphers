import os
from src.app import create_app


app_settings = os.environ.get('APP_SETTINGS')
app = create_app(app_settings)
host = os.environ.get("FLASK_HOST")
port = os.environ.get("FLASK_PORT")
if __name__ == '__main__':
    app.run(host=host,port=port,debug=True)
