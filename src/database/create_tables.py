import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, Column, Integer, String, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_connection_string

Base = declarative_base()

# Define Tables
class Coverage(Base):
    __tablename__ = 'coverage'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10))
    name = Column(String(255))
    year = Column(Integer)
    antigen = Column(String(100))
    coverage = Column(Float)
    target_number = Column(BigInteger)
    doses = Column(BigInteger)

class Incidence(Base):
    __tablename__ = 'incidence'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10))
    name = Column(String(255))
    year = Column(Integer)
    disease = Column(String(100))
    incidence_rate = Column(Float)

class ReportedCases(Base):
    __tablename__ = 'reported_cases'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10))
    name = Column(String(255))
    year = Column(Integer)
    disease = Column(String(100))
    cases = Column(BigInteger)

class VaccineIntro(Base):
    __tablename__ = 'vaccine_introduction'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    iso_code = Column(String(10))
    country_name = Column(String(255))
    year = Column(Integer)
    vaccine = Column(String(100))

class VaccineSchedule(Base):
    __tablename__ = 'vaccine_schedule'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    iso_code = Column(String(10))
    country_name = Column(String(255))
    year = Column(Integer)
    vaccine_code = Column(String(100))

def create_all_tables():
    """Create all tables in the database"""
    
    print("\n" + "="*60)
    print("CREATING DATABASE TABLES")
    print("="*60)
    
    try:
        # Create engine
        connection_string = get_connection_string()
        engine = create_engine(connection_string)
        
        print("\nConnecting to database...")
        print(f"Database: {connection_string.split('@')[1]}")
        
        # Create all tables
        Base.metadata.create_all(engine)
        
        print("\n✅ Successfully created all tables:")
        print("   - coverage")
        print("   - incidence")
        print("   - reported_cases")
        print("   - vaccine_introduction")
        print("   - vaccine_schedule")
        
        print("\n" + "="*60)
        print("DATABASE SCHEMA CREATION COMPLETE!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error creating tables: {e}")
        raise

if __name__ == "__main__":
    create_all_tables()
