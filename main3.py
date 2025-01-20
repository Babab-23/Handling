try:
    num1,num2=eval(input('enter to numbers,seperated by a comma:'))
    result=num1/num2
    print('result is',result)
#using multiple except block from different type of error
except ZeroDivisionError:
    print('division by zero is error!!')
except SyntaxError:
    print('comma is missing.Enter  numbers  seperated by comma like this 1,2')
except:
    print('wrong input')
else:
    print('no exceptions')
finally:
    print('this will execute no matter what')