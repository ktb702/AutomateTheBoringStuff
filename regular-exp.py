import re #regular expressions library

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = phoneNumRegex.search('Call for your free consultation at 123-456-7890')
#the search method returns a match object, and that match object has a group method that returns the matched string
print(message.group())

#instead of using search() and group() you can use findall()
print(phoneNumRegex.findall('Call for your free consultation at 123-456-7890'))

#can also create multiple groups using ()
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Call for your free consultation at 123-456-7890')
print("entire group: " + mo.group())
print("group 1: " + mo.group(1))


#EXAMPLE 2#
batRegex = re.compile(r'Bat(man | mobile | girl | copter)')
msg = batRegex.search('Batmobile lost a wheel')
# print(msg.group())
# print(msg.group(1))

msg = batRegex.search('Batmoto lost a wheel') # this will return None because 'moto' is not part of the raw string
print(msg == None)

batRegex = re.compile(r'Bat(wo)?man') #the ? means that the group in () can appear 0 or 1 times
msg = batRegex.search('Batman') 
print(msg.group())
msg = batRegex.search('Batwoman')
print(msg.group())
msg = batRegex.search('Batwowowowman') #returns none because 'wo' cannot appear more than once

batRegex = re.compile(r'Bat(wo)*man') #the * means that the group in the () can appear any number of times
msg = batRegex.search('Batwowowowman')

batRegex = re.compile(r'Bat(wo)+man') #the + means that the group in the () MUST appear 1 or more times

charRegex = re.compile(r'\+\*\?')
charRegex.search('I learned about +*? regex syntax')
charRegex = re.compile(r'(\+\*\?)+') #means that one of the characters + * or ? must appear at least once
charRegex.search('I learned about +*?+*?+*?+*? syntax')

haRegex = re.compile(r'(Ha){3}') #the string must be found 3 times. There cannot be spaces between () and {}
msg = haRegex.search("That was so funny HaHaHa") #returns a match object
print(msg)
msg = haRegex.search("That was so funny HaHaha") #doesn't match because of the lower case 'h'
print(msg)

haRegex = re.compile(r'(Ha){3,5}') #the string 'Ha' must be matched between 3 and 5 times
haRegex = re.compile(r'(Ha){3,}')  #using {3,} means that it can be matched 3 or more times
haRegex = re.compile(r'(Ha){,5}')  #using {,5} means that it can be matched up to 5 times

#GREEDY MATCHING#
digitRegex = re.compile(r'(\d){3,5}') 
print(digitRegex.search('1234567890')) #will return the longest possible (greedy) string that matches, so 12345

#NON-GREEDY MATCHING#
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1234567890')) #will return the shortest string possible, so 123

#FINDALL METHOD#
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
msg = '''1. 1-603-413-4124: Calling Santa Ever thought of reaching out to Santa months before the Christmas period? Well, this line allows you to talk to the man in charge of deciding who gets what for Christmas. Read more: https://www.legit.ng/1343001-funny-numbers-call-bored-stuck-home.html
2. 605-475-6961: Harry Potter's contact This one is for the Harry Potter Universe fans. If you are seeking admission into the fabled Hogwarts School of Witchcraft and Wizardry, then dial this line. From the first digits of the contact, it seems that the admission office is located in South Dakota, but hey, the location does not matter now, does it? The voice on the other side of the call will give you information related to locating the legendary platform 9¾, as well as your admission details. Read more: https://www.legit.ng/1343001-funny-numbers-call-bored-stuck-home.html
3. (858) 651-5050: Beautiful phrases When looking for random phone numbers to call, it does not get funkier than this one. Dialing this line allows you to listen to what sounds like the most well-thought poem ever written. The voices include numerous phrases spoken by female and male speakers which all sound amazingly perfect. The phrases' beauty lies less in their meanings and more in the flow of words. You will be surprised to learn that the sentences are known as 'Harvard Sentences' and that they were first introduced in 1969 by the IEEE (Institute of Electrical and Electronics Engineers). The institute recommended these phrases for speech quality measurement at a time when there was a need to test various types of noise for military communications during the war. Read more: https://www.legit.ng/1343001-funny-numbers-call-bored-stuck-home.html
4. 605–475–6964: Things could actually be worse This is one of the best dial a joke phone numbers. Read more: https://www.legit.ng/1343001-funny-numbers-call-bored-stuck-home.html
5. 605-475-6959: The bad breath notification hotline Have you ever met someone that, on first glance, looks to be an ideal mate but as soon as they open their mouth and begin speaking, an unbelievable odour comes from their mouth? While it is never advised to be rude, giving them prank phone numbers that tell them what you could not is the best way to go. By having them dial 605-475-6959, they will be directed to the bad breath notification hotline. While this person was unable to score a second date with you, maybe that wake-up call could be what changes their breath forever. Read more: https://www.legit.ng/1343001-funny-numbers-call-bored-stuck-home.html
'''
phoneNums = phoneRegex.findall(msg)
print(phoneNums) #returns a list of matches(strings) instead of a match object

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNums = phoneRegex.findall(msg) #returns a list of tuples because we created groups with parentheses
print(phoneNums)

