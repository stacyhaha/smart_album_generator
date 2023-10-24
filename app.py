import os
import logging
from datetime import datetime
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from album.album import Album
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

app = Flask(__name__)
CORS(app)

#config
basic_path = os.path.abspath(os.path.dirname(__file__))
workspace = os.path.join(os.path.dirname(basic_path), "workspace")
weights_path = os.path.join(basic_path, "models/places365-master/resnet50_places365.pth.tar")
categories_file = os.path.join(basic_path, "models/places365-master/categories_places365.txt")
template_dir= os.path.join(basic_path, "templates")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'heic'} 


album = Album(
    workspace = workspace,
    weights_path = weights_path,
    categories_file = categories_file,
    template_dir= template_dir
)

@app.route("/album", methods=["POST"])
def make_album():
    logger.info("get a request")
    #input_arg = request.json
    logger.info(str(request.json))
    #logger.info(str(input_arg))
    #album_path = album.predict(**input_arg)
    album_path=""
    logger.info("finish")
    return jsonify({"album_path": album_path})

@app.route("/", methods=["GET"])
def a():
    return "Hello"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    path = os.path.join(workspace, datetime.now().strftime("%Y.%m.%d_%H.%M.%S"), "images")
    if not os.path.exists(path):
        os.makedirs(path)
    logger.info(f"pending to save images to {path}")
    uploaded_files = request.files.to_dict()
    
    for key, file in uploaded_files.items():
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(path, filename)
            file.save(filepath)
            logger.info(f"succeessfully save {filename} to filepath")
    return jsonify({"path": path})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    # $flask run