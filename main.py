import flet as ft
from classes import Hotel


def main(page: ft.Page):
    # Configurações da página
    page.title = "Sistema de Gerenciamento de Hotel"
    page.window_width = 800
    page.window_height = 600
    page.scroll = "adaptive"
    page.theme_mode = "light"
    
    # Instância do hotel
    hotel = Hotel()
    
    # Funções auxiliares para exibir mensagens
    def show_snackbar(message, color=ft.colors.GREEN):
        page.snack_bar = ft.SnackBar(ft.Text(message), bgcolor=color)
        page.snack_bar.open = True
        page.update()
    
    # Área para exibir resultados
    output_area = ft.Column(scroll="always", expand=True)
    
    # ========== CLIENTES ==========
    def build_cliente_view():
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Adicionar Cliente", on_click=add_cliente_dialog),
                        ft.ElevatedButton("Ver Todos", on_click=lambda _: show_all_clientes()),
                        ft.ElevatedButton("Modificar", on_click=modify_cliente_dialog),
                        ft.ElevatedButton("Excluir", on_click=delete_cliente_dialog),
                    ],
                    spacing=10
                ),
                output_area
            ]
        )
    
    def show_all_clientes():
        output_area.controls.clear()
        if not hotel.lista_de_clientes:
            output_area.controls.append(ft.Text("Nenhum cliente cadastrado."))
        else:
            for cliente in hotel.lista_de_clientes:
                output_area.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(f"ID: {cliente['ID']}"),
                                    ft.Text(f"Nome: {cliente['Nome']}"),
                                    ft.Text(f"Telefone: {cliente['Telefone']}"),
                                    ft.Text(f"E-mail: {cliente['E-mail']}"),
                                ],
                                spacing=5
                            ),
                            padding=10
                        )
                    )
                )
        page.update()
    
    def add_cliente_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()
        
        def save_cliente(e):
            nome = nome_field.value
            telefone = telefone_field.value
            email = email_field.value
            
            if nome and telefone and email:
                hotel.adicionarCliente(nome, telefone, email)
                close_dlg(e)
                show_snackbar(f"Cliente {nome} cadastrado com sucesso!")
                show_all_clientes()
            else:
                show_snackbar("Preencha todos os campos!", ft.colors.RED)
        
        nome_field = ft.TextField(label="Nome")
        telefone_field = ft.TextField(label="Telefone")
        email_field = ft.TextField(label="E-mail")
        
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Adicionar Cliente"),
            content=ft.Column(
                controls=[
                    nome_field,
                    telefone_field,
                    email_field
                ],
                height=200,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Salvar", on_click=save_cliente),
            ],
            actions_alignment="end",
        )
        
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    
    def modify_cliente_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()
        
        def save_changes(e):
            cliente_id = int(id_field.value)
            nome = nome_field.value
            telefone = telefone_field.value
            email = email_field.value
            
            for cliente in hotel.lista_de_clientes:
                if cliente['ID'] == cliente_id:
                    if nome:
                        cliente['Nome'] = nome
                    if telefone:
                        cliente['Telefone'] = telefone
                    if email:
                        cliente['E-mail'] = email
                    
                    show_snackbar(f"Cliente ID {cliente_id} atualizado com sucesso!")
                    close_dlg(e)
                    show_all_clientes()
                    return
            
            show_snackbar(f"Cliente ID {cliente_id} não encontrado!", ft.colors.RED)
        
        id_field = ft.TextField(label="ID do Cliente")
        nome_field = ft.TextField(label="Novo Nome (deixe em branco para não alterar)")
        telefone_field = ft.TextField(label="Novo Telefone (deixe em branco para não alterar)")
        email_field = ft.TextField(label="Novo E-mail (deixe em branco para não alterar)")
        
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Modificar Cliente"),
            content=ft.Column(
                controls=[
                    id_field,
                    nome_field,
                    telefone_field,
                    email_field
                ],
                height=250,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Salvar", on_click=save_changes),
            ],
            actions_alignment="end",
        )
        
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    
    def delete_cliente_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()
        
        def confirm_delete(e):
            cliente_id = int(id_field.value)
            
            for i, cliente in enumerate(hotel.lista_de_clientes):
                if cliente['ID'] == cliente_id:
                    hotel.lista_de_clientes.pop(i)
                    show_snackbar(f"Cliente ID {cliente_id} excluído com sucesso!")
                    close_dlg(e)
                    show_all_clientes()
                    return
            
            show_snackbar(f"Cliente ID {cliente_id} não encontrado!", ft.colors.RED)
        
        id_field = ft.TextField(label="ID do Cliente a excluir")
        
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Excluir Cliente"),
            content=ft.Column(
                controls=[id_field],
                height=100,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Confirmar", on_click=confirm_delete),
            ],
            actions_alignment="end",
        )
        
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    
    # ========== QUARTOS ==========
    
    def build_quarto_view():
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Adicionar Quarto", on_click=add_quarto_dialog),
                        ft.ElevatedButton("Ver Todos", on_click=lambda _: show_all_quartos()),
                        ft.ElevatedButton("Modificar", on_click=modify_quarto_dialog),
                        ft.ElevatedButton("Excluir", on_click=delete_quarto_dialog),
                        ft.ElevatedButton("Ver Disponíveis", on_click=lambda _: show_available_quartos()),
                    ],
                    spacing=10
                ),
                output_area
            ]
        )
    
    def show_all_quartos():
        output_area.controls.clear()
        if not hotel.lista_de_quartos:
            output_area.controls.append(ft.Text("Nenhum quarto cadastrado."))
        else:
            for quarto in hotel.lista_de_quartos:
                status = "Disponível" if quarto['Status'] else "Ocupado"
                output_area.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(f"Número: {quarto['Número']}"),
                                    ft.Text(f"Tipo: {quarto['Tipo']}"),
                                    ft.Text(f"Preço: R${quarto['Preço']:.2f}"),
                                    ft.Text(f"Status: {status}"),
                                ],
                                spacing=5
                            ),
                            padding=10
                        )
                    )
                )
        page.update()
    
    def show_available_quartos():
        output_area.controls.clear()
        available = [q for q in hotel.lista_de_quartos if q['Status']]
        
        if not available:
            output_area.controls.append(ft.Text("Nenhum quarto disponível."))
        else:
            for quarto in available:
                output_area.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(f"Número: {quarto['Número']}"),
                                    ft.Text(f"Tipo: {quarto['Tipo']}"),
                                    ft.Text(f"Preço: R${quarto['Preço']:.2f}"),
                                ],
                                spacing=5
                            ),
                            padding=10
                        )
                    )
                )
        page.update()
    
    def add_quarto_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        def save_quarto(e):
            numero = numero_field.value
            tipo = tipo_field.value
            preco = preco_field.value

            if numero and tipo and preco:
                try:
                    preco_float = float(preco)
                    hotel.adicionarQuarto(numero, tipo, preco_float)
                    close_dlg(e)
                    show_snackbar(f"Quarto {numero} cadastrado com sucesso!")
                    show_all_quartos()
                except ValueError:
                    show_snackbar("Preço deve ser um número!", ft.colors.RED)
            else:
                show_snackbar("Preencha todos os campos!", ft.colors.RED)

        numero_field = ft.TextField(label="Número do Quarto")
        tipo_field = ft.TextField(label="Tipo (Ex: Solteiro, Casal)")
        preco_field = ft.TextField(label="Preço por Noite")

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Adicionar Quarto"),
            content=ft.Column(
                controls=[numero_field, tipo_field, preco_field],
                height=200,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Salvar", on_click=save_quarto),
            ],
            actions_alignment="end",
        )

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def modify_quarto_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        def save_changes(e):
            numero = numero_field.value
            tipo = tipo_field.value
            preco = preco_field.value

            for quarto in hotel.lista_de_quartos:
                if quarto['Número'] == numero:
                    if tipo:
                        quarto['Tipo'] = tipo
                    if preco:
                        try:
                            quarto['Preço'] = float(preco)
                        except ValueError:
                            show_snackbar("Preço inválido!", ft.colors.RED)
                            return

                    show_snackbar(f"Quarto {numero} atualizado com sucesso!")
                    close_dlg(e)
                    show_all_quartos()
                    return

            show_snackbar(f"Quarto {numero} não encontrado!", ft.colors.RED)

        numero_field = ft.TextField(label="Número do Quarto")
        tipo_field = ft.TextField(label="Novo Tipo (opcional)")
        preco_field = ft.TextField(label="Novo Preço (opcional)")

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Modificar Quarto"),
            content=ft.Column(
                controls=[numero_field, tipo_field, preco_field],
                height=200,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Salvar", on_click=save_changes),
            ],
            actions_alignment="end",
        )

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def delete_quarto_dialog(e):

        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        def confirm_delete(e):
            numero = numero_field.value
            for i, quarto in enumerate(hotel.lista_de_quartos):
                if quarto['Número'] == numero:
                    hotel.lista_de_quartos.pop(i)
                    show_snackbar(f"Quarto {numero} excluído com sucesso!")
                    close_dlg(e)
                    show_all_quartos()
                    return

            show_snackbar(f"Quarto {numero} não encontrado!", ft.colors.RED)

        numero_field = ft.TextField(label="Número do Quarto a excluir")

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Excluir Quarto"),
            content=ft.Column(
                controls=[numero_field],
                height=100,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Confirmar", on_click=confirm_delete),
            ],
            actions_alignment="end",
        )

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    
    # (Implementar add_quarto_dialog, modify_quarto_dialog, delete_quarto_dialog similar aos de clientes)
    
    # ========== RESERVAS ==========
    def build_reserva_view():
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Adicionar Reserva", on_click=add_reserva_dialog),
                        ft.ElevatedButton("Ver Todas", on_click=lambda _: show_all_reservas()),
                        ft.ElevatedButton("Modificar", on_click=modify_reserva_dialog),
                        ft.ElevatedButton("Excluir", on_click=delete_reserva_dialog),
                    ],
                    spacing=10
                ),
                output_area
            ]
        )
    
    # (Implementar funções de reserva similar às anteriores)
    def add_reserva_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        def save_reserva(e):
            cliente_id = id_cliente_field.value
            numero_quarto = numero_quarto_field.value
            data_checkin = checkin_field.value
            data_checkout = checkout_field.value

            if cliente_id and numero_quarto and data_checkin and data_checkout:
                try:
                    cliente_id_int = int(cliente_id)
                    reserva = hotel.adicionarReserva(cliente_id_int, numero_quarto, data_checkin, data_checkout)
                    if reserva:
                        show_snackbar(f"Reserva criada com sucesso!")
                        close_dlg(e)
                        show_all_reservas()
                    else:
                        show_snackbar("Erro ao criar reserva. Verifique dados ou disponibilidade.", ft.colors.RED)
                except ValueError:
                    show_snackbar("ID do cliente deve ser um número!", ft.colors.RED)
            else:
                show_snackbar("Preencha todos os campos!", ft.colors.RED)

        id_cliente_field = ft.TextField(label="ID do Cliente")
        numero_quarto_field = ft.TextField(label="Número do Quarto")
        checkin_field = ft.TextField(label="Data Check-in (YYYY-MM-DD)")
        checkout_field = ft.TextField(label="Data Check-out (YYYY-MM-DD)")

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Adicionar Reserva"),
            content=ft.Column(
                controls=[
                    id_cliente_field,
                    numero_quarto_field,
                    checkin_field,
                    checkout_field
                ],
                height=250,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Salvar", on_click=save_reserva),
            ],
            actions_alignment="end",
        )

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def show_all_reservas():
        output_area.controls.clear()
        if not hotel.lista_de_reservas:
            output_area.controls.append(ft.Text("Nenhuma reserva cadastrada."))
        else:
            for reserva in hotel.lista_de_reservas:
                output_area.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(f"ID: {reserva['ID']}"),
                                    ft.Text(f"Cliente ID: {reserva['ClienteID']}"),
                                    ft.Text(f"Quarto: {reserva['Quarto']}"),
                                    ft.Text(f"Check-in: {reserva['Check-in']}"),
                                    ft.Text(f"Check-out: {reserva['Check-out']}"),
                                ],
                                spacing=5
                            ),
                            padding=10
                        )
                    )
                )
        page.update()

    def modify_reserva_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        def save_changes(e):
            try:
                reserva_id = int(id_field.value)
            except ValueError:
                show_snackbar("ID inválido!", ft.colors.RED)
                return

            checkin = checkin_field.value
            checkout = checkout_field.value

            for reserva in hotel.lista_de_reservas:
                if reserva['ID'] == reserva_id:
                    if checkin:
                        reserva['Check-in'] = checkin
                    if checkout:
                        reserva['Check-out'] = checkout
                    show_snackbar(f"Reserva ID {reserva_id} atualizada com sucesso!")
                    close_dlg(e)
                    show_all_reservas()
                    return

            show_snackbar(f"Reserva ID {reserva_id} não encontrada!", ft.colors.RED)

        id_field = ft.TextField(label="ID da Reserva")
        checkin_field = ft.TextField(label="Novo Check-in (opcional)")
        checkout_field = ft.TextField(label="Novo Check-out (opcional)")

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Modificar Reserva"),
            content=ft.Column(
                controls=[id_field, checkin_field, checkout_field],
                height=200,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Salvar", on_click=save_changes),
            ],
            actions_alignment="end",
        )

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def delete_reserva_dialog(e):
        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        def confirm_delete(e):
            try:
                reserva_id = int(id_field.value)
            except ValueError:
                show_snackbar("ID inválido!", ft.colors.RED)
                return

            for i, reserva in enumerate(hotel.lista_de_reservas):
                if reserva['ID'] == reserva_id:
                    hotel.lista_de_reservas.pop(i)
                    show_snackbar(f"Reserva ID {reserva_id} excluída com sucesso!")
                    close_dlg(e)
                    show_all_reservas()
                    return

            show_snackbar(f"Reserva ID {reserva_id} não encontrada!", ft.colors.RED)

        id_field = ft.TextField(label="ID da Reserva a excluir")

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Excluir Reserva"),
            content=ft.Column(
                controls=[id_field],
                height=100,
                width=400,
                tight=True
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.TextButton("Confirmar", on_click=confirm_delete),
            ],
            actions_alignment="end",
        )

        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    
    # ========== MAIN VIEW ==========
    def change_view(e):
        index = e.control.selected_index
        content_area.content = views[index]
        page.update()
    
    # Criar as visualizações
    cliente_view = build_cliente_view()
    quarto_view = build_quarto_view()
    reserva_view = build_reserva_view()
    views = [cliente_view, quarto_view, reserva_view]
    
    # Barra de navegação
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.PERSON, label="Clientes"),
            ft.NavigationDestination(icon=ft.icons.BED, label="Quartos"),
            ft.NavigationDestination(icon=ft.icons.CALENDAR_TODAY, label="Reservas"),
        ],
        on_change=change_view,
        selected_index=0
    )
    
    # Área de conteúdo principal
    content_area = ft.Container(content=cliente_view, expand=True)
    
    # Layout principal
    page.add(
        ft.Column(
            controls=[
                ft.Text("Sistema de Gerenciamento de Hotel", size=24, weight="bold"),
                content_area,
                nav_bar
            ],
            expand=True
        )
    )

ft.app(target=main)