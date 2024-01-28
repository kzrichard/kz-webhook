from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'


@app.route('/confluence', methods=['POST'])
def confluence():
    data = request.get_json()
    print('data', data)
    return data, 200


# update_page_data = {
#     "page": {
#         "idAsString": "13139970",
#         "creatorAccountId": "5e28d102cc34b10ca3dbf2b0",
#         "spaceKey": "IT",
#         "spaceId": 65634,
#         "modificationDate": 1706398859667,
#         "lastModifierAccountId": "5e28d102cc34b10ca3dbf2b0",
#         "self": "https://kzkitchen.atlassian.net/wiki/spaces/IT/pages/13139970/Test+Page",
#         "id": 13139970,
#         "title": "Test Page",
#         "creationDate": 1706398513664,
#         "contentType": "page",
#         "version": 2
#     },
#     "accountType": "customer",
#     "timestamp": 1706398859681,
#     "userAccountId": "5e28d102cc34b10ca3dbf2b0",
#     "updateTrigger": "edit_page"
# }

# create_page_data = {
#     "page": {
#         "idAsString": "13139970",
#         "creatorAccountId": "5e28d102cc34b10ca3dbf2b0",
#         "spaceKey": "IT",
#         "spaceId": 65634,
#         "modificationDate": 1706398522457,
#         "lastModifierAccountId": "5e28d102cc34b10ca3dbf2b0",
#         "self": "https://kzkitchen.atlassian.net/wiki/spaces/IT/pages/13139970/Test+Page",
#         "id": 13139970,
#         "title": "Test Page",
#         "creationDate": 1706398513664,
#         "contentType": "page",
#         "version": 1
#     },
#     "timestamp": 1706398522460,
#     "accountType": "customer",
#     "userAccountId": "5e28d102cc34b10ca3dbf2b0"
# }
