from flask import Flask, render_template, request, jsonify
from prediction_service.prediction import form_response, api_response
import os
import json

params_path = 'params.yaml'
webapp_root = 'webapp'

static_dir_path = os.path.join(webapp_root, 'static')
template_dir_path = os.path.join(webapp_root, 'templates')

input_csv_folder = os.path.join(static_dir_path, 'input_csv')

app = Flask(__name__, static_folder = static_dir_path, template_folder = template_dir_path)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                response = form_response(dict_req)
                return render_template("index.html", response= response)
            elif request.json:
                response = api_response(request.json)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": e}
            return render_template("404.html", error = error)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 1234, debug = True)

