count=0
total=0

#mapped the words of the string to the coresponding number through a dictionary
x={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven":11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen":16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "sventy":70, "eighty":80, "ninety":90, "hundred":100, "thousand":1000, "lakh":100000,"corer":10000000}

#took a string as a input
str=input("enter a string you want to connnvert to a number: ")
a=str.split( )

#entered the wordes that are to be removed from the list
y=["hundred", "thousand", "lakh", "corer"]
for i in  y:
     if i in a :
          a.remove(i)

#gave the words their respective number
for i in range (0,len(a)):
     a[i]=x[a[i]]

print(a)
a.reverse()
print(a)

#the main loop which calculates the value
for i in range(0,len(a)):
     if i<2:
          count=count+a[i]
          print(count)
     if i==2:
          count=count+(a[i]*100)
          print(count)
     if i==3 or i==4:
          count=count+(a[i]*1000)
          print(count)
     if i==5 or i==6:
          count=count+(a[i]*100000)
          print(count)
     if i==7 or i==8:
          count=count+(a[i]*10000000)
          print(count)
     else:
          continue
total=count
print("the given number in the string is equal to ", total)