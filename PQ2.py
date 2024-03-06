def Reverse(s: str):
    s.split()
    s=list(s)
    s=reversed(s)
    return ''.join(s)  

s=input("enter a sentence: ")    
sent=Reverse(s)
print(sent)
