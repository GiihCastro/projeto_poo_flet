class Cliente:
    def __init__(self, id:int, nome:str, telefone:str, email:str):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Quarto:
    def __init__(self, n_quarto:int, tipo:str, preco:float, status_quarto:bool):
        self.n_quarto = n_quarto
        self.tipo = tipo
        self.preco = preco
        self.status_quarto = status_quarto


class Reserva:
    def __init__(self, dono:int, quarto:int, check_in:str, check_out:str, status_reserva):
        self.dono = dono
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.status_reserva = status_reserva

class Hotel:
    def __init__(self):
        self.lista_de_clientes = []
        self.id_cliente = 1
        self.lista_de_quartos = []
        self.numero_quarto = 1
        self.lista_de_reservas = []
        self.id_reserva = 1
    
    def adicionarCliente(self, nome, telefone, email):
        novo_cliente = {
            "ID": self.id_cliente,
            "Nome": nome,
            "Telefone": telefone,
            "E-mail": email
        }
        self.id_cliente += 1
        self.lista_de_clientes.append(novo_cliente)
        return f"Cliente {nome} cadastrado com sucesso"

    def verTodosClientes(self):
        if len(self.lista_de_clientes) == 0:
            print("Lista Vazia")
        else:
            for cliente_da_vez in self.lista_de_clientes:
                print(f"""
                ID: {cliente_da_vez['ID']}
                Nome: {cliente_da_vez['Nome']}
                Telefone: {cliente_da_vez['Telefone']}
                E-mail: {cliente_da_vez['E-mail']}
                """)

    def modificarCliente(self):
        if not self.lista_de_clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        self.verTodosClientes()
        try:
            id_cliente = int(input("Digite o ID do cliente que deseja modificar: "))
        except ValueError:
            print("ID inválido. Digite um número.")
            return
        
        cliente_encontrado = None
        for cliente in self.lista_de_clientes:
            if cliente['ID'] == id_cliente:
                cliente_encontrado = cliente
                break
        
        if not cliente_encontrado:
            print("Cliente não encontrado.")
            return
        
        print("\nDeixe em branco para manter o valor atual.")
        novo_nome = input(f"Nome atual: {cliente_encontrado['Nome']}. Novo nome: ")
        novo_telefone = input(f"Telefone atual: {cliente_encontrado['Telefone']}. Novo telefone: ")
        novo_email = input(f"E-mail atual: {cliente_encontrado['E-mail']}. Novo e-mail: ")
        
        if novo_nome:
            cliente_encontrado['Nome'] = novo_nome
        if novo_telefone:
            cliente_encontrado['Telefone'] = novo_telefone
        if novo_email:
            cliente_encontrado['E-mail'] = novo_email
        
        print("Cliente atualizado com sucesso!")

    def excluirCliente(self):
        if not self.lista_de_clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        self.verTodosClientes()
        try:
            id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
        except ValueError:
            print("ID inválido. Digite um número.")
            return
        
        for i, cliente in enumerate(self.lista_de_clientes):
            if cliente['ID'] == id_cliente:
                confirmacao = input(f"Tem certeza que deseja excluir o cliente {cliente['Nome']}? (s/n): ")
                if confirmacao.lower() == 's':
                    del self.lista_de_clientes[i]
                    print("Cliente excluído com sucesso!")
                return
        
        print("Cliente não encontrado.")




    def adicionarQuarto(self, numero, tipo, preco):
        novo_quarto = {
            "Número": numero,
            "Tipo": tipo,
            "Preço": preco,
            "Status": True
        }
        self.numero_quarto += 1
        self.lista_de_quartos.append(novo_quarto)
        return f"Quarto {self.numero_quarto - 1} cadastrado com sucesso"

    def verTodosQuartos(self):
        if len(self.lista_de_quartos) == 0:
            print("Lista Vazia")
        else:
            for quarto_da_vez in self.lista_de_quartos:
                print(f"""
                Número: {quarto_da_vez['Número']}
                Tipo: {quarto_da_vez['Tipo']}
                Preço: {quarto_da_vez['Preço']}
                Status: {quarto_da_vez['Status']}
                """)

    def verificarQuartosDisponiveis(self):
        if len(self.lista_de_quartos) == 0:
            print("Lista Vazia")
        else:
            for quarto_da_vez in self.lista_de_quartos:
                if quarto_da_vez['Stauts'] == True:
                    print(f"""
                    Número: {quarto_da_vez['Número']}
                    Tipo: {quarto_da_vez['Tipo']}
                    Preço: {quarto_da_vez['Preço']}
                    Status: {quarto_da_vez['Status']}
                    """)

    def modificarCliente(self):
        if not self.lista_de_clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        self.verTodosClientes()
        try:
            id_cliente = int(input("Digite o ID do cliente que deseja modificar: "))
        except ValueError:
            print("ID inválido. Digite um número.")
            return
        
        cliente_encontrado = None
        for cliente in self.lista_de_clientes:
            if cliente['ID'] == id_cliente:
                cliente_encontrado = cliente
                break
        
        if not cliente_encontrado:
            print("Cliente não encontrado.")
            return
        
        print("\nDeixe em branco para manter o valor atual.")
        novo_nome = input(f"Nome atual: {cliente_encontrado['Nome']}. Novo nome: ")
        novo_telefone = input(f"Telefone atual: {cliente_encontrado['Telefone']}. Novo telefone: ")
        novo_email = input(f"E-mail atual: {cliente_encontrado['E-mail']}. Novo e-mail: ")
        
        if novo_nome:
            cliente_encontrado['Nome'] = novo_nome
        if novo_telefone:
            cliente_encontrado['Telefone'] = novo_telefone
        if novo_email:
            cliente_encontrado['E-mail'] = novo_email
        
        print("Cliente atualizado com sucesso!")

    def excluirCliente(self):
        if not self.lista_de_clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        self.verTodosClientes()
        try:
            id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
        except ValueError:
            print("ID inválido. Digite um número.")
            return
        
        for i, cliente in enumerate(self.lista_de_clientes):
            if cliente['ID'] == id_cliente:
                confirmacao = input(f"Tem certeza que deseja excluir o cliente {cliente['Nome']}? (s/n): ")
                if confirmacao.lower() == 's':
                    del self.lista_de_clientes[i]
                    print("Cliente excluído com sucesso!")
                return
        
        print("Cliente não encontrado.")

    def adicionarReserva(self, cliente_id, numero_quarto, data_checkin, data_checkout):
        cliente = next((c for c in self.lista_de_clientes if c["ID"] == cliente_id), None)
        quarto = next((q for q in self.lista_de_quartos if q["Número"] == numero_quarto), None)
        
        if cliente is None:
            return None 
        
        if quarto is None or not quarto["Status"]: 
            return None
        
        reserva = {
            "ID": len(self.lista_de_reservas) + 1,
            "ClienteID": cliente_id, 
            "Quarto": numero_quarto,
            "Check-in": data_checkin,
            "Check-out": data_checkout
        }
        
        self.lista_de_reservas.append(reserva)
        
        quarto["Status"] = False
        
        return reserva 
