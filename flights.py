# Assignment 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
popular_destinations = {"JFK", "LAX", "EWR", "CDG", "ATL", "DXB"}

# 1. Destinations shared by airlines
shared_destinations = our_routes.intersection(competitor_routes)
print(f"Destinations shared by both airlines: {shared_destinations}")

# 2. Destinations unique to our airline
unique_destination = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline: {unique_destination}")

# 3. Destinations not shared to either airline. Note: I was a little confused by the wording 
# of the question in context of the example data provided. Added popular_destinations to better
# show the logic of what I think was being asked
neither_airline_destinations = popular_destinations.difference(our_routes.union(competitor_routes))
print(f"Destinations neither airline flies to: {neither_airline_destinations}")

