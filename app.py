from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/word_count', methods=['POST'])
def word_count():
    text = request.form.get("user_text")
    message = "Thanks for the feedback!"
    qtd_palavras = len(text)
    data = {
        "message": message,
        "word_count": qtd_palavras
    }

    if len(text) == 0:
        message = 'Text input is required'
        return render_template("feedback_fail_response.html", message=message)

    return render_template("feedback_response.html", data=data)
