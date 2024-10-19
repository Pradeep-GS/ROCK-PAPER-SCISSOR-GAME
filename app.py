import random
print("WELCOME TO THE GAME")
print("ROCK=R","PAPER=P","SCISSOR=S")
n=int(input("ENTER HOW MANY TIME YOU WANT TO PLAY (ONLY ODD):"))
opt=["R","S","P"]
check=["R","S","P","r","s","p"]
sys=0 #SYSTEM INITIAL SCORE
use=0 #USER INITIAL SCORE
i=1
if (n%2==0):
    print("PLEASE ENT ODD NUMBER!!!!")
else:
    while i<=n:
        use_ip=input("ENTER YOUR OPTION R,S,P:")
        if use_ip not in check:
             print("WRONG INPUT")
             break
        else:
            sys_opt=random.choice(opt)
            print("SYSTEM INPUT:",sys_opt)
            #USER SCORE INCREMENT
            if((use_ip=="P" and sys_opt=="R")or
                (use_ip=="R" and sys_opt=="S") or
                (use_ip=="S" and sys_opt=="P") or
                (use_ip=="p" and sys_opt=="R")or
                (use_ip=="r" and sys_opt=="S") or
                (use_ip=="s" and sys_opt=="P") ):
                use+=1
            #SYSTEM SCORE INCREMENT
            elif((use_ip=="P" and sys_opt=="S")or
                (use_ip=="R" and sys_opt=="P") or
                (use_ip=="S" and sys_opt=="R") or
                (use_ip=="p" and sys_opt=="S")or
                (use_ip=="r" and sys_opt=="P") or
                (use_ip=="s" and sys_opt=="R") ):
                 sys+=1
            else:
                 pass
        i+=1
print("------------------------------------------------------------------------------------------")
if use>sys: #USER WIN
    print("YOU WIN:",use)
    print("SYSTEM SCORE:",sys)
elif sys>use: #SYSTEM WIN
    print("SYSTEM WIN:",sys)
    print("YOUR SCORE:",use)
else:
    print("YOUR SCORE:",use)
    print("SYSTEM SCORE:",sys)