def view_locations(**kwargs):
    cities={"1" : "Hyderabad", "2" : "Chennai", "3" : "Bangalore", "4" : "Mumbai" , "5" :"Delhi"}
    for key,value in cities.items():
        print(f"{key} : {value}")

def location_ret(loc):
    cities={"1" : "Hyderabad", "2" : "Chennai", "3" : "Bangalore", "4" : "Mumbai" , "5" :"Delhi"}
    return cities[loc]

def driver_asgn(source):
    drivers=("VIJAY","RAM","ANJALI","PIYUSH","BHAMI")
    return drivers[source-1]


def cost(source,dest):
    return source*dest*1500

def conf(source,dest,price):
    print(f"Source : {source} \nDestination : {dest} \nFare: {price}")
    confirm=input("Do you want to confirm your ride? (y/n) : ")
    return confirm

def status(n):
    mytuple=["ride not yet confirmed.","driver is arriving to your start point...","driver arrived at your location.","ride started.","travelling.","Ride completed."]
    print(f"status: {mytuple[n]}")

def invoice(**kwargs):
    print("\n----- INVOICE -----")
    for key,value in kwargs.items():
        print(f"{key} : {value}")