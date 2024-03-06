#Reverse Words in a string

def Reverse(s: str):
    words=s.split()
    reversed_words=reversed(words)
    return ' '.join(reversed_words) 

st=input("enter a sentence: ")    
sent=Reverse(st)
print(sent)
