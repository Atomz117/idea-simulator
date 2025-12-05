
from flask import Flask, render_template, request, jsonify
from simulation_engine import analyze_idea
import time

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('front.html')

@app.route('/result')
def result():
    # In a real app, we might store the result in a session or DB using an ID.
    # For this prototype, we'll pass data via query params or just render a sample if accessed directly.
    return render_template('result.html')

@app.route('/api/simulate', methods=['POST'])
def simulate():
    data = request.json
    idea = data.get('idea', '')
    
    if not idea:
        return jsonify({"error": "No idea provided"}), 400
        
    # Simulate processing time for effect (optional, can be removed for speed)
    # time.sleep(2) 
    
    analysis_result = analyze_idea(idea)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
