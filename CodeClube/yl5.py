number = 200000
status=False
counter=0

while(True):
    for i in range(20, 0,-1):
        if number%i==0:
            status=True
        else:
            status=False
            counter+=1
            break
    if status==True and counter==0:
        print("Vastus "+str(number))
        break
    counter=0
    print(number)
    number+=20