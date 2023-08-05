from datetime import datetime

from app import db


# todo add users
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(64), index=True, unique=True)
#     password_hash = db.Column(db.String(128))


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longUrl = db.Column(db.String(128), index=True, unique=True)
    shortUrl = db.Column(db.String(16), index=True, unique=True)
    isEvil = db.Column(db.Boolean, default=False)
    timestamp_utc = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'longUrl': self.longUrl,
            'shortUrl': self.shortUrl,
            'isEvil': self.isEvil,
            'timestamp_utc': self.timestamp_utc.isoformat() if self.timestamp_utc else self.timestamp_utc
        }


class UrlLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(128), index=True, unique=False)
    timestamp_utc = db.Column(db.DateTime, index=True, default=datetime.utcnow)
