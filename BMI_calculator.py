from re import A

#program, I first created functions to enter basic information

def  weightheight ():
    weight = float(input("Enter Your Weight: (Kg)"))
    size = float(input("Enter Your Height: (M)"))    
    return weight, size

#here I define the function that will calculate with the data I entered
def bmıcalculate(weight, size):
    return weight/(size*size)


#here I am creating a function to show my calculation

def bmıshow(bmi):
    print(" Your Body Mass Index = ",bmi)

    
# Finally here I define a main function that calls functions
def main():
    a,b = weightheight()
    bmi = bmıcalculate(a,b)
    bmıshow(bmi)
    
main()    
    