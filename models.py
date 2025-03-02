from app import db


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    role = db.Column(db.String, nullable = True)

    def __repr__(self):
        return f"<User : {self.name}, Role : {self.role}"
    
    