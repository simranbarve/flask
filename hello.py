from flask import (Flask, render_template, url_for, request, redirect)
import time
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bubbleSort", methods =["GET", "POST"])
def bubbleSort():
    start = time.time()

    if request.method == "POST":

        req = request.form

        list = req["list"]

        list = (list.split(','))

        if req["which_way"] == 'ascending':

            n = len(list)
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if list[j] > list[j+1] :
                        list[j], list[j+1] = list[j+1], list[j]

        elif req["which_way"] == 'descending':

            n = len(list)
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if list[j] < list[j+1] :
                        list[j], list[j+1] = list[j+1], list[j]

        else:
            list = 'Enter a valid way to sort'

        end = time.time()
        time_taken = end - start

        return render_template("bubblesort.html", lst=list, time_taken = time_taken)
    else:
        return render_template("bubblesort.html")


@app.route("/mergeSort", methods =["GET", "POST"])
def merge():
    start = time.time()

    if request.method == "POST":

        req = request.form

        arr = req["list"]

        arr = (arr.split(','))

        def mergeSort(arr):
            if len(arr) >1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]

                mergeSort(L)
                mergeSort(R)

                i = j = k = 0

                if req["which_way"] == 'ascending':

                    while i < len(L) and j < len(R):
                        if L[i] < R[j]:
                            arr[k] = L[i]
                            i+= 1
                        else:
                            arr[k] = R[j]
                            j+= 1
                        k+= 1

                    while i < len(L):
                        arr[k] = L[i]
                        i+= 1
                        k+= 1

                    while j < len(R):
                        arr[k] = R[j]
                        j+= 1
                        k+= 1

                if req["which_way"] == 'descending':

                    while i < len(L) and j < len(R):
                        if L[i] > R[j]:
                            arr[k] = L[i]
                            i+= 1
                        else:
                            arr[k] = R[j]
                            j+= 1
                        k+= 1

                    while i < len(L):
                        arr[k] = L[i]
                        i+= 1
                        k+= 1

                    while j < len(R):
                        arr[k] = R[j]
                        j+= 1
                        k+= 1

        mergeSort(arr)
        end = time.time()
        time_taken = end - start


        return render_template("mergesort.html", lst = arr, time_taken = time_taken)
    else:
        return render_template("mergesort.html")

@app.route("/linearsearch", methods = ["GET", "POST"])
def linearsearch():
    start = time.time()
    if request.method == "POST":

        req = request.form

        list = req["list"]
        x = req["number"]

        list = (list.split(','))
        for i in range(len(list)):

            if list[i] == x:
                return_val = True
                break
            return_val = False

        end = time.time()
        time_taken = end - start

        return render_template("linearsearch.html", return_val = return_val, time_taken = time_taken)
    else:
        return render_template("linearsearch.html")

@app.route("/binarysearch", methods = ["GET", "POST"])
def binarysearch():
    if request.method == "POST":

        req = request.form

        arr = req["list"]
        x = req["number"]
        arr = (arr.split(','))
        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            # Check if x is present at mid
            if arr[mid] < x:
                low = mid + 1

            # If x is greater, ignore left half
            elif arr[mid] > x:
                high = mid - 1

            # If x is smaller, ignore right half
            else:
                return_val = True
                break
            break
        # If we reach here, then the element was not present
        return_val = False
        return render_template("binarysearch.html", return_val = return_val)
    else:
        return render_template("binarysearch.html")
