            # # Example;  
            # #Input
            # You do not need to take any input.
            # Output
            # Print the date and time in the mentioned format using the already defined variables.
            # Example
            # Output:Date:2025-05-25,Time:14:30:00


                        #kuch importent misteck
            # a, b, c = 2025, 05, 25
            # x, y, z = 14, 30, 00
            # print(a, b, c, sep="-", end=",")
            # print(x, y, z, sep="-")
            #output {they give a SyntaxError}
    # Problem in your code:
        #In Python 3, numbers with a leading zero like 05 or 00 are not allowed (they give a SyntaxError).
        #✅ Instead, just write them normally as 5 and 0.

a, b, c = 2025, 5, 25
x, y, z = 14, 30, 0
print(a, b, c, sep="-", end=",")
print(x, y, z, sep="-")
# Output:Date:2025-05-25,Time:14:30:00

#end the code


