import argparse
import sys
import os

def get_args():
	parser=argparse.ArgumentParser(
		prog="main.py",
		description="Atualiza os campos pré-definidos dos XMLs contendo determinado CNPJ emitente."
	)

	parser.add_argument("-f","--file",
		type=str,
        required=True,
		metavar="arquivo.xml|diretório",
		help="Caminho do XML ou do diretório que contem o(s) XML(s). Em caso de dúvidas, leia o arquivo README.md",
	)

	parser.add_argument("--cnpj",
		type=str,
        required=False,
		metavar="CNPJ.csv",
		default=os.path.join("..","CNPJ.csv"),
		help="Arquivo contendo os CNPJs emitentes. Em caso de dúvidas, leia o arquivo README.md",
	)

	return parser.parse_args()
