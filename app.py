import os
from flask import Flask, request, jsonify
from album.album import Album
app = Flask(__name__)


#config
basic_path = os.path.abspath(os.path.dirname(__file__))
workspace = os.path.join(os.path.dirname(basic_path), "workspace")
weights_path = os.path.join(basic_path, "models/places365-master/resnet50_places365.pth.tar")
categories_file = os.path.join(basic_path, "models/places365-master/categories_places365.txt")
template_dir= os.path.join(basic_path, "templates")

album = Album(
    workspace = workspace,
    weights_path = weights_path,
    categories_file = categories_file,
    template_dir= template_dir
)

@app.route("/album", methods=["POST"])
def make_album():
    input_arg = request.json
    print(type(input_arg))
    print(input_arg)
    album_path = album.predict(**input_arg)
    return jsonify({"album_path": album_path})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    # $flask run