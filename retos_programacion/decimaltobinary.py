def convertDecimaltoBinary():
    n = int(input())
    ans = ""
    while (n > 0):
        if (n%2==0): ans+="0"
        else: ans+="1"
        n = n/2
    print(ans)

if __name__ == "__main__":
    convertDecimaltoBinary()