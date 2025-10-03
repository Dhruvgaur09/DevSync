from flask import Flask

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Small Web Page!</h1><p>This is made using Python Flask 🚀</p>"

@app.route("/about")
def about():
    return "<h2>About Page</h2><p>This is a simple webpage created in Python.</p>"

if __name__ == "__main__":
    app.run(debug=True)
