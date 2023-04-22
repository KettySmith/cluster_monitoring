from flask import Blueprint

upload_blue = Blueprint('upload', __name__, url_prefix='/upload')
from . import upload_data
