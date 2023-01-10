from models import app,db

with app.app_context():

    # To Delete tables
    db.drop_all()
    print("deleted tables")

    # To Create tables
    db.create_all()
    print("created tables")