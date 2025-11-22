from flask import Flask, render_template
import analysis

app = Flask(__name__)

@app.route("/")
def home():

    xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
    yValues = [55, 49, 44, 24, 15];
    barColors = ["red", "green","blue","orange","brown"];

    xValues, yValues = analysis.filter_by_time("year")
    return render_template('home.html', xValues=xValues, yValues=yValues, barColors=barColors)

if __name__ == '__main__':
    app.run(debug=True)

