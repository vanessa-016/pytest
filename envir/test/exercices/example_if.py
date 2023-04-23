a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b)


a = 24
b = 44
if a <= 0:
    print(a)
print(b)


##### if an else
a = 93
b = 27
if a >= b:
    print(a)


a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)


if test_expression:
    # statement(s) to be run
#else:
    # statement(s) to be run    



###elif 

#a = 93
#b = 27
#if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")    

if test_expression:
    # statement(s) to be run
#elif test_expression:
    # statement(s) to be run
    

#if test_expression:
    # statement(s) to be run
#elif test_expression:
    # statement(s) to be run
#elif test_expression:
    # statement(s) to be run
#else:
    # statement(s) to be run

#### combinados

#a = 93
#b = 27
#if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")



#### anidados
# 
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")


###  or

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)


### and
a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)    