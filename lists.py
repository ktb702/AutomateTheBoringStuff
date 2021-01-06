import copy

languages = ['java', 'C', 'python', 'php', 'ruby', 'javascript']
for i in range(len(languages)):
    print('Index ' + str(i) + ' of languages is: ' + languages[i])

#multiple assignments
dog = ['large', 'brindle', 'bark']
size, color, action = dog

size, color, action = 'small', 'blonde', 'whine'

#indexing a list
indexOf = dog.index('large')
print(indexOf)

# append, insert
# note that append and insert do not have return values (well technically they return None), and should not be assigned to a new value
dog = ['pit bull', 'boxer', 'great dane', 'weiner']
dog.append('lab') #appends to the end
print('List after append')
print(dog)
dog.insert(2, 'terrier') # places in pos 2 and moves everything else to the left
print('List after insert')
print(dog)

# remove vs delete
del dog[0] #deletes value at index 0
dog.remove('boxer') # removes the first instance of 'boxer' found in the list

# sort 
#can be used on numbers or strings, but not on a list that contains numbers AND strings
dog.sort()
print('List after sorting' + '\n' + str(dog))
dog.sort(reverse=True) #sorts in reverse order

#sorting happens in ASCII-betical order. So all upper case letters come first, then lower case.
letters = ['A', 'a', 'B', 'b', 'D', 'Z', 'z', 'g']
letters.sort()
print(letters)
letters.sort(key=str.lower) # this will sort with all lower case letters to give you true alphabetical order
print(letters)

# deep vs shallow copies
l2 = letters #shallow copy - both lists reference the same data in memory
l2.insert(1, 'ABC') # this changes letters also
print(letters)

l3 = copy.deepcopy(letters) #creates a deep copy - lists refer to different places in memory
l3.insert(3, 'blah')
print(letters)
print(l3)