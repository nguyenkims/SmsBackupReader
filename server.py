import os
import xml.etree.ElementTree as etree
from datetime import datetime
import sys

from flask import Flask, jsonify


app = Flask(__name__)
sms_path = None


def read_sms(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()
    res = []
    for child in root:
        nb_milli_secs = int(child.attrib["date"])
        dt = datetime.fromtimestamp(nb_milli_secs / 1000)
        pretty_date = dt.isoformat(sep=" ")
        body = child.attrib["body"]
        num = child.attrib["address"]
        res.append({"date": pretty_date, "body": body, "num": num})

    return res


@app.route('/api/sms/list')
def sms_list():
    if sms_path is None:
        basedir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(basedir, "data", "small.xml")
    else:
        file_path = sms_path

    sms = read_sms(file_path)
    return jsonify({"data": sms})


if __name__ == '__main__':
    if len(sys.argv) == 2:
        sms_path = sys.argv[1]
        print("Sms_path=%s" % (sms_path,))

    app.run(debug=True)
