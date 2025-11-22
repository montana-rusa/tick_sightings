from flask import Flask, render_template, request, redirect
import analysis
import pandas as pd#
import os

app = Flask(__name__)

start = None
end = None
location = None
barColors = ["red", "green","blue","orange","brown"];

@app.route("/")
def home():

    barColors = ["red", "green","blue","orange","brown"];

    xValues, yValues = analysis.filter_by_time()
    xValues2, yValues2 = analysis.filter_by_location()

    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors, xValues2 = xValues2, yValues2 = yValues2)

@app.route("/submit1", methods =["GET", "POST"])
def submit1():

    if request.method == "GET":
        return redirect("/")

    start = pd.to_datetime(request.form['start'])
    end = pd.to_datetime(request.form['end'])

    xValues, yValues = analysis.filter_by_time(start, end)
    xValues2, yValues2 = analysis.filter_by_location(location)

    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors, xValues2 = xValues2, yValues2 = yValues2)


@app.route("/submit2", methods =["GET", "POST"])
def submit2():

    if request.method == "GET":
        return redirect("/")

    location = str(request.form['location'])

    if location == "All":
        location = None

    xValues, yValues = analysis.filter_by_time(start, end)
    xValues2, yValues2 = analysis.filter_by_location(location)

    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors, xValues2 = xValues2, yValues2 = yValues2)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)
    #app.run(debug=True)

