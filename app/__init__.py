from flask import Flask, render_template


app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config.from_object('config')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
