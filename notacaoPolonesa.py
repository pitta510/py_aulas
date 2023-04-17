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
            if any(digit in entry for digit in ['0', '1', '2', '3', '4', 
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
    e = Expressao("+ * 3 ^ x 2 7")
    # print(e.eval(1, True))


    a = 1
    b = 4

    e2 = Expressao("- * 3 ^ x 2 17")
    fda = e2.eval(1 , True)
    fdb = e2.eval(4 , True)

    err = 0.0001
    mediaPonderada = 0
    while(math.fabs(a - b)) > err:
        mediaPonderada = (a*fdb + b*fda)/ (fdb + fda)
        if e2.eval(mediaPonderada,True) * fda < 0:
            fdb = mediaPonderada
        else:
            fda= mediaPonderada


    print(fda)
    print(fdb) 
    print(mediaPonderada)     

