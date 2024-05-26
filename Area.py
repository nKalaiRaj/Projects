#Import math function
import math
#Request the user to enter shape of the building
shape = input("Enter the shape of the building 'square,rectangular or round': ")
#If the shape is square, request user length of square
if shape == "square":
    dim_len = int(input("Enter the lenght of square : "))
    dim = dim_len*dim_len   #Calculate area of square
    print(f"Area of the square is : {dim}")
#elif the shape is rectangle, request user length and width of rectangle    
elif shape == "rectangular":
    dim_len = int(input("Enter the length of rectangle : "))
    dim_width = int(input("Enter the width of rectangle : "))
    dim = dim_len * dim_width #Calculate area of rectangle
    print(f"Area of the rectangle is : {dim}")
#elif the shape is round, request user radius of circle     
elif shape == 'round':
    dim_radius = int(input("Enter the radius of the circle : "))
    dim = math.pi*dim_radius*dim_radius #Calculate area of Circle
    print(f"Area of the Circle is : {dim}")
