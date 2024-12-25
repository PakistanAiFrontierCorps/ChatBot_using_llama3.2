from flask import Flask, request, render_template, jsonify
from crew import crew_workflow

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    question = None

    if request.method == 'POST':
        question = request.form.get('query')
        
        if question:
            workflow_result = crew_workflow(question)

            if "error" in workflow_result:
                error = workflow_result["error"]
            else:
                response = workflow_result["response"]
                result = response.get("result", "No answer provided.")
        else:
            error = "Please provide a question."

    return render_template('index.html', question=question, result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)