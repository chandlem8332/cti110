# CTI-110
# P3HW1 - Debugging
# Michael Chandler 
# 6/26/2022
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59
    # TO DO: define the rest of the scores

    
    score = float(input('Please enter score: '))

    if score >= A_score:
        print('Grade is A')
    else:
        if score >= B_score:
            print('Grade is B')
        else:
            if score >= C_score:
                print('Grade is C')
            else:
                if score >= D_score:
                    print('Grade is D')
       

                else:
                    if score <= F_score:
                        print('Grade is F') # TO DO: finish this







# program start
main()
