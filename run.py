from flask import Flask, request
from utils import prepare_image, get_predict


app = Flask(__name__)


@app.route("/", methods=["GET"])
def test():
    return {"Status": "Ok"}


@app.route("/get_prob", methods=["POST"])
def get_prob():
    image = request.files["image"]
    image = prepare_image(image)
    result = get_predict(image)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
