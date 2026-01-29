import uber_functions as uber
import time

name=input("Enter your name:")
name=name.strip().title()
phn_num=input("Enter your phone number: ")
masked_phn_num=phn_num[:2]+"******"+phn_num[-2:]
uber.view_locations()
print("please select the starting location: ")
source=int(input())
source_loc=uber.location_ret(str(source))
print("please select the dropping location: ")
dest=int(input())
dest_loc=uber.location_ret(str(dest))
uber.status(0)
price=uber.cost(source,dest)
print(f"trip fare: {price}")
confirm=uber.conf(source_loc,dest_loc,price)
if confirm=='n':
    reason=input("Why do you want to cancel your ride? ")
    print("Thank you for your feedback.")
else:
    driver=uber.driver_asgn(source)
    print(f"{driver} is assigned as driver for your trip.")
    uber.status(1)
    time.sleep(2)
    uber.status(2)
    uber.status(3)
    print("Hope you have a safe journey.")
    time.sleep(2)
    uber.status(4)
    time.sleep(5)
    curr=input("Did you arrive at your destination? y/n : ")
    if curr=='y':
        uber.status(5)
        print(f"Please pay {price} to {driver}")
        fdbck_driver=float(input(f"Please share your rating of {driver} (driver) 1-5 : "))
        fdbck_ride=input("Please share your feedback:")
        inv_req=input("Do you want an invoice of this ride booking? y/n : ")
        if inv_req == 'y':
            uber.invoice(Name=name,Phone_number=masked_phn_num,Source=source_loc,Destination=dest_loc,Fare=price,Driver=driver,Driver_Feedback=fdbck_driver,Ride_feedback=fdbck_ride)
        print("Thank you for choosing uber :) ")


    