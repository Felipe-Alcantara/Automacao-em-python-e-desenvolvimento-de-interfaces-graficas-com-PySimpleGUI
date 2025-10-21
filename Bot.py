# Qual bibioteca usar? Python FreeSimpleGUI (fork gratuito do PySimpleGUI)

# Importa a biblioteca FreeSimpleGUI
import FreeSimpleGUI as sg

# Define o tema da GUI como "reddit"
sg.theme("reddit")

# Define o layout da janela da GUI
layout = [
    # Cria um campo de texto para o email e um campo de entrada correspondente
    [sg.Text("Email"), sg.Input(key="Email")],
    # Cria um campo de texto para a senha e um campo de entrada correspondente
    [sg.Text("Senha"), sg.Input(key="Senha", password_char="*")],
    # Cria um botão para escolher a pasta de anexos e um campo de entrada correspondente
    [sg.FolderBrowse("Escolher pasta anexos", target="input_Anexos"), sg.Input(key="input_Anexos")],
    # Cria um botão para escolher a pasta de planilhas e um campo de entrada correspondente
    [sg.FolderBrowse("Escolher pasta planilha", target="input_planilha"), sg.Input(key="input_planilha")],
    # Cria um botão "Salvar"
    [sg.Button("Salvar")]
]

# Cria uma janela com o título "Principal" e o layout definido anteriormente
janela = sg.Window("Principal", layout=layout)

# Inicia um loop infinito que mantém a janela aberta
while True:
    # Lê os eventos da janela e os valores dos campos de entrada
    event, values = janela.read()
    # Se o evento for o fechamento da janela, o loop é interrompido e o programa termina
    if event == sg.WINDOW_CLOSED:
        break
    # Se o evento for o clique no botão "Salvar", o programa recupera os valores inseridos nos campos de entrada e os imprime
    elif event == "Salvar":
        Email = values["Email"]
        Senha = values["Senha"]
        caminho_Pasta_anexos = values["input_Anexos"]
        caminho_Pasta_planilha = values["input_planilha"]
        print(f"O Email digitado foi: {Email}")
        print(f"A Senha digitado foi: {Senha}")
        print(f"O caminho da pasta de anexos é: {caminho_Pasta_anexos}")
        print(f"O caminho da pasta de planilhas é: {caminho_Pasta_planilha}")
