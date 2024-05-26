Python program to find the area of a cube       # If Comment is not Commented using (# symbol) SyntaxError : invalid syntax occurs

import.math  # Syntax Error or Compilation Error: Invalid syntax   ( Import math) has to be used
len_cube = Int(input("Enter the Length of Cube : ")) #Compilation Error: NameError: name 'Int' is not defined
#Logical error : Instead of square (Math function is called for sqrt) formula : 6a^2 or 6*(a*a)
Area_Cube = 6 * math.sqrt(len_cube) ##Logical Error : Area_Cube = 6 *(len_cube * len_cube)  has to be used , math function is not needed
print("Area of Cube  ".format(Area_Cube)) #Logical Error : Missing {} bracked and hence no result is displayed
var_name =  10 / 0       # Runtime Error : ZeroDivisionError: division by zero
