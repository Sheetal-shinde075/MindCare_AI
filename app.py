from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "mindcare_secret_key"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/language")
def language():
    return render_template("language.html")


@app.route("/set-language/<lang>")
def set_language(lang):

    allowed_languages = ["english", "hindi", "marathi", "telugu", "urdu"]

    if lang in allowed_languages:
        session["language"] = lang

    return render_template("dashboard.html", language=lang)


@app.route("/dashboard")
def dashboard():

    language = session.get("language", "english")

    return render_template("dashboard.html", language=language)


@app.route("/memory")
def memory():

    language = session.get("language", "english")

    return render_template("memory.html", language=language)

@app.route("/pattern")
def pattern():

    language = session.get("language", "english")

    return render_template("pattern.html", language=language)

@app.route("/sequence")
def sequence():

    language = session.get("language", "english")

    return render_template("sequence.html", language=language)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)