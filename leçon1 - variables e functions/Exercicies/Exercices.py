def logical(x):
    if x == 1:
        return 1
    else:
        return(x + logical(x - 1))
    
result = logical(6)

print(result)

"""
 
    3 + logical( 3 - 1) = 3 + logical(2)
    x = 2
    2 == 1? =>false 

    2 + logical(1) = 3

    3 + 3 = 6

"""