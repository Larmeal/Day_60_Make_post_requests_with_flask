from flask import Flask, render_template, request
import requests

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
content = response.json()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", contents=content)

@app.route("/About")
def about():
    return render_template("about.html")

@app.route("/Contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def post(id):
    port_number = content[id - 1]
    return render_template("post.html", articles=port_number)

@app.route("/form-entry", methods=["post"])
def receive_data():
    name = request.form["username"]
    email = request.form["email"]
    phone = request.form["number"]
    message = request.form["message"]
    return f"""
    <h1> Name: {name}
    Email: {email}
    Phone number: {phone}
    Message: {message} </h1>
    """

if __name__ == "__main__":
    app.run(debug=True)