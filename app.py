from flask import Flask, render_template, request
from llama2 import get_llama2_response
from falcon import get_falcon_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_query', methods=['POST'])
def submit_query():
    query = request.form['query']
    # Here you would normally process the query and get responses from the LLMs
    llama2_response = get_llama2_response(query)
    falcon_response = get_falcon_response(query)
    llm3_response = "Placeholder for LLM 3 response"
    llm4_response = "Placeholder for LLM 4 response"

    return render_template('index.html', query=query, llama2_response=llama2_response, falcon_response=falcon_response, llm3_response=llm3_response, llm4_response=llm4_response)

if __name__ == '__main__':
    app.run(debug=True)
