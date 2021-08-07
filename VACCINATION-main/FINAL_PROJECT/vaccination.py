from flask import Flask,redirect
from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import session
import authentication
import reminder
import logging
import json

app = Flask(__name__)

app.secret_key = b"s@g@d@c0ff33!"

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

navbar = """
        <a href="/">Home</a> | <a href="/aboutus">About Us</a> | <a href="/chatbot">Chat with Us!</a>
        <a href="/signup">Signup</a> | <a href="/login">Login</a>
        <p/>
        """
@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/auth",methods=["GET","POST"])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    is_successful, user=authentication.login(username, password)
    app.logger.info("%s",is_successful)
    if (is_successful):
        session["user"]=user
        return redirect("/")
    else:
        return redirect("/login")

@app.route("/")
def index():
    return render_template("home.html",page="Home")

@app.route ("/aboutus")
def aboutus():
    return render_template("aboutus.html",page="About Us")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/")

@app.route("/calendar")
def calendar():
    fd_days_left, sd_days_left = reminder.countdown(session["user"])
    source_url = "https://www.unicef.org/rosa/stories/what-do-during-and-after-getting-vaccinated-covid-19"
    return render_template("calendar.html",page="Calendar", fd_days_left=fd_days_left, sd_days_left=sd_days_left, source_url=source_url)

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html",page="Chat with Us!")

@app.route("/answer", methods=["GET","POST"])
def answer():
    question = request.form.get("question")
    if question == "1":
        return render_template("qna1.html",page="Chat with Us!")
    elif question == "2":
        return render_template("qna2.html",page="Chat with Us!")
    elif question == "3":
        return render_template("qna3.html",page="Chat with Us!")
    elif question == "4":
        return render_template("qna4.html",page="Chat with Us!")
    elif question == "5":
        return render_template("qna5.html",page="Chat with Us!")
    elif question == "6":
        return render_template("qna6.html",page="Chat with Us!")
    elif question == "7":
        return render_template("qna7.html",page="Chat with Us!")
    elif question == "8":
        return render_template("qna8.html",page="Chat with Us!")
    elif question == "9":
        return render_template("qna9.html",page="Chat with Us!")
    elif question == "10":
        return render_template("qna10.html",page="Chat with Us!")
    else:
        return render_template("chatbot.html",page="Chat with Us!")

@app.route("/account")
def account():
    return render_template("account.html",page="My Account")

@app.route("/signup")
def signup():
    return render_template("signup.html",page="Signup")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        fileObject = open("database.json","r")
        jsonContent = fileObject.read()
        aDict = json.loads(jsonContent)

        username = request.form.get("username")
        password = request.form.get("password")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        org = request.form.get("org")
        vaccine = request.form.get("vaccine")
        first_dose=request.form.get("first_dose")

        aDict[username]={"password":password, "first_name":first_name,"last_name":last_name,"org":org,"brand":vaccine,"first_dose":first_dose}
        jsonString = json.dumps(aDict)
        jsonFile = open("database.json","w")
        jsonFile.write(jsonString)
        jsonFile.close()
    return redirect("/")
