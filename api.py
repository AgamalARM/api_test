# import requests
# import json

# res = requests.get(
#     "https: // api.stackexchange.com/2.3/questions?order=desc & sort=activity & site=stackoverflow")
# print(res)


from flask import *
import json
import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'page': 'Home',
                'message': 'Success loaded Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    # 127.0.0.1:port/user/?user=USER_NAME
    user_query = str(request.args.get('user'))
    data_set = {'page': 'Request',
                'message': f'Success got the request for{user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


# if __name__ == '__main__':
#     app.run(port=7777)

home_page()
