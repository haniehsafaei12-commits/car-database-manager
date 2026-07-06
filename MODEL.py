from sqlalchemy import create_engine , text , Column , Integer, String , Float 
from sqlalchemy.orm import declarative_base , sessionmaker
from urllib.parse import quote_plus
password="haha11code34@#h7"
password_encoded=quote_plus(password)

engine=create_engine(f"mysql+mysqlconnector://root:{password_encoded}@localhost")
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS Car_db_project"))
    engine=create_engine(f"mysql+mysqlconnector://root:{password_encoded}@localhost/Car_db_project")
Base=declarative_base()
RobotFactory=sessionmaker(bind=engine)
car_attributes=RobotFactory()
class Car(Base):
    __tablename__="Cars" 
    Id=Column(Integer , primary_key=True , autoincrement=True)
    Name=Column(String(50) , nullable=False)
    Model=Column(String(50) , nullable=False)
    Color=Column(String(30) , nullable=False)
    Horse_Power=Column(Integer , nullable=False)

Base.metadata.create_all(engine)

