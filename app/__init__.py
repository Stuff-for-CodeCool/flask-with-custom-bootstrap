"""The server for this application"""

from flask import Flask, render_template
from .database import query

app = Flask(__name__)


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.jinja_env.strip_trailing_newlines = True


@app.route("/")
def index():
    """Main entry point, depends on a particular table existing"""

    clients = query("select * from clients")
    return render_template("index.html", clients=clients)
