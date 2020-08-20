from models import db, Cupcake
from app import app


db.drop_all()
db.create_all()


cupcakes = [
    Cupcake(flavor="Chocalte", size="Large", rating=2.3),
    Cupcake(flavor="Vanilla", size="Small", rating=3.4),
    Cupcake(flavor="Chocalte", size="Large", rating=2),
    Cupcake(flavor="Peanut Butter", size="Medium", rating=5)
]

db.session.add_all(cupcakes)
db.session.commit()
