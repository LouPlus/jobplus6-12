from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_user, logout_user, login_required

from jobplus.models import User
from jobplus.forms import LoginForm, CompanyregisterForm


front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('.index'))

        # todo: add different redirect for different user groups

    return render_template('login.html', form=form)


@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logout!', 'success')
    return redirect(url_for('.index'))


@front.route('/companyregister', methods=['GET', 'POST'])
def companyregister():
    form = CompanyregisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('Company Register Success, please login!', 'success')
        return redirect(url_for('.login'))
    return render_template('/company/register.html', form=form)