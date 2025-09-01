
from flask import Flask
from config import Config
from app import create_app

if __name__=="__main__":
    app = create_app(config_class=Config)
    app.run(host='localhost', port=8888, debug=True)
