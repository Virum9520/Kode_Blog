from flask import Flask, render_template, url_for, flash, redirect
# from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

SECRET_KEY = 'baeef982bfca2daa43'
app = Flask(__name__)


app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

db = SQLAlchemy(app)


# Database models as classes

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!',
              'success')
        return redirect(url_for('home'))
    return render_template("register.html",
                           title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'kode_blog@admin.com' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for("home"))
        else:
            flash('Login Unsuccessful, Please check Email/Password',
                  'danger')
    return render_template("login.html",
                           title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        # db.create_all()
        # user1 = User(username='Virum',
        #              email='virumranka@gmail.com',
        #              password='password')
        # user2 = User(username='admin',
        #              email='admin@gmail.com',
        #              password='password')
        # db.session.add(user1)
        # db.session.add(user2)
        # db.session.commit()
        post1 = Post(title="Elon loves SpaceX",
                     content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at augue vehicula, malesuada ipsum ut, laoreet est. Suspendisse potenti. Integer tincidunt lorem at lobortis aliquet. Nunc non lacus vitae eros auctor posuere. Morbi iaculis ipsum quis arcu elementum pellentesque. Sed",
                     user_id=1)
        post2 = Post(title="Google has your attention",
                     content="Vestibulum non nisi fringilla mauris mattis dapibus eu ac nunc. Quisque vitae cursus lacus, in suscipit sapien. Sed ac auctor elit, sit amet pulvinar nisl. Suspendisse in diam egestas nisi iaculis suscipit non vel nibh. Vestibulum eros lorem, mattis in.",
                     user_id=2
                     )
        db.session.add(post1)
        db.session.add(post2)
        db.session.commit()
        # db.drop_all()
        # db.create_all()
        # User.query.all()


