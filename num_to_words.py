#numbers to words
dict = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six"
    }
num = input("number: ")
ans =""
for i in num:
    #print(dict.get(i))
    ans = ans + str(dict.get(i,"-")) + " "
print(ans)

