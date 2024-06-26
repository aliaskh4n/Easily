from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from models import db, Situation, Sentence
from forms import SituationForm, SentenceForm
from sqlalchemy.orm import sessionmaker
import ssl

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'MySecretKey'

db.init_app(app)

@app.route('/info')
def info():
    return render_template('index.html')

@app.route('/')
def index():
    return redirect(url_for('loading'))

@app.route('/<lang>')
def main(lang):
    situations = Situation.query.all()
    situations_dict = []

    for situation in situations:
        count = len(situation.sentences)

        if lang == 'en':
            situations_dict.append({
                'title': situation.en,
                'description': situation.description_en,
                'situation_id': situation.situation_id,
                'animation': situation.animation,
                'count': count
            })
        elif lang == 'ru':
            situations_dict.append({
                'title': situation.ru,
                'description': situation.description_ru,
                'situation_id': situation.situation_id,
                'animation': situation.animation,
                'count': count
            })
        else:
            situation_dict = situation.to_dict()
            situation_dict['count'] = count
            situations_dict.append(situation_dict)

    return render_template('test.html', buttons_data=situations_dict)


@app.route('/load')
def loading():
    return render_template('load.html')

@app.route('/situation/<int:situation_id>/<lang>')
def text(situation_id, lang):
    Session = sessionmaker(bind=db.engine)
    session = Session()
    situation = session.get(Situation, situation_id)
    sentences = session.query(Sentence).filter_by(situation_id=situation_id).all()
    if lang == 'en':
        situations_dict ={'title': situation.en, 'description': situation.description_en}
        sentences_dict = [{
            'title': sentence.en,
            'translate': sentence.kz,
            'audio': sentence.audio}for sentence in sentences]
    elif lang == 'ru':
        situations_dict ={'title': situation.ru, 'description': situation.description_ru}
        sentences_dict = [{
            'title': sentence.ru,
            'translate': sentence.kz,
            'audio': sentence.audio} for sentence in sentences]
    return render_template('text.html', situation=situations_dict, sentences=sentences_dict)


if __name__ == '__main__':
    cert_file = '/etc/letsencrypt/live/neko-anime.site/cert.pem'
    key_file = '/etc/letsencrypt/live/neko-anime.site/privkey.pem'
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)
    app.run(host='0.0.0.0', port=443, ssl_context=context)