from sympy import symbols
x,y = symbols('x,y')
def binomial_exp(x,y,e):
    if e == 0:              #Pascal series last values calculator start
        return [1]
    List_1 = [1, 1]
    if e == 1:
        return x+y

    for i in range(e - 1):
        List_bi = [1]
        for j in range(len(List_1) - 1):
            add = List_1[j] + List_1[j + 1]
            List_bi.append(add)
        List_bi.append(1)
        List_1 = List_bi        #Pascal series last values calculator end, basically calculate all the coefficient values


    L1 = []                     #Variable calculator starts
    L2 = []
    for i in range(e + 1):
        L1.append(x ** i)
    for j in range(e, -1, -1):
        L2.append(y ** j)
    final_list=[]
    for i in range(len(L2)):
        final_list.append(L1[i]*L2[i]*List_bi[i])
    sum =0                      #Variable calculator ends
    for i in final_list:        #List to int conversion
        sum+=i
    return sum


print(binomial_exp(2*x,3*y,9))