<h1 align="center">🛒 Sistema de Caixa com Desconto v2.0 🛒</h1>

<p align="center">
  <strong>Um simulador de ponto de venda (PDV) interativo em Python, que aplica descontos com base no valor da compra e em cupons específicos, agora com funções modulares e tratamento de erros.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status Concluído">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License MIT">
</p>

---

## 📍 Tabela de Conteúdos

* [📌 Sobre o Projeto](#-sobre-o-projeto)
* [🎬 Demonstração em Ação](#-demonstração-em-ação)
* [✨ Funcionalidades Principais](#-funcionalidades-principais)
* [⚙️ Lógica e Regras de Negócio](#️-lógica-e-regras-de-negócio)
* [🚀 Como Executar](#-como-executar)
* [💡 Ideias para Melhorias Futuras](#-ideias-para-melhorias-futuras)
* [👨‍💻 Autor](#-autor)

---

## 📌 Sobre o Projeto

Este projeto simula um sistema de caixa de uma loja, onde o operador pode inserir o valor de um produto e um cupom de desconto para calcular o preço final. O programa foi estruturado com funções para melhor organização e inclui validação de entrada para uma experiência de usuário mais robusta e à prova de erros. É um excelente exercício prático de lógica condicional, loops e funções em Python.

---

## 🎬 Demonstração em Ação

Veja abaixo uma simulação do fluxo do programa, incluindo o tratamento de erros e a aplicação de um cupom válido.

```sh
==================== Bem-vindo ao Sistema de Caixa ====================

============ Cupons Aplicáveis ===================
- DESCONTO10 (para compras de R$ 51 a R$ 100)
- DESCONTO20 (para compras acima de R$ 100)
- SEM_DESCONTO (para qualquer compra)
==================================================

Digite o valor original da peça: R$ ola mundo
Erro: Por favor, digite um valor numérico válido.

============ Cupons Aplicáveis ===================
...
Digite o valor original da peça: R$ 80
Digite seu cupom: DESCONTO10
✔️ Cupom 'DESCONTO10' aplicado!

Resumo da Compra:
Preço Original....: R$ 80.00
Desconto..........: R$ 8.00
Preço Final a Pagar: R$ 72.00

Processando pagamento...
██████████████████████████████
Pagamento realizado com sucesso!

Deseja realizar outra operação? (S/N): n

Obrigado, volte sempre!
```

---

## ✨ Funcionalidades Principais

* **Menu Interativo em Loop:** O sistema exibe um menu de cupons e continua rodando até que o usuário decida sair.
* **Lógica de Desconto Condicional:** Aplica descontos específicos apenas se o valor da compra e o cupom digitado corresponderem às regras de negócio.
* **Validação de Entrada Numérica:** Utiliza um bloco `try-except` para garantir que o programa não quebre se o usuário digitar um texto em vez de um número para o preço.
* **Código Modular com Funções:** Separa responsabilidades em funções como `exibir_menu_cupons()` e `simular_pagamento()`, tornando o código mais limpo e reutilizável (Princípio DRY).
* **Animação de Processamento:** Inclui uma barra de carregamento para simular o processamento do pagamento, melhorando a experiência do usuário.
* **Feedback Claro:** Fornece mensagens claras para o usuário, seja para confirmar o sucesso de uma operação (✔️) ou para informar sobre um erro (❌).

---

## ⚙️ Lógica e Regras de Negócio

O coração do sistema é a sua lógica de descontos, que combina faixas de preço com cupons específicos.

| Faixa de Preço | Cupom Válido | Desconto Aplicado |
| :--- | :--- | :---: |
| `R$ 51.00` - `R$ 100.00` | `DESCONTO10` | **10%** |
| Acima de `R$ 100.00` | `DESCONTO20` | **20%** |
| Qualquer Valor | `SEM_DESCONTO` | **0%** |

Qualquer outra combinação de preço e cupom resultará em uma mensagem de "cupom inválido" e nenhum desconto será aplicado.

---

## 🚀 Como Executar

Este projeto não requer a instalação de bibliotecas externas (a `time` já vem com o Python).

1.  **Pré-requisitos:**
    * Ter o **Python 3** instalado.

2.  **Passos para Execução:**
    * Faça o clone deste repositório ou baixe o arquivo `.py`.
    * Abra seu terminal na pasta onde o arquivo está localizado.
    * Execute o seguinte comando:
        ```bash
        python nome_do_seu_arquivo.py
        ```
    * Siga as instruções que aparecerão no terminal!

---

## 💡 Ideias para Melhorias Futuras

Este projeto pode ser expandido de várias maneiras:

* [ ] Ler uma lista de produtos e preços de um arquivo (`.csv` ou `.json`).
* [ ] Salvar cada transação em um arquivo de log com data e hora.
* [ ] Adicionar mais formas de pagamento com diferentes taxas ou benefícios.
* [ ] Transformar em um sistema com múltiplos usuários e senhas.
* [ ] Criar uma interface gráfica simples usando `Tkinter` ou `PySimpleGUI`.

---

## 👨‍💻 Autor

**Eugenio Santana**.

