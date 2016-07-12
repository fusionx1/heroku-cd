from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>ello World, I love continuous delivery a lot!</h1>"

if __name__ == "__main__":
    app.run()
