# SET : unique elements, not ordered, not based on indexing, mutable

# myset={1,3,4,5,5,2}
# print(myset)

uber_cities={"chennai","bangalore","hyderabad", "delhi"}
# print(uber_cities)

# ADD
# uber_cities.add("pondicherry")
# print(uber_cities)

# LIST
# list_cities=list(uber_cities)
# print(type(list_cities))


# UNION
uber_cities2={"mumbai","kolkata","delhi","chennai"}
# print(uber_cities.union(uber_cities2))

# INTERSECTION
# print(uber_cities.intersection(uber_cities2))

# DIFFERENCE
# print(uber_cities.difference(uber_cities2))

uber_cities.add("pune")
# print(uber_cities)

# REMOVE
uber_cities.remove("pune")
# print(uber_cities)

print(len(uber_cities))

