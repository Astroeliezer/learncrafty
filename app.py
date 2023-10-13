from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Sample data storage (you can replace this with a database)
data = None

@app.route('/import-data', methods=['POST'])
def import_data():
    global data
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        try:
            data = pd.read_csv(file)
            return jsonify({'message': 'Data imported successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@app.route('/process-data', methods=['GET'])
def process_data():
    global data
    if data is None:
        return jsonify({'error': 'No data imported yet'}), 400

    # Add data processing code here

    return jsonify({'message': 'Data processed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
