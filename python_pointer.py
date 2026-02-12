num1=12
num2=num1

print('Before num2 change:')
print('num1:', num1)
print('num2:', num2)

print('Memory address of num1:', id(num1))
print('Memory address of num2:', id(num2))

num2=20
print('After num2 change:')
print('num1:', num1)        
print('num2:', num2)
print('Memory address of num1:', id(num1))
print('Memory address of num2:', id(num2))