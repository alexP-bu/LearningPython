str = "testing1 testing2"
print(str)
str = str.upper()
print(str)
print(str.lower().find('e'))
str = str.lower()
print(str.capitalize())
print(str.split(' '))
print(str.split('e'))
print(str.replace('t', 'b'))
print(str.replace('t', 'b').split(' '))
print("Testing slice operator:")
print(str[::])
print(str[0::2])
print(str[::-1])
print("hmm..")
print(str[len(str)::-1])
print((str + " testing3")[::-1])