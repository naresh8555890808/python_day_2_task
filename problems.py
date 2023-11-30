

print(" compound intrest")
# component intrest


# formula for component intrest

# A=p(1+r/n)**nt
#
#A	=	final amount
#P	=	initial principal balance
#r	=	interest rate
#n	=	number of times interest applied per time period
#t	=	number of time periods elapsed

n = int(input("Enter the principle amount:"))

rate = int(input("Enter the rate:"))

years = int(input("Enter the number of years:"))

for i in range(years):
    n = n + ((n * rate) / 100)

print(n)

#==============================================================================================================

print("simple intrest")

# simple intrest
# formula for simple intrest
# P*T*R/100

# p = money
# t = time
# r = rate
p = int(input("enter your money"))
t = int(input("enetr your time"))
r= int(input("enter your rate"))

simple_intrest = p*t*r/100
print(simple_intrest)

#===============================================================================================================
print("a+b**2 formula")

# (a+b)**2 problem

#formula = (a+b)**2

a = int(input("enter your number"))
b = int(input("enter your number"))

formula = (a+b)**2
print(formula)

