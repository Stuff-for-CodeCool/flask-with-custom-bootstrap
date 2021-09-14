from flask import Flask, render_template
from os.path import join

app = Flask(__name__)


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.jinja_env.strip_trailing_newlines = True


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
