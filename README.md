# Atualizar arquivos XML

## Descrição
Este projeto consiste em realizar algumas operações matemáticas em determinados arquivos XML, onde estes serão os arquivos que contenham
um CPNJ que foi escrito no arquivo `cnpj.csv`.

---
## Requisitos
* `Python - versão 3.7` - [Download](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)
* `pip (Gerenciador de pacotes do Python)`

---
## Dependências

Para instalar as dependências, execute o comando abaixo num terminal/power sheel/prompt de comando de comando:

* `python -m pip install -r requirements.txt --user`

---
## Como usar

Para executar o programa, abra um terminal/power sheel/prompt de comando e como parâmetro de execução do mesmo é preciso passar o link da pesquisa que foi realizada na OLX e como parâmetro opcional, você pode escolher o nome da planilha que será gravado os números.:

* `cd src/`
* **Comando para exibir ajuda**
    * `python main.py -h`
* **Executa o programa passando todos os arquivos XML que estão localizados na pasta `input`, onde serão analisados todos os CNPJ que foram escritos no arquivo `cnpj.csv`.**:
    
    * `python main.py -f ..\\input --cnpj ..\\cnpj.csv` 

* **Executa o programa passando somente um arquivo XML para ser analisado:**
    * `python main.py -f ..\\input\\35190912331433000109550010000399671725554367.xml --cnpj ..\\cnpj.csv` 

A saída do programa será gravada na pasta `output`, onde esta contem o arquivo XML que foi atualizado.

---