import math

class Expressao:
    __switch_op = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: math.pow(a, b)
        }
    
    def __init__(self, exp=None):
        self.s = []  # Stack / Pilha
        self.t = -1  # Top   / Topo

        if exp is None:
            return

        for entry in exp.split(' '):
            if  any(digit in entry for digit in ['0', '1', '2', '3', '4',
                                                  '5', '6', '7', '8', '9']):
                self.stack(float(entry))
            else:
                self.stack(entry)

    def stack(self, value):
        self.t = self.t + 1
        self.s.insert(0, value)

    def pop(self):
        self.t = self.t - 1
        return self.s[self.t + 1]

    def eval(self, x, reset=False):
        if reset:
            self.t = len(self.s) - 1
        
        entry = self.pop()

        if type(entry) == float:
            return entry
        elif 'x' in entry:
            return x
        else:
            return self.__switch_op[entry](self.eval(x), self.eval(x))
            
if __name__ == "__main__":
    e = Expressao("- * 3 ^ x 2 17")

    def f(x):
        return (e.eval(x, True))

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    tol = 0.0001
    c = a - b
    x0 = (a + b)/2

    while(math.fabs(c) > tol):
        if(f(a)*f(x0) > 0.0):
            a = x0
        else:
            b = x0
        x0 = (a + b)/2
        c = math.fabs(a - b) 

    print("O valor de x0: ",x0)