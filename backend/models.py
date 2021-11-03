from app import db

class RecipeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    coffee = db.Column(db.Float, nullable=False)
    water = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return "Recipe %r" % self.name
