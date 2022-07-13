from operator import truediv, xor


is_the_sky_blue = True
door_is_closed = False

print(is_the_sky_blue)

if is_the_sky_blue: 
    print("the sky is blue!")

if door_is_closed:
    print("door is closed!")
else:
    print("door is open!")

if is_the_sky_blue == door_is_closed:
    print('the sky is blue is equal to the door is closed')
else: 
    print('the sky is blue is not equal to the door is closed')

print(True)
print(not True)
print(not not True)
print(True and False)
print(not True and False)
print((not True) and False)
print(True and (not False))

if not is_the_sky_blue:
    print("the sky isn't blue!")
else:
    print("the sky is blue!")

print(True + True)
print(xor(True, False))
print(False + False)
print()