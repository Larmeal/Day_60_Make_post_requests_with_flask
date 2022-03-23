from flask import Flask, render_template, request
import requests
import smtplib

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
content = response.json()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", contents=content)

@app.route("/About")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)

@app.route("/post/<int:id>")
def post(id):
    port_number = content[id - 1]
    return render_template("post.html", articles=port_number)



if __name__ == "__main__":
    app.run(debug=True)
