import math

radius = float(input("Enter the radius of the circle: "))
    
if radius < 0:
    print("Radius cannot be negative. Please enter a valid radius.")
else:
    # Calculate the area and circumference
     area = math.pi * radius ** 2
     circumference = 2 * math.pi * radius
        
     # Print out the results
     print(f"The area of the circle is: {area:.2f}")
     print(f"The circumference of the circle is: {circumference:.2f}")
        