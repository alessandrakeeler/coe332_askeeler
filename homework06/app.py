from flask import Flask, request
import json
import logging
import redis

app = Flask(__name__)
meteor_data = {}


@app.route("/data", methods=["POST"])
def read_data_from_file():
    """
    This route confirms data has been successfully read.
    """
    rd = redis.Redis(host="172.17.0.12", port=6379)
    logging.info("Reading Data.")
    global meteor_data
    with open("ml_data.json", "r") as f:
        meteor_data = json.load(f)
    for d in meteor_data["meteorite_landings"]:
        rd.set(d["id"], json.dumps(d))
    return f"Data has been read from file\n"


@app.route("/data", methods=["GET"])
def get_all_names():
    """
    Loops through all names in the meteorite landing data.
    Returns:
    Names of meteors (list)
    """
    rd = redis.Redis(host="172.17.0.12", port=6379)
    logging.info("Obtaining all names...")
    list_data = []
    for i in range(10001, 10301, 1):
        list_data.append(json.loads(rd.get(i)))

    return json.dumps(list_data, indent=2) + "\n"
