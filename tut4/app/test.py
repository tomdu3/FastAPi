from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Sample SQLite in-memory database for quick testing
DATABASE_URL = "sqlite:///:memory:"

# Create Database Engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test the Session import
session: Session = SessionLocal()
print(f"Session created: {session}")
session.close()