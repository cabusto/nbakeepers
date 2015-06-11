from flask import render_template, url_for, redirect, Blueprint
from project import app
from yahooapi import YahooAPI
from apiconnect import apiConnect
from yahooform import yahooForm



home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

@home_blueprint.route('/', methods=['GET', 'POST'])
@home_blueprint.route('/welcome', methods=['GET', 'POST'])
def welcome():
    
    api = apiConnect('keys')
    link = api.getURL()
    form = yahooForm()
    if form.validate_on_submit():
        #yahoo = YahooAPI('keys', form.authToken.data)
        api.connect(form.authToken.data)
        #return redirect('/success')
    return render_template('welcome.html', link=link, form=form)