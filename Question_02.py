## #Compound Interest Calculation in Python -1
# Input values
P, r, t = input().split()
P = int(P)
r = float(r)
t = int(t)
# Compound Interest formula
CI = (P * (1 + (r / 100)) ** t) - P
# Output rounded to 1 decimal place
print(round(CI, 1)) #Output =157.6