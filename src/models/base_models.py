from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    exchange = db.Column(db.String(255))
    is_blacklisted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Company {self.name.title()}>'


class Bot(db.Model):
    __tablename__ = 'bot'

    id = db.Column(db.Integer, primary_key=True)
    bot_status = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())


class Trade(db.Model):
    __tablename__ = 'trade'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255))
    order_price = db.Column(db.Numeric(10, 2))
    trade_status = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, default=db.func.now(), onupdate=db.func.now())


class Ticker(db.Model):
    __tablename__ = 'ticker'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
