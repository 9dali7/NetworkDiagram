from flask import Flask, jsonify, render_template
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    with open("data.yaml", "r") as file:
        data = yaml.safe_load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

