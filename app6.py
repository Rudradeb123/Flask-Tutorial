from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def profile():
    return render_template(
        "student_profile.html",
        name="Rudra",
        is_topper=True,
        subjects=["Maths", "Science", "History"]
    )

if __name__ == "__main__":
    app.run(debug=True)
