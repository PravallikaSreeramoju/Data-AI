from pydantic import BaseModel


# ==============================
# 🚌 BUS SCHEMA
# ==============================
class BusCreate(BaseModel):
    seats: int


class BusResponse(BaseModel):
    busname: str
    total_seats: int
    available_seats: int

    class Config:
        from_attributes = True


# ==============================
# ✈️ FLIGHT SCHEMA
# ==============================
class FlightCreate(BaseModel):
    seats: int


class FlightResponse(BaseModel):
    flightname: str
    total_seats: int
    available_seats: int

    class Config:
        from_attributes = True


# ==============================
# 🏨 HOTEL SCHEMA
# ==============================
class HotelCreate(BaseModel):
    rooms: int


class HotelResponse(BaseModel):
    hotelname: str
    total_rooms: int
    available_rooms: int

    class Config:
        from_attributes = True
