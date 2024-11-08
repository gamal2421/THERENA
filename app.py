from main import main
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Python Backend!"

@app.route('/run_code', methods=['GET'])
def run_code():
    main()
    return jsonify({"message": "Running Python code..."})  
    

if __name__ == '__main__':
    app.run(debug=True)
