def arithmetic_arranger(problems, solve = False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    fl = ''
    sl = ''
    tl = ''

    if solve:
        ll = ''
        
    for l in range(len(problems)):
        sp = problems[l].split()

        if len(sp) != 3:
            quit()
        else:
            fo = sp[0]
            o = sp[1]
            so = sp[2]

        if not o == '+' and not o == '-':
            return 'Error: Operator must be \'+\' or \'-\'.'

        elif not fo.isdigit() or not so.isdigit():
            return 'Error: Numbers must only contain digits.'

        elif len(sp[0]) > 4 or len(sp[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        else:
            pl = (max(len(fo),len(so))+2)
            fl += (pl-len(fo)) * ' ' + fo + '    '
            sl += o + (pl-1-len(so)) * ' ' + so + '    '
            tl += pl * '-' + '    '

            if solve:
                if o == '+':
                    result = int(fo)+int(so)
                else:
                    result = int(fo)-int(so)
                ll += (pl-len(str(result))) * ' ' + str(result) + '    '

    arranged_problems=fl.rstrip() + '\n' + sl.rstrip() + '\n' + tl.rstrip()

    if solve:
        arranged_problems = fl.rstrip() + '\n' + sl.rstrip() + '\n' + tl.rstrip() + '\n' + ll.rstrip()
    return arranged_problems