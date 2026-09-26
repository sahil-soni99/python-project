b=5000
p=1234
w="W"
w="D"
while True:

    for c in range(3):

        c+=1
        pin=int(input("ENTER PIN : "))

        if pin==p:
            print("Correct Pin")
            print("Your Balance is:",b,end='\n\n')
            print("`Press W For Withdraw or Press D for Deposite`")
            w=input("")
            if w=="W":
                a=int(input("Enter Amount:"))
                if a<=b:
                    b=b-a
                    print("Transction Succecfully")
                    print("Current Balance is:",b)
        
                else:
                    print("Insufficiant Balance")
                    print("Your Balance is:",b)
                    # break
        

            elif w=="D":
                x=int(input("Enter Amount:"))
                b=b+x
                print("Deposit Successfully")
                print("Current Balance is:",b)

            else:
                print("Wrong Key")
                print("Re-",end="")
            break


        elif c==2:
            print("Incorrect Pin\n")
            print("LAST ATTEMPT\n")

        else:
            print("Incorrect Pin\n")

    else:
        print("ACCOUNT FREEZE\n")
        break
