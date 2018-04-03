#BRIANNE KELLY R. OLLOS
#MIDTERM

def match_a():
    print ("Function match_a() \n")

    ko1 = input("Enter 1st input:")
    ko2 = input("Enter 2nd input:")
    ko3 = input("Enter 3rd input:")

    ko22 = []
    ko33 = []
    ko11 = []

    for i in ko1:
        if len(i) != 1:
            if i == i[::-1]:
                ko11.append(i)

    for i in ko2:
        if len(i) != 1:
            if i == i[::-1]:
                ko22.append(i)

    for i in ko3:
        if len(i) != 1:
            if i == i[::-1]: 
               ko33.append(i)

    print ("1st output: ", len(ko11))
    print("2nd output: ", len(ko22))
    print ("3rd output: ", len(ko33))


match_a()
print ("\n\n")


def front_x():
    print ("Function front_x()\n")

    ko1 = input("Enter 1st input:")
    ko2 = input("Enter 2nd input:")
    ko3 = input("Enter 3rd input:")

    ko11 = []
    ko111 = []
    ko22 = []
    ko222 = []
    ko33 = []
    ko333 = []

    for i in ko1:
        if i.startswith('x'): 
            ko11.append(i)
        else:
            ko111.append(i) 

    print ("1st output: ", sorted(ko11) + sorted(ko111)) 

    for i in ko2:
        if i.startswith('x'): 
            ko22.append(i)
        else:
            ko222.append(i)  

    print ("2nd output: ", sorted(ko22) + sorted(ko222)) 

    for i in ko3:
        if i.startswith('x'): 
            ko33.append(i)
        else:
            ko333.append(i)  

    print ("3rd output: ", sorted(ko33) + sorted(ko333)) 


front_x()
