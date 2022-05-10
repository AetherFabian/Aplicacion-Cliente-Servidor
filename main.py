"""
@author: Fabian Escobar
@date:   2020-05-10
@description: Flask Exercise
"""
# Modules inclusion
from flask import Flask

app = Flask('__main__')

@app.route('/', methods=['GET'])
def go_home():
    return "Ola pa"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')