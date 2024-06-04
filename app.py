from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_query', methods=['POST'])
def submit_query():
    query = request.form['query']
    # Here you would normally process the query and get responses from the LLMs
    return render_template('index.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
