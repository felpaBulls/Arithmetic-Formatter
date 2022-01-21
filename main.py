import re


def arithmetic_arranger(listaNum, results=False):
    if len(listaNum) > 5:  # detecta error 1
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems

    for elem in listaNum:  # detecta error 2
        if '/' in elem:
            arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
            return arranged_problems


        if '*' in elem:
            arranged_problems = 'Error: Operator must be \'+\' or \'-\''
            return arranged_problems

        if re.search('[a-zA-Z]', elem):  # detecta error 3
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems

    num_sup = list()
    op = list()
    num_inf = list()

    for elem in listaNum:
        num_sup.append(re.findall('([0-9]+)\s', elem))
        op.append(re.findall(r'[-\+]', elem))
        num_inf.append(re.findall('\s([0-9]+)', elem))

    num_sup_S = list()
    op_S = list()
    num_inf_S = list()

    for i in range(len(listaNum)):  # convierte en listas de strings
        num_sup_S.append(num_sup[i][0])
        op_S.append(op[i][0])
        num_inf_S.append(num_inf[i][0])

    for i in range(len(listaNum)):  # detecta error 4
        if len(num_sup_S[i]) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems
        if len(num_inf_S[i]) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems

    results_I = list()

    if results:  # cuando True, suma o resta ambos números
        for i in range(len(listaNum)):
            if op_S[i] == '+':
                results_I.append(int(num_sup_S[i]) + int(num_inf_S[i]))
            elif op_S[i] == '-':
                results_I.append(int(num_sup_S[i]) - int(num_inf_S[i]))

    fila_sup = list()
    fila_inf = list()
    fila_dashes = list()
    fila_results = list()

    def agreg_espacios(nro_espacios):
        str1 = ''
        for i in range(nro_espacios):
            str1 = str1 + ' '
        return str1

    def espacios_resultado(num1, num2, r):
        str2 = ''
        if len(r) > len(num1) and len(r) > len(num2):
            str2 = ' '
        else:
            str2 = '  ' + agreg_espacios(len(num1) - len(r))
        return str2

    for i in range(len(listaNum)):
        if len(num_sup_S[i]) > len(num_inf_S[i]):
            fila_sup.append('  ' + num_sup_S[i])
            fila_inf.append(op_S[i] + ' ' + agreg_espacios(len(num_sup_S[i]) - len(num_inf_S[i])) + num_inf_S[i])

        else:
            fila_sup.append('  ' + agreg_espacios(len(num_inf_S[i]) - len(num_sup_S[i])) + num_sup_S[i])
            fila_inf.append(op_S[i] + ' ' + num_inf_S[i])

        fila_dashes.append('')

        for j in range(len(fila_sup[i])):
            fila_dashes[i] = fila_dashes[i] + '-'

        if results:
            fila_results.append(espacios_resultado(num_sup_S[i], num_inf_S[i], str(results_I[i])) + str(results_I[i]))

    if len(fila_sup) == 1:
        arranged_problems = fila_sup[0]+ '\n' + fila_inf[0] +'\n' + fila_dashes[0]
        if results:
            arranged_problems = arranged_problems + '\n' + fila_results[0]

    elif len(fila_sup) == 2:
        arranged_problems = fila_sup[0] + '    ' + fila_sup[1] + '\n' + fila_inf[0] + '    ' + fila_inf[1] + '\n' + \
                            fila_dashes[0] + '    ' + fila_dashes[1]
        if results: arranged_problems = arranged_problems + '\n' + fila_results[0] + '    ' + fila_results[1]

    elif len(fila_sup) == 3:
        arranged_problems = fila_sup[0] + '    ' + fila_sup[1] + '    ' + fila_sup[2] + '\n' + fila_inf[0] + '    ' +\
                            fila_inf[1] + '    ' + fila_inf[2] + '\n' + fila_dashes[0] + '    ' + fila_dashes[1] +\
                            '    ' + fila_dashes[2]
        if results: arranged_problems = arranged_problems + '\n' + fila_results[0] + '    ' + fila_results[1] + '    ' +\
                                        fila_results[2]

    elif len(fila_sup) == 4:
        arranged_problems = fila_sup[0] + '    ' + fila_sup[1] + '    ' + fila_sup[2] + '    ' + fila_sup[3]+ '\n' +\
                            fila_inf[0] + '    ' + fila_inf[1] + '    ' + fila_inf[2] + '    ' + fila_inf[3]+ '\n' +\
                            fila_dashes[0] + '    ' + fila_dashes[1] +'    ' + fila_dashes[2] + '    ' + fila_dashes[3]
        if results:
            arranged_problems = arranged_problems + '\n' + fila_results[0] + '    ' + fila_results[1] + '    ' + fila_results[2] + '    ' + fila_results[3]

    elif len(fila_sup) == 5:
        arranged_problems = fila_sup[0] + '    ' + fila_sup[1] + '    ' + fila_sup[2] + '    ' + fila_sup[3] + '    ' + fila_sup[4]+ '\n' + \
                            fila_inf[0] + '    ' + fila_inf[1] + '    ' + fila_inf[2] + '    ' + fila_inf[3] + '    ' + fila_inf[4] + '\n' +\
                            fila_dashes[0] + '    ' + fila_dashes[1] + '    ' + fila_dashes[2] + '    ' + fila_dashes[3] + '    ' + fila_dashes[4]
        if results: arranged_problems = arranged_problems + '\n' + fila_results[0] + '    ' + fila_results[1] + '    ' + fila_results[2] + '    ' + fila_results[3] + '    ' + fila_results[4]

    return arranged_problems


print(arithmetic_arranger(['3801 / 2', '123 + 49']))
