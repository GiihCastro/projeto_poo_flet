class Pessoa:
    def __init__(self, nome:str, idade:int, telefone:str, email:str):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email

class CLiente(Pessoa):
    def __init__(self, nome:str, idade:int, telefone:str, email:str, id:str):
        super().__init__(nome, idade, telefone, email)
        self.id = id


class Quarto:
    def __init__(self, num:int, tipo:str, diaria:float, status_quarto:bool):
        self.num = num
        self.tipo = tipo
        self.diaria = diaria
        self.status_quarto = status_quarto

class Reserva:
    def __init__(self, dono:int, quarto:int, checkin:str, checkout:str, status_reserva:bool):
        self.dono = dono
        self.quarto = quarto
        self.checkout = checkout
        self.checkin = checkin
        self.status_reserva = status_reserva

class Gerenciador:
    def __init__(self):
        self.lista_de_clientes = []
        self.id_cliente = 1
        self.lista_de_quartos = []
        self.lista_de_reservas = []

# ---------- CLiente --------------------------------------------------------------

    def adicionarCliente(self):
        nome = input("Digite o nome do cliente")
        telefone = input("Digite o telefone do cliente")
        email = input("Digite o email do cliente")

        novo_cliente = {
            "ID": self.id_cliente,
            "Nome": self.nome,
            "Telefone": self.telefone,
            "E-mail": email
        }

        self.id_cliente += 1
        self.lista_de_clientes.append(novo_cliente)
        return f"Cliente cadastrado com sucesso"

    def verTodosClientes(self):
        if not self.lista_de_clientes:
            print("Não há clientes cadastrados.")
            return
        for cliente in self.lista_de_clientes:
            print(f"ID: {cliente.id}, Nome: {cliente.nome}, Idade: {cliente.idade}, Telefone: {cliente.telefone}, Email: {cliente.email}")

    def modificarClientes(self):
        pass

    def ExcluirCliente(self):
        for cliente in self.lista_de_clientes:
            if cliente.id == id:
                self.lista_de_clientes.remove(cliente)
                print(f"Cliente {id} excluído com sucesso.")
                return
            print(f"Cliente com ID {id} não encontrado.")

# ---------- Quartos --------------------------------------------------------------

    def adicionarQuarto(self):
        pass

    def verTodosQuartos(self):
        pass

    def modificarQuartos(self):
        pass

    def ExcluirQuarto(self):
        pass

    def VerificarQuartosDisponiveis(self):
        pass

# ---------- Reserva --------------------------------------------------------------

    def adicionarReserva(self):
        pass

    def verTodasReservas(self):
        pass

    def modificarReservas(self):
        pass

    def ExcluirReserva(self):
        pass

    def VerificarReservasDisponiveis(self):
        pass

