my_1=5
my_2=10

print("Sum is", my_1+my_2)

if(my_1 > my_2):
    print("Difference is", my_1-my_2)
    print("second line in the if condtion --- my_1 is greater than my_2")
else:
    print("second line in the if condtion --- my_1 is smllaer than my_2")
    print("Difference is", my_2-my_1)




print("Prod is", my_1*my_2)

if ( my_1 > my_2):
   print("Quotioent is", my_1/my_2)
else:
   print("Quotioent is", my_2/my_1)

   def square(a,b):
       return(a*a -b*b)
   for i in range(10):
       i1=10
       print("value of a is", i1,"value of b is", i,"and the square of a - square of b is", square(i1,i))
      # print("value of b is", i)
       #print("and the square of a - square of b is", square(i1,i))
