# import requests
# import json

# res = requests.get(
#     "https: // api.stackexchange.com/2.3/questions?order=desc & sort=activity & site=stackoverflow")
# print(res)


from flask import *
import json
import time

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home_page():
    data_set = {'page': 'Home',
                'message': 'Success loaded Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


