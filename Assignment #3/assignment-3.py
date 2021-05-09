from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/terms-of-use', methods = ['GET'])
def termsOfUse():
    return render_template('terms-of-use.html')

@app.route('/privacy-policy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/dashboard', methods = ['GET'])
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug = True)