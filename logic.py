#Python program to Display Logic Error
#Finding the perimeter of a rectangle
Len_rec = int(input("Enter the Length of the rectangle: ")) #Request the user to enter Length of Rectangle
width_rec = int(input("Enter the Width of the rectangle: "))#Request the user to enter Width of Rectangle
perimeter_of_rec = 2*Len_rec+width_rec # Logical Error has occured .. Missing brackets as the formula is : 2 (L + W)
print(f"Perimeter of Rectangle : {perimeter_of_rec}") #Display the output