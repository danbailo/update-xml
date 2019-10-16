from core import Xml

if __name__ == "__main__":
    # xml = Xml("../input/NF 4762 Com dois itens.xml")
    # xml = Xml("../input/NF_000067228_ChaveAcesso_35190711272246000481550010000672281733208444.xml")
    xml = Xml("../input")

    # print(xml)
    xml.update_fields()