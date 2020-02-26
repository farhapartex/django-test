class Fibonacci:

    def __init__(self,n):
        self.get_solution(n)

    def get_solution(self,n):
        a = 0
        b = 1
        if n < 0: 
            print("Incorrect input") 
        elif n == 0: 
            return a 
        elif n == 1: 
            print(b) 
        else: 
            for i in range(2,n+1): 
                c = a + b 
                a,b = b,c
            print(b)

if __name__ == "__main__":
    n = int(input())
    fibb = Fibonacci(n)