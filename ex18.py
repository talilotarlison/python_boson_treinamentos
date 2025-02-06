var_global = "I'm a global variable"

def escreve_algo():
    global var_global
    var_global = "I'm a local variable test"
    var_local = "I'm a local variable"
    print(var_local)
    print(var_global)

if __main__ == '__main__':
    escreve_algo()