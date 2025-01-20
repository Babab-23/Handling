valid=False
while not valid: #using nested while loop
   try:
      n=int(input('enter your number:'))
      #enter an even number
      while n%2==0:
         print('bye')
         valid=True
   except ValueError:
      print('invalid')