i=int(input('Enter 1 for temperature in Celsius: \n 2 for temperature in Fahrenheit '))
if(i==1):
 celsius = float(input('Enter temperature in Celsius: '))  
 fahrenheit = (celsius * 1.8) + 32  
 print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))
elif(i==2):
 Fahrenheit = float(input('Enter temperature in Fahrenheit: '))  
 celsius = (Fahrenheit - 32)/1.8
 print('%0.1f  Fahrenheit is equal to %0.1f degree celsius '%(fahrenheit,celsius))
else:
 print('Entered choice is invalid \n please select 1 or 2')
