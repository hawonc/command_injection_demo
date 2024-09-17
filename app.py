from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/echo', methods=['POST'])
def ping():
    user_input = request.form.get('link')
    if user_input:
        # Execute the command directly with os.system
        command = f"echo {user_input}"
        result = os.popen(command).read()
        return render_template('index.html', result=result)
    return render_template('index.html', result='No input provided.')

if __name__ == '__main__':
    app.run(debug=True)