# we ar doing conditonals
# if statement
a= 33
b= 200
if b>a:
    print("b is greater than a")
    # the elif statement
    a = 33
    b = 33
    if b>a:
        print("b is greater than a")
    elif a == b:
        print("a and be are equal")
    # else statement
        a= 200
        b= 33
        if b>a:
            print("b is greater than a")
        elif a == b:
           print("a and b are the same")
        else:
            print("a is greater than b")

    # else statement without elif statement
            a= 200
            b= 33
            if b>a:
                print("b is greater a")
            else:
                print("b is not gretaer than a")
    # using the AND keyword
                a == 200
                b= 33
                c= 500
                if a>b and c>a:
                    print("both conditons are true")
    # or keyword 
                    if a>b or a>c:
                        print("at least one of the condions is true")

    # loops
    #examples of while loops
          #  print i as long as i is less than 6
                        i= 1
                        while i<6:
                            print(i)
                            i +=1
        count = 1
        while count <=5:
            print(count)
            count+=1
    # eixt the loop when i is 3:
            while i<6:
                print(i)
                if i ==3:
                    break
                i+=1
                # for loop 
    # print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)  
    # brak statement
    if x == "banana": 
    
    # continue part
       continue
print(x)
         # range function
for x in range(6):
    print(x)   
