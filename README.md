# Atualizar arquivos XML

## Descrição
Este projeto consiste em realizar algumas operações matemáticas em determinados arquivos XML, onde estes serão os arquivos que contenham
um CPNJ que foi escrito no arquivo `cnpj.csv`.

---
## Requisitos
* `Python - versão 3.7` - [Download](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)
    * Para instalar o Python de forma correta, basta fazer o Download e na tela inicial, marcar o checkbox "Add Python 3.7 to PATH" e clicar em "Install Now"
    ![](imgs/install.png)
* `pip (Gerenciador de pacotes do Python)`

---
## Dependências

**OBS: Para abrir uma janela de comando no diretório corrente, segure a tecla `Shift` e clique com o botão direito do mouse em algum ponto do espaço da pasta, após isso, clique na opção "Abrir janela de comando aqui"**

![](imgs/command.png)

**Tanto o PowerShell quanto o Prompt de Comando, irão realizar as mesmas ações, portanto, a escolha do mesmo fica a critério do usuário.**

Para instalar as dependências, abra PowerShell/prompt de comando no diretório corrente e execute o comando abaixo :

* `python -m pip install -r requirements.txt --user`

---
## Como usar

Para executar o programa, abra um PowerShell/Prompt de Comando na pasta corrente e como parâmetro de execução do mesmo é preciso passar a pasta onde contém os arquivos XML ou um arquivo XML da pesquisa que foi realizada na OLX e como parâmetro opcional, você pode escolher o nome da planilha que será gravado os números.:

* `cd src`
* **Comando para exibir ajuda**
    * `python main.py -h`
* **Executa o programa passando todos os arquivos XML que estão localizados na pasta `input`, onde serão analisados todos os CNPJ que foram escritos no arquivo `cnpj.csv`.**:
    
    * `python main.py -f ..\\input --cnpj ..\\cnpj.csv` 

* **Executa o programa passando somente um arquivo XML para ser analisado:**
    * `python main.py -f ..\\input\\35190912331433000109550010000399671725554367.xml --cnpj ..\\cnpj.csv` 

A saída do programa será gravada na pasta `output`, onde esta contem o arquivo XML que foi atualizado.

---