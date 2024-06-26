from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Situation(db.Model):
    __tablename__ = 'situation'
    situation_id = db.Column(db.Integer, primary_key=True)
    en = db.Column(db.String)
    ru = db.Column(db.String)
    kz = db.Column(db.String)
    description_en = db.Column(db.String)
    description_ru = db.Column(db.String)
    description_kz = db.Column(db.String)
    animation = db.Column(db.String)
    
    sentences = db.relationship('Sentence', backref='situation', lazy=True)

    def to_dict(self):
        return {
            'situation_id': self.situation_id,
            'en': self.en,
            'ru': self.ru,
            'kz': self.kz,
            'description_en': self.description_en,
            'description_ru': self.description_ru,
            'description_kz': self.description_kz,
            'animation': self.animation
        }

class Sentence(db.Model):
    __tablename__ = 'sentence'
    sentence_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    en = db.Column(db.String)
    kz = db.Column(db.String)
    ru = db.Column(db.String)
    audio = db.Column(db.String)
    situation_id = db.Column(db.Integer, db.ForeignKey('situation.situation_id'))
    
    def to_dict(self):
        return {
            'sentence_id': self.sentence_id,
            'en': self.en,
            'kz': self.kz,
            'ru': self.ru,
            'audio': self.audio,
            'situation_id': self.situation_id
        }
