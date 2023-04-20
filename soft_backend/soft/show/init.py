from flask import Blueprint

show_blue = Blueprint('show', __name__, url_prefix='/show')
from . import show_data