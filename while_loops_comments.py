my_list = [3, 8, 23, 18, 83, 48]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

j = 0;
while j < len(my_list):
    print(my_list[j::1]) #im an inline comment
    j += 1

#im an entire line comment

'''
This is a multi-line comment!
This will make an infinite loop:
i = 1
while i:
    print("I'm stuck in an infinite loop!") 
'''
