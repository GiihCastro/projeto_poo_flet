from objetos import Gerenciador

while True:
    print('\nEscolha uma das opções abaixo:')
    menu = input('''\n ------ Refúgio dos Sonhos ------
        | 1 - Gerenciar Clientes
        | 2 - Gerenciar Quartos
        | 3 - Gerenciar Reservas
        | 0 - Sair
            
        Digite sua escolha => ''')
    match menu:
        case "1":
            print("\n----- Gerenciar Clientes -----\n")
            while True:
                menu_clientes = input("""
                Escolha uma opção:
                | 1 - Adicionar Cliente
                | 2 - Ver todos os Clientes
                | 3 - Modificar Cliente
                | 4 - Excluir Cliente
                | 0 - Sair
                """)
                
                match menu_clientes:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "4":
                        Gerenciador.ExcluirCliente()
                    case "0":
                        break
                    case _:
                        pass

        case "2":
            print("\n----- Gerenciar Quartos -----\n")
            while True:
                menu_clientes = input("""
                Escolha uma opção:
                | 1 - Adicionar Quarto
                | 2 - Ver todos os Quartos
                | 3 - Modificar Quarto
                | 4 - Excluir Quarto
                | 0 - Sair
                """)
                
                match menu_clientes:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "4":
                        pass
                    case "0":
                        break
                    case _:
                        pass

        case "3":
            print("\n----- Gerenciar Reservas -----\n")
            while True:
                menu_clientes = input("""
                Escolha uma opção:
                | 1 - Adicionar Reserva
                | 2 - Ver todos as Reservas
                | 3 - Modificar Reserva
                | 4 - Excluir Reserva
                | 0 - Sair
                """)
                
                match menu_clientes:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case "4":
                        pass
                    case "0":
                        break
                    case _:
                        pass

        case "0":
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida!")

    