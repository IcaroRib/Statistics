def sum_ranks(n):
    summation = 0  
    for i in range(1,n+1):
        summation +=i
    return summation


def sum_ranks_v2(n):
    return (n * (n+1))/2
       

def sum_lines(k, n):
    return k * sum_ranks_v2(n)


def expected_value(k, n):
    return sum_lines(k,n) / n


def sum_column(R, n, j):
    R_j = 0
    for i in range(n):
        R_j += R[i][j]
    return R_j


def sampling_distribution(k, n, R):
    summation = 0
    E_Rj = expected_value(k, n)
    for j in range(n):
        R_j = sum_column(R, n, j)
        summation += (R_j - E_Rj) ** 2
    return summation


def avg_variance(k, n, R):
    summation = 0
    for i in range (k):
        for j in range(n):
            summation += R[i][j]/(n*k)
    return summation


def avg_variance_v2(n):
    return (n+1)/2


def squared_deviations(k, n, R):
    summation = 0
    r_hat = avg_variance_v2(n)
    for i in range(k):
        for j in range(n):
            summation += (R[i][j] - r_hat) ** 2
    return summation


def squared_deviations_v2(k, n):
    summation = 0 
    for j in range(1, n+1):
        summation += j - ((n+1)/2)**2
    return summation


def squared_deviations_v3(k, n):
    return (k * n) * ((n**2 - 1) / 12)


def friedmand_statistic(k, n, R):
    return ((n-1) * sampling_distribution(k, n, R)) / squared_deviations_v3(k, n)
        

def friedmand_statistic_v2(k, n, R):
    summation = 0
    for j in range(n):
        summation += sum_column(R, n, j) ** 2
    Q = 12 / (k*n*(n+1))
    Q = Q * summation
    Q -= 3 * k * (n+1)
    return Q
    
def friedmand_statistic_v3(k, n, R):
    summation = 0
    for j in range(n):
        summation += R[j] ** 2
    Q = 12 / (k*n*(n+1))
    Q = Q * summation
    Q -= 3 * k * (n+1)
    return Q

k = 5
n = 4
R = [[1,2,3,4],[4,3,2,1],[1,3,2,4],[4,2,3,1],[2,1,3,4]]
print(friedmand_statistic(k, n, R))
print(friedmand_statistic_v2(k, n, R))


R = [[4,2,3,1],[1,3,2,4],[4,3,2,1],[4,2,3,1],[4,1,3,2]]
print(friedmand_statistic(k, n, R))
print(friedmand_statistic_v2(k, n, R))


R = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print(friedmand_statistic(k, n, R))
print(friedmand_statistic_v2(k, n, R))

