from flask import Flask, render_template

from database import initialize_database


app = Flask(
    __name__,
    template_folder="../Template"
)


@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    initialize_database()

    app.run(debug=True)