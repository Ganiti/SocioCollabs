import os, logging 
from flask import Flask, render_template, request, jsonify,redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'razorpay'])
import razorpay
from flask import (
    render_template,
    request,
    url_for,
    redirect,
    send_from_directory,
    flash,
    make_response,
)
from sqlalchemy import func

from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2 import TemplateNotFound

from app import app, lm, db, bc
from app.models import Users, Fundraisers,New_donations
from app.forms import LoginForm, RegisterForm, FundraiserForm, DonationForm


@lm.user_loader
def load_user(user_id):
    ans = Users.query.get(int(user_id))
    print(ans)
    return ans


# Logout user
@app.route("/logout")
def logout():
    logout_user()
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("user_name", "")
    return resp


# Register a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)

    msg = None
    success = False

    if request.method == "GET":
        return render_template("register.html", form=form, msg=msg)

    if form.validate_on_submit():
        username = request.form.get("username", "", type=str)
        password = request.form.get("password", "", type=str)
        email = request.form.get("email", "", type=str)

        user = Users.query.filter_by(user=username).first()
        user_by_email = Users.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = "Error: User exists!"

        else:
            pw_hash = bc.generate_password_hash(password)

            user = Users(username, email, pw_hash)
            user.save()

            msg = 'User created, please <a href="' + url_for("login") + '">login</a>'
            success = True

    else:
        msg = "Input error"

    return render_template("register.html", form=form, msg=msg, success=success)


# Authenticate user
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    msg = None

    if form.validate_on_submit():
        username = request.form.get("username", "", type=str)
        password = request.form.get("password", "", type=str)

        
        user = Users.query.filter_by(user=username).first()

        if user:
            if bc.check_password_hash(user.password, password):
                login_user(user)

                resp = make_response(redirect(url_for("dashboard")))
                resp.set_cookie("user_name", username)
                return resp
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template("login.html", form=form, msg=msg)


#Create a new fundraiser
@app.route('/new_fundraiser', methods = ['GET', 'POST'])
def new_fundraiser():
    form = FundraiserForm(request.form)

    msg     = None
    success = False

    if request.method == 'GET': 

        return render_template( 'post_fundraiser.html', form=form, msg=msg,created_by=current_user.user)

    
    if form.validate_on_submit():

        name = request.form.get('name', '', type=str)
        amount= request.form.get('amount',0, type=int)
        summary = request.form.get('summary', '', type=str) 
        #created_by    = request.form.get('created_by'   , '', type=str)     

        fundraiser = Fundraisers(name=name, amount=amount ,summary=summary ,created_by=current_user.user)

        fundraiser.save()

        msg     = 'Fundraiser created'     
        success = True

    else:
        msg = 'Input error'     
    username = request.cookies.get("user_name")
    data = Users.query.filter_by(user=username).first()
    return render_template( 'post_fundraiser.html', form=form, msg=msg, success=success, data=data,logged_in=True,created_by=current_user.user)


# App main route + generic routing (Home Page)
@app.route("/", defaults={"path": "index"})
@app.route("/<path>")
def index(path):
    
    try:
        name = request.cookies.get('user_name')
        print(name)
        if (name==None):
            return render_template("index.html",logged_in=False)
        return render_template("index.html",logged_in=name!="")
        
    except TemplateNotFound:
        return render_template("page-404.html"), 404

    except:
        return render_template("page-500.html"), 500



@app.route("/dashboard")
def dashboard():
    username = request.cookies.get("user_name")
    data = Users.query.filter_by(user=username).first()

    no_fundr = Fundraisers.query.filter_by(created_by=username).count()

    sum_result = (
        db.session.query(func.sum(New_donations.amount))
        .filter_by(name=username)
        .scalar()
    )
    print(sum_result)
    temp1=New_donations.query.filter_by(name=username).all()
    print(temp1)
    resp = make_response(
        render_template(
            "dashboard.html",
            data=data,
            no_fundr=no_fundr,
            sum_result=sum_result,
            Donations=temp1,
        )
    )
    return resp

# Return sitemap
@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(os.path.join(app.root_path, "static"), "sitemap.xml")

# method for creating fundraiser list
@app.route("/fundraiserlist")
def fundraiserlist():
     name = request.cookies.get('user_name')
     if (name==None):
        return render_template("fundraiserlist.html", Fundraisers=Fundraisers.query.all(),logged_in=False) 

     results = db.session.query(New_donations.fundraiser_name, func.sum(New_donations.amount)).group_by(New_donations.fundraiser_name).all()       
     return render_template("fundraiserlist.html", Fundraisers=Fundraisers.query.all(),logged_in=name!="",results=results)


@app.route('/new_donation2', methods=['GET', 'POST'])
def hello():
    
    if request.method=="POST":

        #name = request.form.get("name", "", type=str)
        #email = request.form.get("email", "", type=str)
        fundraiser_name = request.form.get("fundraiser_name", "", type=str)
        #print("Hello")
        amount = request.form.get("amount", "0", type=int)

        donation = New_donations(email = current_user.email, name= current_user.user,fundraiser_name=fundraiser_name,amount = amount)
        db.session.add(donation)
        db.session.commit()
        msg = "Donation Confirmed"
        success = True
        return redirect (url_for('pay', id = donation.id))
    return render_template('index2.html',name=current_user.user,email = current_user.email)


@app.route('/pay/<id>', methods=['GET', 'POST'])
def pay(id):
    user = New_donations.query.filter_by(id=id).first()
    client = razorpay. Client (auth = ("rzp_test_aa8LC7jVhoEkBI", "9QeRcMiD5dLcYQOEdHlHj6Tf"))
    payment = client.order.create({'amount': (int(user.amount)*100), 'currency': 'INR', 'payment_capture':'1'})
    return render_template('pay.html', payment = payment, x=user.email,y=user.name)
   

@app.route('/success', methods=['GET', 'POST'])
def success():
 return render_template('success.html')