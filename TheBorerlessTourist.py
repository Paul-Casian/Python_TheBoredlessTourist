### Input destination
destinations = [ 
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt"
]

attractions = []

### Test traveler in order to see functionality
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

###### Functions ######
### Get destination index
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
### Get treveler location
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
### Get attraction list
def get_attraction_list():
    for destination in range(len(destinations)):
        attractions.append(destinations[destination])
        attractions[destination] = []
### Add atractions
def add_attraction(destination,attraction):
    destination_index = get_destination_index(destination)
    attraction_for_destination = attractions[destination_index].append(attraction)


###
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
get_attraction_list()
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)