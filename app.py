from flask import Flask, request, jsonify, render_template, session
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name, template_folder="templates")
app.config['UPLOAD_FOLDER'] = 'uploads'  # Define the UPLOAD_FOLDER here

# Initialize data as an empty DataFrame
data = pd.DataFrame()

# Sample data storage (you can replace this with a database)
data = None

def process_data(data):
    if not data.empty:
        try:
            # Clean the data (e.g., handle missing values)
            data = data.dropna()

            # Process the data (e.g., calculate new variables)
            data['new_variable'] = data['column1'] * data['column2']

            # You can perform additional data processing here

            # Return the processed data as a list of dictionaries
            processed_data = data.to_dict(orient='records')
            return processed_data
        except Exception as e:
            return {'error': str(e)}
    else:
        return {'error': 'No data to process.'}

# Data analysis function
def analyze_data(data):
    if not data.empty:
        # Perform data analysis (you can customize this based on your data)
        # For example, clustering using K-Means
        X = data[['feature1', 'feature2']]  # Select the features for analysis
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        kmeans = KMeans(n_clusters=3)
        data['cluster'] = kmeans.fit_predict(X_scaled)

        # Data Visualization
        # Example: Create a bar chart
        bar_data = data.groupby('cluster')['feature1'].count()
        bar_data.plot(kind='bar')
        plt.title('Data Analysis Results')
        plt.xlabel('Cluster')
        plt.ylabel('Count')
        plt.savefig('analysis_result.png')  # Save the plot as an image

# Flask routes
@app.route('/')
def hello():
    return render_template('index.html')

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
            session['data'] = data  # Store data in the session for future use
            return jsonify({'message': 'Data imported successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

@app.route('/process-data', methods=['GET'])
def process_data_route():
    data = session.get('data', None)  # Retrieve data from the session
    processed_data = process_data(data)
    return jsonify(processed_data)

@app.route('/analyze-data', methods=['GET'])
def analyze_data_route():
    data = session.get('data', None)  # Retrieve data from the session
    analyze_data(data)  # Call the data analysis function
    return jsonify({'message': 'Data analysis and visualization complete'})

if __name__ == '__main':
    app.run(debug=True)
