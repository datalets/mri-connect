""" Client App """

from flask import Blueprint, render_template, send_file, send_from_directory
from os import path
from . import Config

client_bp = Blueprint('client_app', __name__,
                      url_prefix='',
                      static_url_path='',
                      static_folder='./dist/static/',
                      template_folder='./dist/',
                      )

IMAGE_ROOT = path.join(Config.DIST_DIR, 'images')
UPLOADS_ROOT = Config.UPLOAD_DIR

@client_bp.route('/')
def index_client():
    return send_file(path.join(Config.DIST_DIR, 'index.html'))

@client_bp.route('/demo')
def index_demo():
    return send_file(path.join('..', 'public', 'demo.html'))

@client_bp.route('/favicon.ico')
def index_favicon():
    return send_file(path.join(IMAGE_ROOT, 'favicon.ico'))

@client_bp.route('/images/<path:imagepath>')
def index_images(imagepath):
    return send_from_directory(IMAGE_ROOT, imagepath)

@client_bp.route('/uploads/<path:filename>')
def index_uploads(filename):
    return send_from_directory(UPLOADS_ROOT, filename)
