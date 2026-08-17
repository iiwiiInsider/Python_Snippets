# Create a server with flask to show hello world
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
