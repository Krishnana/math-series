def sum_series(n,x,y):
    """
    Description : This method provides sum of series based on first 2 values provided
    Argument    : n --> Provide a number for which you need lucas value
                  x --> first value in the series
                  y --> second value in the series
    return      : nth value of series
    """

    if n == 0 :
        return x
    elif n== 1:
        return y    
    else:
        return sum_series(n-1,x,y) + sum_series(n-2,x,y)

def lucas(n):
    """
    Description : This method provides lucas value for the provided number
    Argument    : Provide a number for which you need lucas value
    return      : nth value of lucas series
    """

    if n == 0 :
        return 2
    elif n== 1:
        return 1    
    else:
        return lucas(n-1) + lucas(n-2)

def fibonacci(n):
    """
    Description : This method provides fibanacci value for the provided number
    Argument    : Provide a number for which you need fibonacci value
    return      : nth value of fibonacci series
    """

    if n <= 1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Enter the value you want in the fibonacci & lucas series"))
    if n<0:
        print("Negative number is not accepted")
    else:
        print(f"nth value in the fibonacci series is {fibonacci(n)}")
        print(f"nth value in the lucas series is {lucas(n)}")
        # fibonacci number
        print(f"nth value in the fibonacci series is {sum_series(n,0,1)}") 
        # lucas number
        print(f"nth value in the lucas series is {sum_series(n,2,1)}") 

if __name__ == "__main__":
    main()
