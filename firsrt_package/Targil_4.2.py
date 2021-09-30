num=int(input("enter a nunber"))
for n in range(2,num):
    if(num%n==0):
        print("the number is not rishoni")
        break
ggg=0
for i in  range(2,num):


    if(num%i!=0):
      ggg+=1

if(ggg==(num-2)):
    print("the number is rishoni")




