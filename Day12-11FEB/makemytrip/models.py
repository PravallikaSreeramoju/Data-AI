from sqlalchemy import Column, Integer, String
from database import Base


# ==============================
# 🚌 BUS TABLE
# ==============================
class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    busname = Column(String, unique=True, index=True)
    total_seats = Column(Integer)
    available_seats = Column(Integer)


# ==============================
# ✈️ FLIGHT TABLE
# ==============================
class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flightname = Column(String, unique=True, index=True)
    total_seats = Column(Integer)
    available_seats = Column(Integer)


# ==============================
# 🏨 HOTEL TABLE
# ==============================
class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    hotelname = Column(String, unique=True, index=True)
    total_rooms = Column(Integer)
    available_rooms = Column(Integer)
