from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/betterparts')
def dashboard():
    return render_template('dash.html')

@app.route('/software')
def software():
    return render_template('systems.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)