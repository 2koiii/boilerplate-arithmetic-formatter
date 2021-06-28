def arithmetic_arranger(problems, show_results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ''
    second_line = ''
    third_line = ''

    if show_results:
        fourth_line = ''

    for problem_count in range(len(problems)):
        problem_list = problems[problem_count].split()

        if len(problem_list) != 3:
            quit()
        else:
            first_operand = problem_list[0]
            operator = problem_list[1]
            second_operand = problem_list[2]

        if not operator == '+' and not operator == '-':
            return "Error: Operator must be '+' or '-'."
        elif len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        else:
            problem_length = (max(len(first_operand),len(second_operand))+2)
            first_line += (problem_length-len(first_operand)) * ' ' + first_operand + '    '
            second_line += operator + (problem_length-1-len(second_operand)) * ' ' + second_operand + '    '
            third_line += problem_length * '-' + '    '

            if show_results:

                if operator == '+':
                    result = int(first_operand)+int(second_operand)
                else:
                    result = int(first_operand)-int(second_operand)
                fourth_line += (problem_length-len(str(result))) * ' ' + str(result) + '    '

    arranged_problems=first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()

    if show_results:
        arranged_problems=first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip() + '\n' + fourth_line.rstrip()
    return arranged_problems