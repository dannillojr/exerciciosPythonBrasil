
fib = [0 , 1]

while True:

    fib.append(fib[-1] + fib[-2])

    if fib[-1] > 500:
        print(fib)
        break 
