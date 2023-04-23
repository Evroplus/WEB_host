from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from data.users import User
from forms.user import RegisterForm
from data import db_session
import bluda_api
from flask_ngrok import run_with_ngrok
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WEB_secret_key'

pichci = {}
con = 's'
for i in os.listdir('static/img'):
    pichci[str(con)] = f'/static/img/{i}'
    con += 's'

opis = {}
oon = 'o'
with open('opisanie.txt', encoding='utf8') as us:
    for i in us.readlines():
        opis[oon] = i
        oon += 'o'

names = {}
na = 'n'
with open('bluda.txt', encoding='utf8') as us:
    for i in us.readlines():
        names[na] = i
        na += 'n'

price = {}
pr = 'p'
with open('price.txt', encoding='utf8') as us:
    for i in us.readlines():
        price[pr] = i
        pr += 'p'

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', **pichci, **opis, **names)

@app.route('/product.html/<nims>')
def product(nims):
    pric = price['p' * int(nims)]
    nomer = pichci['s' * int(nims)]
    name = names['n' * int(nims)]
    opisan = opis['o' * int(nims)]
    return render_template('product.html', picha=nomer, name=name, opis=opisan, price=pric)


@app.route('/form.html', methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template('form.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('form.html', title='Регистрация', form=form)


@app.route('/spravka.html')
def spravka():
    return render_template('spravka.html', title='Справка')


@app.route('/telegram')
def telega():
    return f'<meta http-equiv="Refresh" content="0; URL=https://t.me/YandexLyceumDeliveryBot">'


if __name__ == '__main__':
    print(names)
    db_session.global_init("db/food.db")
    app.register_blueprint(bluda_api.blueprint)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    #run_with_ngrok(app)
    #app.run(port=8080, host='127.0.0.1')