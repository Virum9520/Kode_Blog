from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Virum Ranka',
        'title': 'Data Science',
        'content': 'Machine learning and Deep learning',
        'date': 'May 6, 2022'
    },
    {
        'author': 'Elon Musk',
        'title': 'SpaceX',
        'content': 'Aeronautics and Space R&D',
        'date': 'May 5, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == '__main__':
    app.run(debug=True)
