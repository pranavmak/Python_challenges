def sum_to_int(N):
    sum = 0
    for i in range(1, N+1):
        sum+=1
    return sum

N_value = 10
result = sum_to_int(N_value)
print(f"The sum of integers from 1 to {N_value} is: {result}")
