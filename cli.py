from db.models import Base, create_engine

db = create_engine('sqlite:///db/system.db', echo=True)
Base.metadata.create_all(db)