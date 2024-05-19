# Automacao-em-python-e-desenvolvimento-de-interfaces-graficas-com-PySimpleGUI
 Um robô que entre em um email, baixa as mensagens em anexo salvando numa pasta, após isso, lê os anexos e os que possuirem códigos de barras são lançados em uma planilha com o código digitavel do boleto, nome do arquivo, data de vencimento e o valor.

# Projeto PySimpleGUI

Este projeto é um script Python que usa a biblioteca PySimpleGUI para criar uma interface gráfica do usuário (GUI). A GUI permite que os usuários insiram um email e uma senha, e escolham pastas para anexos e planilhas.

## Como funciona

1. **Importação da biblioteca PySimpleGUI**: A biblioteca PySimpleGUI é usada para criar a GUI.

2. **Definição do tema da GUI**: O tema da GUI é definido como "reddit".

3. **Definição do layout da GUI**: O layout da janela da GUI é definido. A janela contém campos de texto para inserir um email e uma senha, dois botões para selecionar pastas para anexos e planilhas, e um botão "Salvar".

4. **Criação da janela da GUI**: Uma janela é criada com o título "Principal" e o layout definido anteriormente.

5. **Loop de eventos**: Um loop infinito é iniciado que mantém a janela aberta. O programa lê os eventos da janela e os valores dos campos de entrada. Se o evento for o fechamento da janela, o loop é interrompido e o programa termina. Se o evento for o clique no botão "Salvar", o programa recupera os valores inseridos nos campos de entrada e os imprime.

## Utilidade

Este projeto pode ser útil para qualquer situação em que seja necessário coletar informações do usuário através de uma GUI, como um email e uma senha, e permitir que o usuário selecione pastas para anexos e planilhas. Por exemplo, pode ser usado em um aplicativo de email para coletar as credenciais do usuário e permitir que o usuário selecione pastas para anexos de email e planilhas.
