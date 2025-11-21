from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    labels = ['January', 'February', 'March', 'April', 'May', 'June']
    data = [0, 10, 15, 8, 22, 18, 25]

    return render_template('home.html', labels=labels, data=data)
if __name__ == '__main__':
    app.run()

