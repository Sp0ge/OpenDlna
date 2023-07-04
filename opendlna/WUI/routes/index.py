from ..models import User
from ..extentions import db
from flask import flash, render_template, Blueprint, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_login import current_user, login_user, logout_user, login_required
from ..forms import User_Add, User_log

index_bp = Blueprint("index", __name__, url_prefix="/")

@index_bp.before_request
def before_request():
    db.create_all()
    if current_user.is_anonymous and \
    str(request.endpoint) == "index.setup" and \
    len(User.query.all()) != 0:
        return redirect(url_for("index.log"))

@index_bp.route("/")
@index_bp.route("/index", methods=['GET','POST'])
def main():
    
    if len(User.query.all()) == 0:
        return redirect(url_for("index.setup"))
    else:
        return render_template("index.html", user=current_user)







@index_bp.route("/setup", methods=['GET','POST'])
def setup():
    form = User_Add()
    if form.validate_on_submit():
        user = form.username.data
        password = form.password.data
        obj = User(username=str(user))
        obj.set_password(str(password))
        db.session.add(obj)
        db.session.commit()
        return redirect(url_for("index.main"))
    return render_template("setup.html", form=form, user=current_user)

@index_bp.route("/app/settings/reset", methods=['GET','POST'])
def reset_all():
    database = User.query.all()
    for obj in database:
        db.session.delete(obj)
    
    db.session.commit()
    return redirect(url_for("index.main"))

    
    
    
    
    
    
    
    
    
    
@index_bp.route("/auth/log", methods=['GET','POST'])
def log():
    if current_user.is_anonymous:
        form = User_log()
        if form.validate_on_submit():
            user = form.username.data
            password = form.password.data
            remember = form.remember_me.data
            obj = User.query.filter_by(username=user).first()
            if obj != None and obj.check_password(password) is True:
                print('login good')
                login_user(obj, remember)
                return redirect(url_for("index.main"))
            else:
                print('login error')
                flash("bad data")
            
        return render_template("log.html", form=form, user=current_user)
    else:
        return redirect(url_for("index.main"))
    
@index_bp.route("/auth/out", methods=['GET','POST'])
@login_required
def out():
    logout_user()
    return redirect(url_for('index.log'))
        