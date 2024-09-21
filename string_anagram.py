str1=input("Enter string 1:")
str2=input("Enter string 2:")
if(len(str1)!=len(str2)):
    print("Not anagram")
else :
    if(sorted(str1)==sorted(str2)):
        print("Anagram")
    else:
        print("not anagram")    