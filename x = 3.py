x = 3
if x+5 > x**2 or x % 4 != 0:
        print("This comparison is True")

number = 6
if number * 2 < 14:
        print(number * 6 % 3)
elif number > 7:
        print(100 / number)
else:
        print(7 - number)

def get_remainder(x, y):
 
  if x == 0 or y == 0 or x ==y:
    remainder = 0
  else:
    remainder = (x % y) / y
  return remainder


print(get_remainder(10, 3))        

7 < "number"
test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)

def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))    

x = 5*2

((10 != x) or (10 > x))

def clothing_type(temp):
    if clothing_type > 65:
        clothing = "T-Shirt"
    elif clothing_type > 50:
        clothing = "Sweatshirt"
    elif clothing_type >= 65:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat

def clothing_type(temp):
    if (temp > 65):
        clothing = "T-Shirt"
    elif (temp > 50 or (temp) > 65):
        clothing = "Sweatshirt"
    elif (temp > 32 or (temp) > 50):
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat

x =   0
while x < 20:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)

def matrix(initial_number, end_of_first_row):
  n1= initial_number
  n2= end_of_first_row+1
  for column in range(n1, n2):
    for row in range(n1, n2):
        print(column*row, end=" ")
    print()

matrix(1, 4)

def x_figure(salary):
    tally = 0
    if salary == 0:
        tally += 1
    while salary >= 1:
        salary = salary/10
        tally += 1
    return tally
print("Your overpaid salary is a " + str(x_figure(230000)) + "-figure sum.")
