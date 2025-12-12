from flask import Flask, render_template, request, jsonify, send_file, Response
from simulation_engine import analyze_idea
import io

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('finder.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        try:
            idea = request.form.get('idea', '')
            industry = request.form.get('industry', '')
            
            if not idea:
                 return render_template('finder.html') # Redirect back if empty
                 
            # Run the deterministic simulation with industry context
            simulation_data = analyze_idea(idea, industry)
            
            # Render the dynamic template with the data
            # Fix: Pass original_idea explicitly so the template can render it
            return render_template('result_v2.html', original_idea=idea, **simulation_data)
        except Exception as e:
            import traceback
            traceback.print_exc() # This will print to the server logs (Render console)
            return f"<h2>Simulation Failed</h2><p>Error: {str(e)}</p><pre>{traceback.format_exc()}</pre>", 500
        
    # If accessed via GET (e.g. reload), send back to home
    return render_template('finder.html')

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
