
def multiplication(a, b):
    return a * b

def division(a,b):
    if b == 0:
        print("It is not possible to divide by 0")
        return 0
    else:
        return a/b


def main():

    print("=== Start Program ===\n")
    
    result1 = multiplication(5, 3)
    print(f"Multiplication: 5 * 3 = {result1}")
    
    result2 = division(10, 2)
    print(f"Division: 10 / 2 = {result2}")
    
    result3 = division(10, 0)
    print(f"Division result: {result3}")
    
    print("\n=== Program End ===")


# Punkt wejścia programu
if __name__ == "__main__":
    main()
