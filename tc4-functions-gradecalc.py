############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Zachary Rudolf

# main() FUNCTION
def main():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")

    numericGrade = 0.0
    letterGrade= ""
    modifier=0.0
    classes=["PROG 1700", "NETW1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1007"]
    grades=[]
    #Gather user inputs 
    def gradeCalc():
    # Determine base numeric value of the grade
        if letterGrade == "A":
            numericGrade = 4.0
        elif letterGrade == "B":
            numericGrade = 3.0
        elif letterGrade == "C":
            numericGrade = 2.0
        elif letterGrade == "D":
            numericGrade = 1.0
        elif letterGrade == "F":
            numericGrade = 0.0
        else:
            #If an invalid entry is made
            print("You entered an invalid letter grade.")
        
        # Determine whether to apply a modifier
        if modifier == "+":
            if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
                numericGrade += 0.3
        elif modifier == "-":
            if letterGrade != "F":     # Minus is not valid on F
                numericGrade -= 0.3 
        return numericGrade
    
    def getLetter():
        validGrade=False 
        while validGrade==False:
            letterGrade=input("\nPlease enter a letter grade for {0}: ".format(classes[i])).upper()
            if letterGrade=="A" or letterGrade=="B" or letterGrade=="C" or letterGrade=="D" or letterGrade=="F": 
                validGrade==True
                return letterGrade
            else: 
                print("This is not a valid grade entry, try again.")
                validGrade==False
    def getMod():
        validMod=False 
        while validMod==False:
            modifier=input("Please enter a modifier (+, - or nothing) : ")
            if modifier=="-" or modifier=="+" or modifier=="": 
                validMod==True
                return modifier
            else: 
                print("This is not a valid modifier entry, try again.") 
                validMod==False

    for i in range(0, len(classes)):
        letterGrade=getLetter()
        modifier=getMod()
        numericGrade= gradeCalc()
        grades.insert(i, numericGrade)  


    # Output final message and result, with formatting
    print("\n****************************************\n")

    for i in range(0, len(classes)):
        print("The numeric value for {0} is: {1:.1f}".format(classes[i], grades[i])) 

    def gpaCalc():
        gradeTotal=(sum(grades))
        gpa=gradeTotal/(len(classes))
        return gpa  
    
   
    gpa=gpaCalc()
    print("==================================================")
    print("Your grade point average for the semester is: {0:.1f}".format(gpa))
    print("==================================================") 

#PROGRAM EXECUTION STARTS HERE
main()