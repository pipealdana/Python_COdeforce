def palindrome ():
    j= int(input())
    

    while j>0:
        add= int(input())
        parseo=str(add)
        reverse= int(parseo[::-1])
        i= str(add + reverse)
        j=j-1
        
        if i == i[::-1]:
            print=(i, "Es un palindromo")
            break
        

            
        

if __name__ == "__main__":
    palindrome()
      

        




