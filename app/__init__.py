from flask import Flask, render_template

app = Flask(__name__)


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.jinja_env.strip_trailing_newlines = True


@app.route("/")
def index():
    return render_template("index.html")