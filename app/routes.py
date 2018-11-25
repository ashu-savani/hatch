from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.login_form import LoginForm
from app.login_form import RegistrationForm, SellingForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, SoldItems, BoughtItems

@app.route('/', methods=["GET"])
@app.route("/index", methods=["GET"])
@login_required
def index():
    return render_template("index.html", title="Home Page")


@app.route('/sell', methods=["GET", "POST"])
@login_required
def sell():
    form = SellingForm()
    if form.validate_on_submit():
        id = current_user.get_id()
        sold_items = SoldItems(user_id=id, item=form.produce.data, quantity=form.quantity.data, date=form.date.data, location=form.location.data)
        db.session.add(sold_items)
        db.session.commit()
        flash("You have successfully added an item!")
        return redirect(url_for("index"))
    return render_template("sell.html", title="Buy", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, phone_number=form.phone_number.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)  

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))