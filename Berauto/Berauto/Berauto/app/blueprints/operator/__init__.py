#from flask import Blueprint
from apiflask import APIBlueprint

bp = APIBlueprint('ugyintezo', __name__, tag="ugyintezo")

from app.blueprints.ugyintezo import routes