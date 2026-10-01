# opinions_app/models.py

from datetime import datetime

from . import db


class Opinion(db.Model):
    __tablename__ = 'opinion'
    __table_args__ = (
        db.UniqueConstraint('text', name='uq_opinion_text'),
    )

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    added_by = db.Column(db.String(64))
