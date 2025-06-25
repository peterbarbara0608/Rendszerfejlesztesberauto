#from flask import Blueprint
from apiflask import APIBlueprint


bp = APIBlueprint('administrator', __name__, tag="administrator")

from app.blueprints.administrator import routes


