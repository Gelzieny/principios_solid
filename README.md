# Princípios SOLID em Python

Os princípios SOLID são um conjunto de diretrizes para a escrita de um código mais limpo, modular e manutenível. Eles foram definidos por Robert C. Martin (Uncle Bob) e são amplamente utilizados no desenvolvimento de software orientado a objetos.

## S.O.L.I.D:

### 1. **Single Responsibility Principle (SRP) - Princípio da Responsabilidade Única**
Uma classe deve ter apenas um motivo para mudar, ou seja, deve ter apenas uma responsabilidade.

**Exemplo em Python:**
```python
class Relatorio:
    def gerar_relatorio(self, dados):
        # Gera o relatorio
        pass
    
class SalvarRelatorio:
    def salvar_em_pdf(self, relatorio):
        # Salva o relatorio em PDF
        pass
```

### 2. **Open/Closed Principle (OCP) - Princípio Aberto/Fechado**
Uma classe deve estar aberta para extensão, mas fechada para modificação.

**Exemplo em Python:**
```python
from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoNatal(Desconto):
    def calcular(self, valor):
        return valor * 0.9

class DescontoBlackFriday(Desconto):
    def calcular(self, valor):
        return valor * 0.8
```

### 3. **Liskov Substitution Principle (LSP) - Princípio da Substituição de Liskov**
Uma classe derivada deve poder ser substituída por sua classe base sem alterar a corretude do programa.

**Exemplo em Python:**
```python
class Ave:
    def voar(self):
        pass

class Pardal(Ave):
    def voar(self):
        print("O pardal está voando")

class Pinguim(Ave):
    def voar(self):
        raise NotImplementedError("Pinguins não voam")
```
**Correção usando Segregação de Interfaces:**
```python
class Ave:
    pass

class AveQueVoa(Ave):
    def voar(self):
        pass

class Pardal(AveQueVoa):
    def voar(self):
        print("O pardal está voando")

class Pinguim(Ave):
    def nadar(self):
        print("O pinguim está nadando")
```

### 4. **Interface Segregation Principle (ISP) - Princípio da Segregação de Interfaces**
Uma classe não deve ser forçada a implementar métodos que não usa.

**Exemplo em Python:**
```python
from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def comer(self):
        pass

class AveQueVoa(Ave):
    @abstractmethod
    def voar(self):
        pass

class Pardal(AveQueVoa):
    def comer(self):
        print("Pardal comendo")
    
    def voar(self):
        print("Pardal voando")

class Pinguim(Ave):
    def comer(self):
        print("Pinguim comendo")
```

### 5. **Dependency Inversion Principle (DIP) - Princípio da Inversão de Dependência**
Os módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

**Exemplo em Python:**
```python
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass

class EmailNotificador(Notificador):
    def notificar(self, mensagem):
        print(f"Enviando e-mail: {mensagem}")

class SMSNotificador(Notificador):
    def notificar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class Usuario:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador
    
    def enviar_notificacao(self, mensagem):
        self.notificador.notificar(mensagem)

# Uso
usuario = Usuario(EmailNotificador())
usuario.enviar_notificacao("Bem-vindo!")
```

## Conclusão
Os princípios SOLID ajudam a manter o código mais limpo, flexível e fácil de manter. Ao aplicá-los corretamente, é possível melhorar a qualidade do software e reduzir custos de manutenção.
