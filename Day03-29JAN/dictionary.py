# mydict={"key1":"value1","key2":"value2"}
# print(type(mydict))

trip={
    "provider":"uber",
    "source":"pondicherry",
    "destination" : "chennai airport",
    "fare" : 3500.50,
    "status" : "completed"
}

# print(trip["provider"])
# print(trip["fare"])

# GET_METHOD
# print(trip.get("source"))
# print(trip.get(3500.50))

# KEYS & VALUES
# print(trip.keys())
# print(trip.values())

# ITEMS
# for key,value in trip.items():
#     print(f"key : {key}, value : {value}")

# UPDATE
# trip.update({"distance_km":150})
# print(trip)

# POP
# trip.pop("distance_km")
# print(trip)

# trip["fare"]=4000.00
# print(trip)

# for key in trip:
#     print(key,"->",trip[key])

