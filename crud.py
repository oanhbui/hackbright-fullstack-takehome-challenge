from model import db, User, Slot, Reservation, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

def get_user_by_name(name):
    return User.query.filter(User.user_name == name).first() 