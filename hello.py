from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return render_template('index.html', new = arr)

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template('login.html')
