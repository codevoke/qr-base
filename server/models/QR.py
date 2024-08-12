from .db import db


class QRModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    counter = db.Column(db.Integer, default=0)
    name = db.Column(db.String)
    manufacture = db.Column(db.String)
    code = db.Column(db.String)

    @classmethod
    def get_by_code(cls, code: str, SYSTEM=False):
        qr = cls.query.filter_by(code=code).first()

        if qr is None:
            return None

        else:
            if not SYSTEM:
                qr.counter += 1
                qr.save()
            return qr

    def save(self):
        db.session.add(self)
        db.session.commit()
