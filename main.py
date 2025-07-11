from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # show the form

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']  # get form input
    return render_template('result.html', name=name)  # pass it to result page

if __name__ == '__main__':
    app.run(debug=True)
