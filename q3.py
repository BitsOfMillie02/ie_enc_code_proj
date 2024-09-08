def strornot(s):
    if s == s[::-1]:
        print('palindrome')
    else:
        print("not a palindrome")
        
s = input("enter a string : ")
strornot(s)


def swap(s):
    a=''
    for i in s:
        if i.isupper():
            a =a+ i.lower()
        if i.islower():
            a = a+ i.upper()
    print(a)       
s = input("enter a string:")
swap(s)
