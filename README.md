# Hotel Management System

Este é um sistema de **gerenciamento de hotel** desenvolvido em Python. Ele permite o controle e a gestão de clientes, quartos e reservas de um hotel. O sistema oferece uma interface interativa para realizar operações como cadastro de clientes, criação de reservas, visualização de reservas e informações dos quartos.

## Funcionalidades

- **Cadastro de Clientes:** Adicione novos clientes ao sistema com informações como nome e e-mail.
- **Cadastro de Quartos:** Registre os quartos disponíveis no hotel, com informações sobre o número do quarto, tipo e preço.
- **Gerenciamento de Reservas:** Crie reservas para os clientes, incluindo a seleção de um quarto e as datas de check-in e check-out.
- **Visualização de Reservas:** Exiba todas as reservas feitas, com detalhes como ID do cliente, número do quarto, e as datas de estadia.
- **Controle de Disponibilidade:** O sistema marca os quartos como ocupados quando uma reserva é realizada e os disponibiliza quando a reserva é finalizada.

## Tecnologias Utilizadas

- **Python 3.x**
- **Flet** - Biblioteca para criação de interfaces gráficas interativas.

## Estrutura do Projeto

- **main.py**: Contém a lógica principal do sistema, incluindo as classes `Hotel`, `Cliente` e `Reserva`, e os métodos que manipulam o cadastro e reservas.
- **hotel.py** (opcional): Arquivo de configuração para dados persistentes do hotel (se necessário).

## Instalação

1. Clone este repositório para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
