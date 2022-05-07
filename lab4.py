"""
11. Формируется матрица F следующим образом: если в С сумма чисел  в нечетных столбцах в области 2 больше, чем произведение чисел в четных строках в области 1,
то поменять в С симметрично области 2 и 3 местами,иначе Е и В поменять местами несимметрично.При этом матрица А не меняется. После чего вычисляется выражение:
(К*A)*А– (K * AT). Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random
import time

def print_matrix(M,matr_name,tt):
        print ( "матрица "+matr_name+" промежуточное время = " +str(format(tt, '0.2f'))+ " seconds.")
        for i in M:            # делаем перебор всех строк матрицы
            for j in i:     # перебираем все элементы в строке 
                print("%5d" % j, end = ' ')
            print() 
  
print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q>100:
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))    
    K = int(input("Введите число К="))
    start = time.time()
    A,F,AA,AT = [],[],[],[]       # задаем матрицы 
    for i in range(row_q):
        A.append([0]*row_q)
        F.append([0]*row_q)
        AA.append([0]*row_q)
        AT.append([0]*row_q)        
    time_next = time.time()
    print_matrix(F,"F",time_next-start)

    for i in range(row_q):        # заполняем матрицу А         
        for j in range(row_q):
                A[i][j] = random.randint(-10,10)
                      
    time_prev = time_next
    time_next = time.time()
    print_matrix(A,"A",time_next-time_prev)
    for i in range(row_q):        # F
        for j in range(row_q):
            F[i][j] = A[i][j]    
    time_prev = time_next
    time_next = time.time()
    print_matrix(F,"F",time_next-time_prev)

     
    C = []                        # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):         # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[size + row_q % 2 + i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)


    # обработка матрицы C


    summa = 0

    proizv = 1
    
    for i in range(size):          
        for j in range(i+1,size,1):            
            if j < size-1-i and i % 2 == 1:
                proizv *= C[i][j]
            elif j > size-1-i and j % 2 == 0:
                summa += C[i][j]

    print("Сумма = ", summa)
    print("Произведение = ", proizv)
                
    #формируем F по условию


    if summa > proizv:
        for i in range(size + row_q % 2 + 1,row_q ,1):
                for j in range(size + row_q % 2 + 1,row_q,1):
                        if (i-size-row_q%2)>(j-size-row_q%2) and (i-size-row_q%2) > size - (j-size-row_q%2) - 1:
                                buffer = F[i][j]
                                F[i][j] = F[j][i]
                                F[j][i] = buffer                                        
    else:
        for i in range(size):
                for j in range(size):
                        buffer = F[i][j]
                        F[i][j] = F[i + row_q %2 + size][j]
                        F[i + raw_q %2 + size][j] = buffer
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "Измененная F", time_next - time_prev)   

    #(К*A)*А – (K * AT)

    print_matrix(A,"A",0)


    for i in range(row_q):      # AT
        for j in range(i,row_q,1):
            AT[i][j],AT[j][i] = A[j][i],A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT,"A^T",time_next-time_prev)


    for i in range(row_q):      # K * AT
        for j in range(row_q):
            AT[i][j] = K*AT[i][j]    
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT,"K*AT",time_next-time_prev)


    for i in range(row_q):      # A*A
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s=s+ A[i][m] * A[m][j]
            AA[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(AA,"A*A",time_next-time_prev)


    for i in range(row_q):      # K*AA
        for j in range(row_q):
            AA[i][j] = K*AA[i][j]    
    time_prev = time_next
    time_next = time.time()
    print_matrix(AA,"K*A*A",time_next-time_prev)


    for i in range(row_q):      # (К*A)*А – (K * AT)
        for j in range(row_q):
            AA[i][j] = AA[i][j]-AT[i][j]    
    time_prev = time_next
    time_next = time.time()
    print_matrix(AA,"(К*A)*А – (K * AT)",time_next-time_prev)        
    
    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")


except ValueError:
        print("\nэто не число, перезапустите программу и повторите попытку") 
