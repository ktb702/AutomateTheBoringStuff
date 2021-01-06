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