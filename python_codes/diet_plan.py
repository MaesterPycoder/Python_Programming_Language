import time
dos={1:"Food",2:"Excercise"}
def note_data(ch):
    if ch==1:
        with open("diet_plan.txt","a") as f1:
            while True:
                item=input("Enter Food_Item:")
                f1.write(str(time.ctime()))
                f1.write("\n"+item+"\n")
                f1.write("-"*100+"\n")
                ag=input("Enter another if Yes enter 'yes' , not enter 'no':").lower()
                if ag=="no":
                    break
    else:
        with open("Excerise_plan.txt","a") as f2:
            while True:
                item=input("Enter Excercise:")
                f2.write(str(time.ctime()))
                f2.write("\n"+item+"\n")
                f2.write("-"*100+"\n")
                ag=input("Enter another if Yes enter 'yes' , not enter 'no':").lower()
                if ag=="no":
                    break
if __name__=='__main__':
    try:
        print("Welcome Shanmukkha,")
        for ele in dos:
            print(ele,":",dos[ele])
        ch=int(input("Enter option:"))
        if ch==1 or ch==2:
            note_data(ch)
            print("Succusfully Noted.")
        else:
            raise Exception
    except Exception as e:
        e=print("Invalid Input.")
    finally:
        print("----Thank You \
                Have a nice day")
