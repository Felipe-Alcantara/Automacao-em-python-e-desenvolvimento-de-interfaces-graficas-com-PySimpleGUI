# 🤖 Automação de E-mail e Processamento de Boletos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![FreeSimpleGUI](https://img.shields.io/badge/FreeSimpleGUI-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*Sistema automatizado para download de anexos de e-mail e extração de dados de boletos*

</div>

## 📚 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Como Usar](#como-usar)
   - [Pré-requisitos](#pré-requisitos)
   - [Instalação](#instalação)
   - [Executando o Projeto](#executando-o-projeto)
- [Configuração](#configuração)
- [Interface](#🖼️-interface)
- [Tecnologias Utilizadas](#🛠️-tecnologias-utilizadas)
- [Estrutura do Projeto](#📂-estrutura-do-projeto)
- [Próximas Funcionalidades](#🔮-próximas-funcionalidades)
- [Contribuindo](#🤝-contribuindo)
- [Licença](#📝-licença)
- [Autor](#👨‍💻-autor)

---

## 📋 Sobre o Projeto

Este projeto é um robô de automação desenvolvido em Python que realiza as seguintes tarefas:

1. **Acessa uma conta de e-mail** configurada pelo usuário
2. **Baixa mensagens e anexos** automaticamente para uma pasta específica
3. **Processa os anexos** em busca de códigos de barras de boletos
4. **Extrai informações** importantes como:
   - Código digitável do boleto
   - Nome do arquivo
   - Data de vencimento
   - Valor do boleto
5. **Lança os dados em uma planilha** para fácil gerenciamento

### 💡 Casos de Uso

- Gestão financeira de empresas
- Controle de contas a pagar
- Automação de processos de cobrança
- Organização de boletos pessoais
- Redução de trabalho manual repetitivo

---

## ✨ Funcionalidades

- ✅ Interface gráfica intuitiva e moderna
- ✅ Configuração fácil de credenciais de e-mail
- ✅ Seleção personalizada de pastas
- ✅ Processamento automático de anexos
- ✅ Extração de dados de boletos via código de barras
- ✅ Exportação para planilha Excel

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Felipe-Alcantara/Automacao-em-python-e-desenvolvimento-de-interfaces-graficas-com-PySimpleGUI.git
   cd Automacao-em-python-e-desenvolvimento-de-interfaces-graficas-com-PySimpleGUI
   ```

2. **Crie um ambiente virtual** (recomendado)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install FreeSimpleGUI
   ```

### Executando o Projeto

```bash
python Bot.py
```

### Configuração

1. **Digite suas credenciais de e-mail** nos campos fornecidos
2. **Selecione a pasta de anexos** onde os arquivos serão salvos
3. **Selecione a pasta da planilha** onde o arquivo Excel será gerado
4. **Clique em "Salvar"** para confirmar as configurações

---

## 🖼️ Interface

A aplicação possui uma interface gráfica simples e intuitiva com:

- 📧 **Campo de E-mail**: Para inserir seu endereço de e-mail
- 🔒 **Campo de Senha**: Campo seguro com caracteres ocultos
- 📁 **Seletor de Pasta de Anexos**: Para escolher onde salvar os anexos baixados
- 📊 **Seletor de Pasta de Planilha**: Para escolher onde salvar a planilha gerada
- 💾 **Botão Salvar**: Para confirmar todas as configurações

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Linguagem de programação principal
- **[FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGUI)** - Framework para interface gráfica (fork open-source do PySimpleGUI)

### Por que FreeSimpleGUI?

O projeto originalmente usava PySimpleGUI, mas foi migrado para o **FreeSimpleGUI** devido à mudança de licenciamento do PySimpleGUI para um modelo comercial. O FreeSimpleGUI é:
- ✅ Totalmente gratuito e open-source
- ✅ Compatível com o código PySimpleGUI original
- ✅ Mantém todas as funcionalidades

---

## 📂 Estrutura do Projeto

```
📦 Automacao-em-python-e-desenvolvimento-de-interfaces-graficas-com-PySimpleGUI
┣ 📜 Bot.py           # Script principal da aplicação
┣ 📜 README.md        # Documentação do projeto
┣ 📜 LICENSE          # Licença do projeto
┗ 📁 .venv            # Ambiente virtual Python (criado localmente)
```
## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar este projeto:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Felipe Alcantara**

- GitHub: [@Felipe-Alcantara](https://github.com/Felipe-Alcantara)

---

## ⭐ Mostre seu apoio

Se este projeto foi útil para você, considere dar uma ⭐!

---

<div align="center">

**Desenvolvido com ❤️ e Python**

</div>
