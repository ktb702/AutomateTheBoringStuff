#! python3
import re, pyperclip

#Create a regex for phone numbers
phoneRegex = re.compile(r'''
((\d\d\d) | (\(\d\d\d)))?    #area code (optional)
(\s|-)                       #first separator
\d\d\d                       #first 3 digits
-                            #second separator 
\d\d\d\d                     #last 4 digits 
(((ext(\.)?\s) | x)          #extension word-part (optional) 
 (\d{2,5}))?                 #extension number-part (optional)
''', re.VERBOSE)

#Create a regex for email addresses
emailRegex = re.compile(r''' 
[a-z0-9_.+]+        #name part
@                   #@
[a-z0-9_.+]+        #domain name part
''', re.VERBOSE | re.I)

#Get text off the clipboard
text = pyperclip.paste()

#TODO: Extract phone/email from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print() #debug

#TODO: Copy the extracted email/phone to the clipboard
