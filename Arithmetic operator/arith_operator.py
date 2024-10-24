def arithmetic_arranger(problems, show_result=False):
    # check the number of problems to be solved if more than five then return error
    if len(problems) > 5 :
        return 'Error: Too many problems'

    operators = ['+', '-']
    

    row1 = []
    row2 = []
    dashes = []
    answer = []  
    # Going through the problems to solve
    for problem in problems:
        each_arithmetic = problem.split()

        first_num, operator, second_num  = each_arithmetic

        # Check for operator + or -
        if operator not in operators:
            return 'Error: Operator must be "+" or "-" '
        # Check if the numbers contains only digit
        if not(first_num.isdigit() and second_num.isdigit()):
            return 'Error: Numbers must only be digit' 
        # Check if number on each side is more than 4 digit on each side i.e more than 1000
        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        #considering all information is correct 
        width = max(len(x) for x in each_arithmetic) + 1 

        spaces = " "
        dash = "_"

        # compute each line/row to rightly adjust and four spaces between each number
        row1.append(first_num.rjust(width)  + spaces*4 )
        row2.append(operator  + second_num.rjust(width - 1)  + spaces*4 )
        dashes.append(dash * width  + spaces*4 )
        result = str(eval(problem))
        answer.append(result.rjust(width)  + spaces*4 )

        # if result is set to true
        if show_result == True:
            arranged_problem = "".join(row1) + '\n' + "".join(row2) + '\n' + "".join(dashes) + '\n' + "".join(answer)

        else:
            arranged_problem = problems

    return arranged_problem

print(arithmetic_arranger( ["3801 - 2", "123 + 49", "130 + 500"], True)) 



    




