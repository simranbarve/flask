from flask import (Flask, render_template, url_for, request, redirect)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bubbleSort", methods =["GET", "POST"])
def bubbleSort():

    if request.method == "POST":

        req = request.form

        list = req["list"]

        list = (list.split(','))

        n = len(list)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if list[j] > list[j+1] :
                    list[j], list[j+1] = list[j+1], list[j]

        print(list)

        return redirect(request.url)
    return render_template("bubblesort.html")

@app.route("/mergeSort", methods =["GET", "POST"])
def mergeSort():

    if request.method == "POST":

        req = request.form

        list = req["list"]

        list = (list.split(','))

        def mergeSort(arr):
            if len(arr) >1:
                mid = len(arr)//2 # Finding the mid of the array
                L = arr[:mid] # Dividing the array elements
                R = arr[mid:] # into 2 halves

                mergeSort(L) # Sorting the first half
                mergeSort(R) # Sorting the second half

                i = j = k = 0

                # Copy data to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i+= 1
                    else:
                        arr[k] = R[j]
                        j+= 1
                    k+= 1

                # Checking if any element was left
                while i < len(L):
                    arr[k] = L[i]
                    i+= 1
                    k+= 1

                while j < len(R):
                    arr[k] = R[j]
                    j+= 1
                    k+= 1

        arr = list
        mergeSort(arr)
        for i in range(len(arr)):
            print(arr[i], end =" ")
        print()
        return redirect(request.url)
    return render_template("mergesort.html")
