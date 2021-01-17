def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: you tried to divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0)) #will print None
print(div42by(5))

print()
print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats!')
    elif int(numCats) < 0:
        raise Exception('numCats should be greater than 0. The value of numCats was: {}'.format(numCats))
    else:
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number')