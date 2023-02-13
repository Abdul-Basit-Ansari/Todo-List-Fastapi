

from database import SessionLocal, engine

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
