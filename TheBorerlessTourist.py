### Input destination
destinations = [ 
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt"
]


### Test traveler in order to see functionality
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

###### Functions ######
### Get destination index
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
### Get treveler location
def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
### 
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
