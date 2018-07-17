from flask import abort, Blueprint, jsonify, redirect, request, send_from_directory

from services import fhir_search


BP = Blueprint("main", __name__)


@BP.route("/")
def index():
    return redirect("/index.html")


@BP.route("/q")
def search():
    term = request.args.get("term")
    if not term:
        return jsonify(list())
    return jsonify(fhir_search.search(term))


@BP.route("/<path:path>")
def static(path):
    return send_from_directory("static", path)
