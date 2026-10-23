def number_pattern(n):
    nump=""
    if not(isinstance(n,int)):
        return "Argument must be an integer value."
    if n<1:
        return "Argument must be an integer greater than 0."
    for i in range(1,n+1):
        nump+=str(i)+" "
    return nump.strip() 
print(number_pattern("4"))
print(number_pattern(0))
print(number_pattern(4))
print(number_pattern(12))