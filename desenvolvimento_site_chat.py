'''
    # Título: DioChat
    # Botão de iniciar chat
        # Pop-Up (Janela na frente da tela)
        # Título: Bem vindo ao DioChat
        # Campo de texto -> Escreva seu nome
        # Botão pra Iniciar Chat
            # Sumir o Título DioChat
            # Fechar a janela (Pop-Up)
            # Carregar o chat
                # As mensagens que já foram enviadas (Chat)
                # Campo: Digite sua mensagem
                # Botão de Enviar
    
    # 3 Pasos ( Criar as Funcionalidades 
                Add as Funcionalidades
                Rodar o APP/Sistema/Site 
                )
                
    pip install flet -> no seu terminal

'''

import flet as ft

def main (pagina):
    # Criar todas as funcionalidades

    titulo = ft.Text("DioChat")
    chat = ft.Column()

    # Criando tunel de comunicação - 2 Etapas
    # 01 - Criar uma função
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat) # Add a mensagem no final da lista - O APPEND faz isso
        pagina.update()

    # Criar o tunel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_msg = campo_msg.value
        nome_usuario = campo_nome_usuario.value
        #print(f"Diogo: {texto_msg}") # Contatenando texto fixo com texto dinamico
        mensagem = f"{nome_usuario}: {texto_msg}"
        pagina.pubsub.send_all(mensagem)
        #texto_chat = ft.Text(mensagem)
        #chat.controls.append(texto_chat) # Add a mensagem no final da lista - O APPEND faz isso
        campo_msg.value = ""
        pagina.update()
    
    campo_msg = ft.TextField(label="Digite sua Mensagem", on_submit=enviar_mensagem)
    bt_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_msg, bt_enviar])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(bt_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value}, Entrou no chat"
        #texto_entrar_chat = ft.Text()
        #chat.controls.append(texto_entrar_chat)
        pagina.pubsub.send_all(mensagem)
        #pagina.add(campo_msg)
        #pagina.add(bt_enviar)
        pagina.update()    

    # Criando poupop

    titulo_janela = ft.Text("Bem vindo ao DioChat")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome", on_submit=entrar_chat)
    bt_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    
    janela = ft.AlertDialog(title=titulo_janela, 
                            content=campo_nome_usuario, 
                            actions=[bt_entrar])

    # Função pra iniciar o CHAT
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()


    bt_iniciar = ft.ElevatedButton("Entrar no Chat", on_click=iniciar_chat)

    # Adicionar o elemento na pagina

    pagina.add(titulo)
    pagina.add(bt_iniciar)

# Rodar o App/Site

ft.app(main, view=ft.WEB_BROWSER)