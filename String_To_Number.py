x={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven":11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen":16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "sventy":70, "eighty":80, "ninety":90, "hundred":100, "thousand":1000, "lakh":100000,"corer":10000000}

str=input("enter a string you want to connnvert to a number: ")

def num_to_words(str):
     str=str.lower()
     str=str.split(" ")
     total = 0
     current = 0

     for  i in range(len(str)):
          if str[i] in x:
               value=x[str[i]]
               if value < 100:
                    current=current+value
               else :
                    current=current*value
          else:
               continue #will ignore any misspelled word
     total = total + current
     print ("the converted number is ", total)
num_to_words(str)