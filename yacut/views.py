import random
import string

from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import UrlForm
from .models import URLMap


def get_unique_short_id():
    letters_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_digits, 6))
    while URLMap.query.filter_by(short=rand_string).first():
        rand_string = ''.join(random.sample(letters_digits, 6))
    return rand_string


def check_unique_short_url(custom_id):
    if URLMap.query.filter_by(short=custom_id).first():
        return custom_id
    return None


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if short is None or not short or len(short) == 0:
            short = get_unique_short_id()
        if check_unique_short_url(short):
            flash(f'Имя {short} уже занято!', "error")
            return render_template('index.html', form=form)
        url_map = URLMap(original=form.original_link.data,
                         short=short)
        db.session.add(url_map)
        db.session.commit()
        flash(url_for('redirect_url', short=short, _external=True), "redirect")
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def redirect_url(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)
