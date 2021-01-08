# dictionaries are key-vaue pairs (equivalent to Map interface in Java)
# unlike lists, the order of a dict does not matter. 
# like lists, they are a mutable data type and variables hold references to dict values.
# tuples are like lists but they are immutable and defined with ()
house = {'sq ft': 1500, 'bedrooms': 3, 'neighborhood': 'bellevue'}
print('My house is located in ' + house['neighborhood']) 
# print(house[color]) #would throw a KeyError as this key does not exist in this dict
# print(house[0]) #would throw a KeyError as values are referenced by key not by index

#can find out if a key exists/does not exist in a dict 
print('bedrooms' in house) #True
print('bedrooms' not in house) #False
print('color' in house) #False
print('color' not in house) #True

# keys, values, items methods
print(house.keys()) # returns the keys of the dict
print(house.values()) # returns the values of the dict
print(house.items()) # returns two item tuples of the key, value pair
print()

#alternatively you can use the following that return list like data types 
print(list(house.keys()))
print(list(house.values()))
print(list(house.items()))
print()

# can use the above methods in for loops also
for i in house.keys():
    print(i)

for j in house.values():
    print(j)

for k, v in house.items():
    print(k, v)

# get method - helpful to avoid KeyError
bedrooms = house.get('bedrooms', 0) #returns the value of 'bedrooms' or 0 if it doesn't exist.
print('The number of bedrooms is ' + str(bedrooms))
color = house.get('color', '')
print('The color of the house is ' + color)

# setdefault - sets a key/value pair in the dict only if the key doesn't exist already
house.setdefault('bathrooms', 2)
print(house)
house.setdefault('bathrooms', 2.5) #doesn't do anything because the key/value pair is already set
