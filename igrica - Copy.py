import random
slucajni = random.randint(1,10)
broj=int(input("unesi broj:"))
broj=0
pokusaj=0
while(broj!=slucajni):
 broj=int(input())
 if (broj<slucajni):
    print("broj je manji od zamisljenog,unesite ponovo")
 elif (broj>slucajni):
   print("broj je veci od zamisljenog,unesite ponovo")
   pokusaj+=1
 else:
   print("pogodili ste broj iz ",pokusaj+1,"put")
   break
 print("broj pokusaja je: " ,pokusaj)
 
 
 

 
   

    
