# strings are immutable
# when comparing stings, case matters. Use .lower() or .upper() methods to avoid case issues

greeting = 'Hello There!'
print(greeting.isupper()) #False because there are lower case letters also

num = '12345'
print(num.isupper()) #False because there are no letters in this string

#other is___() methods: 
# isalpha() --> letters only: returns True
# isalnum() --> letters and numbers only: returns True
# isdecimal() --> numbers only: returns True
# isspace() --> whitespace only: returns True
# istitle() --> titlecase only: returns True

# startswith() & endswith()
print("greeting starts with 'H' -" + str(greeting.startswith('H'))) #True
print("greeting starts with 'h' -" + str(greeting.startswith('h'))) #False because case matters

#join()
myPets = ['cat', 'dog', 'snake']
print('my pets are ' + myPets[0] + myPets[1] + myPets[2])
j = ","
print(j.join(myPets)) # joins the elements in the list so that they are separated with a comma.

#split()
pets = 'CatDogRat'
print([pets[i:i+3] for i in range(0, len(pets), 3)]) #split at every 3rd letter

#ljust() rjust() center() - adds space either left or right of (or centers) the string so that the string is the specified number of spaces in total.
print("ljust: " + greeting.ljust(20))
print("rjust: " + greeting.rjust(20))
print("center: " + greeting.center(20))
print("center: " + greeting.center(20, '-'))

#strip() methods
print("strip: " + greeting.strip()) #removes any white space
print("lstrip: " + greeting.lstrip()) #removes any white space from the left of the string
print("rstrip: " + greeting.rstrip()) #removes any white space from the right of the string

phrase = 'yoyoheyhoyoletsgoyoyo'
print(phrase.strip('yo')) #removes the letters y & o from the beginning and end of the string

#replace() method
print(phrase.replace('o', '!')) #replace every 'o' in the string with a '!'