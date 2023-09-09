def factrec(n):
 if n==0 or n==1:
    return True
 else:
  return n*factrec(n-1)
number=int(input("Enter a value:"))
res=factrec(number)
print("The factorial of {} is {}.".format(number,res))