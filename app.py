from flask import Flask, jsonify

app = Flask(__name__)

# Define an endpoint that returns arbitrary data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello, this is arbitrary data!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

