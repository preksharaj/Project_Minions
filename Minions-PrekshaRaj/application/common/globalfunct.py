import random
import string
import json
import re
from flask import jsonify


# random id generator
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def json_encode(json_dict=None):
    assert isinstance(json_dict, dict)
    return json.dumps(json_dict)


def json_encode_flask(json_dict=None):
    assert isinstance(json_dict, dict)
    return jsonify(json_dict)


def json_decode(json_str=None):
    assert isinstance(json_str, str)
    return json.loads(json_str)
