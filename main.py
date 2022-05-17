"""
@author: Fabian Escobar
@date:   2020-05-10
@description: Flask Exercise
"""
# Modules inclusion
from flask import Flask, request

app = Flask('__main__')
user = {
    "matricula":"112233",
    "first_name":"SOLOMIRO",
    "last_name":"PEGAMENTOSOS",
    "phone":"614-1112233"
}
# GET methods

#test method
@app.route('/', methods=['GET'])
def go_home():
    return "Ola pa"

#get users
@app.route('/users', methods=['GET'])
def get_users():
    return user

# POST methods

# save an user
@app.route('/users', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user

#save a device
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')