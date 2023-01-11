from flask import Flask, render_template, request


def creat_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    @app.route('/', methods=['GET', 'POST'])
    def index():
        error = None
        count = None
        if request.method == 'POST':
            text = request.form['text']
            if not text:
                error = "Please enter some text."
            else:
                count = len(text.split())

        return render_template('index.html', error=error, count=count)

    return app


app = creat_app()
