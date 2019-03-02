from datetime import datetime

from twittor import db


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "id={}, body={}, create_time={}, user_id={}".format(
            self.id, self.body, self.create_time, self.user_id
        )
