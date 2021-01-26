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
print(msg.group())
print(msg.group(1))

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
print(msg.group())

batRegex = re.compile(r'Bat(wo)+man') #the + means that the group in the () MUST appear 1 or more times

