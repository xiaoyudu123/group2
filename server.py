from flask import Flask, jsonify

app = Flask(__name__)

# 模拟数据
data = [
    {"id": 1, "domain": "astronomy", "data": "Star data set"},
    {"id": 2, "domain": "biology", "data": "Genome sequence"},
    {"id": 3, "domain": "climate", "data": "Climate change data"}
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)