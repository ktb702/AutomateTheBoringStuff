import pprint # pretty print
message = 'Seattle is always nice in the summer time'
count = {}

for char in message.upper():
    count.setdefault(char, 0)
    count[char] = count[char] + 1
    # could also do the above in one line
    count[char] = count.get(char, 0) + 1

pprint.pprint(count)

# could also print using this method
msg = pprint.pformat(count)
print(msg)