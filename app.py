from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/flights")
def flights():
    return render_template("flights.html")

@app.route("/aircraft")
def aircraft():
    return render_template("aircraft.html")

@app.route("/crew")
def crew():
    return render_template("crew.html")

@app.route("/passengers")
def passengers():
    return render_template("passengers.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)