from flask import (Flask, render_template, url_for, request)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        lst = request.form["nums"]
        return redirect(url_for("list", list=lst))
    else:
        return render_template("login.html")

@app.route("/<lst>")
def user(list):
    n = len(list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return f"<h1>{list}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
