from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    # if username=="rudra123" and password=="123":
    #     return render_template("welcome.html")

    valid_users={
        'admin':'123',
        'sagar123':'pass',
        'rajat':'raj'
    }
    if username in valid_users and password==valid_users[username]:
        return render_template("welcome.html")
    else:
        return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)