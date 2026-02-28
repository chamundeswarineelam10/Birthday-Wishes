from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CORRECT_DAY = 2
CORRECT_MONTH = 3
CORRECT_YEAR = 2004

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        try:
            day = int(request.form["day"])
            month = int(request.form["month"])
            year = int(request.form["year"])

            if day == CORRECT_DAY and month == CORRECT_MONTH and year == CORRECT_YEAR:
                return redirect(url_for("surprise"))
            else:
                error = "Wrong Date 😜 Try Again My Love 💕"
        except:
            error = "Please enter valid numbers 🥺"

    return render_template("index.html", error=error)

@app.route("/surprise")
def surprise():
    return render_template("surprise.html")

if __name__ == "__main__":
    app.run(debug=True)