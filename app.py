from flask import Flask, render_template, request, jsonify, send_file, Response
from simulation_engine import analyze_idea
import io

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('front.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        idea = request.form.get('idea', '')
        if not idea:
             return render_template('front.html') # Redirect back if empty
             
        # Run the deterministic simulation
        simulation_data = analyze_idea(idea)
        
        # Render the dynamic template with the data
        return render_template('result_dynamic.html', **simulation_data)
        
    # If accessed via GET (e.g. reload), send back to home or show sample
    return render_template('front.html') # Or redirect('/')

@app.route('/download_report', methods=['POST'])
def download_report():
    report_content = request.form.get('report_content', 'No report data found.')
    
    return Response(
        report_content,
        mimetype="text/plain",
        headers={"Content-disposition": "attachment; filename=simulation_report.txt"}
    )

# Keep the API endpoint just in case, though not used by front.html anymore
@app.route('/api/simulate', methods=['POST'])
def simulate():
    data = request.json
    idea = data.get('idea', '')
    if not idea:
        return jsonify({"error": "No idea provided"}), 400
    analysis_result = analyze_idea(idea)
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
