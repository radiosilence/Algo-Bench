def factorial(x):
    #-------------------------------------------------
    #--- Code snippet from The Math Vault          ---
    #--- Calculate factorial (C) Arthur Smith 1999 ---
    #-------------------------------------------------
    result = str(1)
    i = 1 #Thanks Adam
    while i <= x:
        #result = result * i  #It's faster to use *=
        #result = str(result * result + i)
           #result = int(result *= i) #??????
        result = str(int(result) * i)
        #result = int(str(result) * i)
        i = i + 1
    return result
