def decimaltobinary(n):
    if n == 0:
        return "0"
    
    binarystring = ""
    while n > 0:
        remainder = n % 2
        binarystring = str(remainder) + binarystring
        n = n // 2
        
    return binarystring

print("decimal_to_binary(10) ->", decimaltobinary(10))
print("decimal_to_binary(25) ->", decimaltobinary(25))
