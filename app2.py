from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Sample data storage (you can replace this with a database)
data = None

def process_data(data):
    if data is not None:
        try:
            # Create a DataFrame from the imported data
            df = pd.DataFrame(data)

            # Clean the data (e.g., handle missing values)
            df = df.dropna()

            # Process the data (e.g., calculate new variables)
            df['new_variable'] = df['column1'] * df['column2']

            # You can perform additional data processing here

            # Return the processed data as a list of dictionaries
            processed_data = df.to_dict(orient='records')
            return processed_data
        except Exception as e:
            return {'error': str(e)}
    else:
        return {'error': 'No data to process.'}

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
def process_data_route():
    global data
    processed_data = process_data(data)
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
