def fibonnaci(m):
    if m<=1:
        return m
    else:
        return(fibonnaci(m-1) + fibonnaci (m-2))
m=7
print("fibonnaci series:")
for i in range(m):
    print(fibonnaci(i),"+",end="")