from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas
from database import engine, SessionLocal, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MakeMyTrip Travel API with SQLite")


# ==============================
# DB Dependency
# ==============================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =================================================
# 🚌 BUS CRUD + BOOKING
# =================================================

# GET all buses
@app.get("/bus")
def get_buses(db: Session = Depends(get_db)):
    return db.query(models.Bus).all()


# GET individual bus
@app.get("/bus/{busname}")
def get_bus(busname: str, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.busname == busname).first()
    if not bus:
        raise HTTPException(404, "Bus not found")
    return bus


# SEARCH bus
@app.get("/bus/search/")
def search_bus(busname: str, db: Session = Depends(get_db)):
    buses = db.query(models.Bus).filter(
        models.Bus.busname.contains(busname)
    ).all()
    return buses


# ADD bus
@app.post("/bus/{busname}/seat")
def add_bus(busname: str, bus: schemas.BusCreate, db: Session = Depends(get_db)):
    new_bus = models.Bus(
        busname=busname,
        total_seats=bus.seats,
        available_seats=bus.seats
    )
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    return new_bus


# UPDATE seats
@app.put("/bus/{busname}/seat")
def update_bus(busname: str, seats: int, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.busname == busname).first()
    if not bus:
        raise HTTPException(404, "Bus not found")

    bus.available_seats = seats
    db.commit()
    return bus


# BOOK seat
@app.get("/bus/{busname}/seat")
def book_seat(busname: str, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.busname == busname).first()
    if not bus:
        raise HTTPException(404, "Bus not found")

    if bus.available_seats <= 0:
        return {"message": "No seats available"}

    bus.available_seats -= 1
    db.commit()

    return {
        "message": "Booking Confirmed",
        "remaining_seats": bus.available_seats
    }


# DELETE bus
@app.delete("/bus/{busname}")
def delete_bus(busname: str, db: Session = Depends(get_db)):
    bus = db.query(models.Bus).filter(models.Bus.busname == busname).first()
    if not bus:
        raise HTTPException(404, "Bus not found")

    db.delete(bus)
    db.commit()
    return {"message": "Bus deleted"}


# =================================================
# ✈️ FLIGHT CRUD
# =================================================

@app.get("/flight")
def get_flights(db: Session = Depends(get_db)):
    return db.query(models.Flight).all()


@app.post("/flight/{flightname}/seat")
def add_flight(flightname: str, flight: schemas.FlightCreate, db: Session = Depends(get_db)):
    new_flight = models.Flight(
        flightname=flightname,
        total_seats=flight.seats,
        available_seats=flight.seats
    )
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight


@app.delete("/flight/{flightname}")
def delete_flight(flightname: str, db: Session = Depends(get_db)):
    flight = db.query(models.Flight).filter(
        models.Flight.flightname == flightname
    ).first()

    if not flight:
        raise HTTPException(404, "Flight not found")

    db.delete(flight)
    db.commit()
    return {"message": "Flight deleted"}


# =================================================
# 🏨 HOTEL CRUD
# =================================================

@app.get("/hotel")
def get_hotels(db: Session = Depends(get_db)):
    return db.query(models.Hotel).all()


@app.post("/hotel/{hotelname}/room")
def add_hotel(hotelname: str, hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
    new_hotel = models.Hotel(
        hotelname=hotelname,
        total_rooms=hotel.rooms,
        available_rooms=hotel.rooms
    )
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return new_hotel


@app.delete("/hotel/{hotelname}")
def delete_hotel(hotelname: str, db: Session = Depends(get_db)):
    hotel = db.query(models.Hotel).filter(
        models.Hotel.hotelname == hotelname
    ).first()

    if not hotel:
        raise HTTPException(404, "Hotel not found")

    db.delete
