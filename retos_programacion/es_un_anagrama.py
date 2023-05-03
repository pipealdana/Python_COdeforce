def anagrama():
    a= input("")
    b= input("")
    if len (a) == len(b):
        if sorted (a) == sorted (b):
         print ("la palabra", a, "y la palabra", b, "son anagramas")      
    else:
       print("la palabra", a, "y la palabra", b, "no son anagramas")
       
if __name__=="__main__":
   anagrama()
   