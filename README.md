# Avaliação de POO - Sistema de Caixa Eletrônico

> O sistema consiste e um sistema de caixa eletrônico (ATM) utilizando os princípios 
de POO (Programação Orientada a Objetos), organização em pacotes, modularização, separação
de responsabilidades e demais boas práticas no desenvolvimento de software.

[Clique aqui](docs/pdfs/🧠%20Avaliação%20de%20Programação%20Orientada%20a%20Objetos%20(POO).pdf) para acessar o pdf com todas as informações acerca da avalidação.

## ⚙️ Requisitos

O sistema deve implementar as seguintes funcionalidades:

- Usuários devem criar contas
- Usuários podem depositar e sacar dinheiro
- Deve ser permitido a consulta do saldo atual
- Operações devem ser armazenadas em um histórico que pode ser acessado

## 🧩 Requisitos de POO

O projeto <b>deve</b> implementar os seguintes conceitos:

1. Organização em pacotes (arquivos)
2. Criação e instanciação de classes (Conta, Cliente, Operacao...)
3. Implementar conceitos de herança, polimorfismo, agregação e composição
4. Atributos devem ser encapsulados

## 🧪 Regras de negócio

- Não permitir saque com saldo insuficiente
- Registrar todas as operações no histórico
- Validar entradas do usuário
- Exibir mensagens claras na interface

## 🛠️ Tecnologias

- Python v3.12.3

## 🖥️ Interface

A interface deve ser um menu interativo. A princípio será feito via terminal, mas pode haver mudanças na abordagem conforme o desenvolvimento.

## 🏗️ Estrutura do projeto

O projeto irá seguir uma organização simples em módulos. Cada módulo irá conter os arquivos correspondentes ao domínio. 
Poderemos ter mais pastas auxiliares conforme a necessidade. 
Os módulos poderão se comunicar entre si por meio dos contratos definidos.

### Exemplo:

```
.
├── app/
│   ├── modules/
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   ├── models/
│   │   │   │   └── user.py
│   │   │   └── services/
│   │   │       └── user_service.py
│   │   └── ...
│   ├── shared/
│   │   └── ...
│   ├── lib/
│   │   └── ...
│   └── ...
└── main.py
```

## 📚 Mais informações

Para mais informações [clique aqui](docs/README.md).

## 🏃‍♂️‍➡️ Execução

```bash
python main.py
```
