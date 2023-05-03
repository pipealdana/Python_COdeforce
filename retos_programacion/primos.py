def primos():
    aux=0
    
    for i in range (2, 10000):
            if (i%2!=0 or i==2) and (i%3!=0 or i==3) and (i%5!=0 or i==5) and (i%7!=0 or i==7) and (i%11!=0 or i==11) and (i%13!=0 or i==13) and (i%17!=0 or i==17) and (i%19!=0 or i==19) and (i%23!=0 or i==23):             
                print(i)
                aux+=1
                if (aux==100):
                     break
                
                                    
if __name__=="__main__":
   primos()