"""Models for reservation app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Replace this with your code!
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String, unique=True)

    reservations = db.relationship("Reservation", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.user_name}>'

class Slot(db.Model):
    __tablename__ = "slots"
    slot_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    reservation = db.relationship("Reservation", back_populates="slot")

    def __repr__(self):
        return f'<Slot slot_id={self.slot_id} start_time={self.start_time}>'

class Reservation(db.Model):
    __tablename__ = "reservations"
    reservation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    slot_id = db.Column(db.Integer, db.ForeignKey("slots.slot_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    slot = db.relationship("Slot", back_populates="reservation")
    user = db.relationship("User", back_populates="reservations")

    def __repr__(self):
        return f'<Reservation reservation_id={self.reservation_id} slot_id={self.slot_id}>'

def connect_to_db(flask_app, db_uri="postgresql:///reservation", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)