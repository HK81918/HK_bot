import random
import time
guess_num=random.randrange(1,10)
start=0
end=5
u=5
print('''U have in total 5 chance''')
time.sleep(0.5)
while start<end:
    u=u-1
    time.sleep(0.5)
    i = int(input("Guess a number between 0-10:-"))
    if(i!=guess_num):
        start = start + 1
        if (i > 10 or i==0 or i==10 or i<0):
            start = start - 1
            u = u + 1
            time.sleep(0.5)
            print("""
          WARNING:-

Please enter a number between 1-10
"""+"U have "+str(u)+" chances left")
        if(start<5):
            time.sleep(0.5)
            print('''Give one more try
            ''')
            if(u<5):
              time.sleep(0.5)
              print("You have "+str(u)+" chances left")
        if(start==end):
            time.sleep(0.5)
            print("""
Sorry! You failed""")
            print("The number was:- "+str(guess_num))
            time.sleep(0.5)

    else:
        time.sleep(0.5)
        print("Wow! you guessed it right the "+str(start+1)+" time")
        time.sleep(0.5)
        break
