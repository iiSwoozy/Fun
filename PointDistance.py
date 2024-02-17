import math

def calculate_d(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance


def main():
    x1 = int(input("Enter the x value of the first point: "))
    y1 = int(input("Enter the y value of the first point: "))
    x2 = int(input("Enter the x value of the second point: "))
    y2 = int(input("Enter the y value of the second point: "))
    
    distance = calculate_d(x1, y1, x2, y2)
    distance_rounded = round (distance, 2)
    print("The distnace between" , (x1, y1) , "and" , (x2, y2) , "is: " , distance_rounded)
    

main()
    