#CHARACTER CLASSES#
# \d - any numeric digit 0-9
# \D - any char that is NOT a digit
# \w - any letter, numeric, or underscore char (think "word" chars)
# \W - any char that is NOT a letter, numeric, or underscore
# \s - any space, tab, or newline char
# \S - anything that is NOT a space, tab, or newline

lyrics = '''12 drummers drumming
11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 golden rings
4 calling birds
3 french hens
2 turtle doves, and
1 partridge in a pear tree'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]') # the [] allows you to create your own character classes
print(vowelRegex.findall('I like to eat apples and bananas'))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}') #will only find any 2 vowel together
print(doubleVowelRegex.findall('I like to eat apples and bananas'))

consRegex = re.compile(r'[^aeiouAEIOU]') #finds anything that IS NOT one of those chars (i.e. consonants)
print(consRegex.findall('I like to eat apples and bananas!'))

#to make your char class case-INsensitive, pass re.I 
vowelRegex = re.compile(r'[aeiou]', re.I)

#BEGINS WITH#  ^
beginsWithRegex = re.compile(r'^Hello')
print(beginsWithRegex.search("Hello, is it me you're looking for?"))
print(beginsWithRegex.search("I said hello!") == None) # no match beacuse it doesn't start with the string 'Hello'

#ENDS WITH#  $
endsWithRegex = re.compile(r'world!$')
print(endsWithRegex.search("What in the world!"))
print(endsWithRegex.search("What in the world  ") == None)

allDigitsRegex = re.compile(r'\d+$')
print(allDigitsRegex.search("3179876513168764551654"))
print(allDigitsRegex.search("31798765131x8764551654.") == None) 

#DOT# picks up everything EXCEPT a newline character
atRegex = re.compile(r'.at') # . is looking for one character and then 'at'
print(atRegex.findall("The cat in the hat sat on the flat mat in his raincoat."))

# atRegex = re.compile(r'{1,2}.at') # will find the first 2 chars before the 'at'
# print(atRegex.findall("The cat in the hat sat on the flat mat in his raincoat."))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # .* is greedy, for non-greedy matching use .*?
print(nameRegex.findall('First Name: Kate Last Name: Baldwin'))

dotStar = re.compile(r'.*') #picks up all but the newline character
print(dotStar.findall(lyrics))
dotStar = re.compile(r'.*', re.DOTALL) #will include the newline character
print(dotStar.findall(lyrics))

#SUB METHOD#
namesRegex = re.compile(r'Agent \w+') #Agent with 1 or more word characters
print(namesRegex.findall('Agent Amber gave the secret flash drive to Agent Bailey'))
namesRegex.sub('REDACTED', 'Agent Amber gave the secret flash drive to Agent Bailey.')

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Amber gave the secret flash drive to Agent Bailey'))
#change to a raw (r) string so that the literal \ isn't printed. 1 is for the first group (\w)
print(namesRegex.sub(r'Agent \1***', 'Agent Amber gave the secret flash drive to Agent Bailey.') )

#VERBOSE MODE#
phoneRegex = re.compile(r'''
(\d\d\d)    #area code
-           #first dash
\d\d\d      #first 3 digits
-
\d\d\d\d''', re.VERBOSE)
#could add multiple arguments to compile method
phoneRegex = re.compile(r'''
(\d\d\d)    #area code
-           #first dash
\d\d\d      #first 3 digits
-
\d\d\d\d''', re.VERBOSE | re.DOTALL | re.I)
