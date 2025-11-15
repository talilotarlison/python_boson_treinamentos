Em Python, um **decorator** (ou decorador) é uma função que permite adicionar ou modificar o comportamento de outras funções ou métodos de forma modular e reutilizável, sem modificar diretamente o código da função original. Ele "envolve" outra função, alterando sua execução de uma maneira elegante e compacta.

### Como funciona um decorator?

O decorador em Python é uma função que recebe outra função como argumento e retorna uma nova função que geralmente faz algo extra antes ou depois da execução da função original.

Aqui está um exemplo simples de como um decorator funciona:

```python
# Definindo um decorador
def meu_decorator(func):
    def wrapper():
        print("Antes de chamar a função")
        func()
        print("Depois de chamar a função")
    return wrapper

# Função que será decorada
def ola_mundo():
    print("Olá, Mundo!")

# Aplicando o decorador
ola_mundo = meu_decorator(ola_mundo)

# Chamando a função decorada
ola_mundo()
```

### Saída:

```
Antes de chamar a função
Olá, Mundo!
Depois de chamar a função
```

### Usando a sintaxe de "@" (sintaxe do decorador)

O Python oferece uma maneira mais elegante de aplicar um decorador, usando a sintaxe `@`, o que evita a necessidade de reatribuir a função decorada manualmente:

```python
def meu_decorator(func):
    def wrapper():
        print("Antes de chamar a função")
        func()
        print("Depois de chamar a função")
    return wrapper

@meu_decorator
def ola_mundo():
    print("Olá, Mundo!")

ola_mundo()
```

### Saída:

```
Antes de chamar a função
Olá, Mundo!
Depois de chamar a função
```

### Decoradores com parâmetros

Se a função decorada aceita parâmetros, o decorador também pode ser feito para aceitar e passar esses parâmetros:

```python
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes de chamar a função")
        result = func(*args, **kwargs)
        print("Depois de chamar a função")
        return result
    return wrapper

@meu_decorator
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
```

### Saída:

```
Antes de chamar a função
Olá, João!
Depois de chamar a função
```

### Decoradores integrados em Python

O Python já fornece alguns decoradores prontos para uso, como:

* **`@staticmethod`**: Para definir métodos estáticos em classes.
* **`@classmethod`**: Para definir métodos de classe.
* **`@property`**: Para criar propriedades de acesso em classes.

### Por que usar decoradores?

Decoradores são muito úteis quando você precisa adicionar funcionalidades (como logs, autenticação, permissão, ou contagem de tempo) de maneira reutilizável e sem alterar o código original de uma função. Eles ajudam a manter o código limpo e modular.
