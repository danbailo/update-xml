import xmltodict
import os

class Xml:
    def __init__(self, file = None, cnpj = None):        
        self.__xml = file
        self.__cpnj = cnpj
    
    def get_xml(self):
        if os.path.isfile(self.__xml):
            if self.__xml[-4:] == ".xml": 
                return [self.__xml.split("/")[-1]]
            print("Por favor, entre com um arquivo .xml!")
            exit(-1)
        if os.path.isdir(self.__xml):
            xmls = [xml for xml in os.listdir(self.__xml) if xml[-4:]==".xml"]
            if len(xmls) == 0: return None
            return xmls

    def __check_cnpj(self, doc):
        if self.__cpnj == doc['nfeProc']['NFe']['infNFe']["emit"]["CNPJ"]:
            return True
        return False            

    def update_fields(self):
        count = 0
        for xml in self.get_xml():      
            if len(self.get_xml()) == 1: 
                fd = open(os.path.join(self.__xml))
            else : 
                fd = open(os.path.join(self.__xml,xml))
            
            doc = xmltodict.parse(fd.read())
            if not self.__check_cnpj(doc):
                # print("O CNPJ {cnpj} não foi encontrado!\n".format(cnpj=self.__cpnj))
                continue
            count = 1
            print('O CNPJ "{cnpj}" foi encontrado no arquivo "{xml}"'.format(cnpj=self.__cpnj, xml=xml))

            if isinstance(doc['nfeProc']['NFe']["infNFe"]["det"], list):
                for i in range(len(doc['nfeProc']['NFe']["infNFe"]["det"])):
                    new_doc = doc.copy()
                    vICMS = new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["ICMS"]["ICMS00"]["vICMS"]
                    
                    #REGRA 1 E REGRA 3
                    vBC_PIS = new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["PIS"]["PISAliq"]["vBC"]
                    new_vBC_PIS = str(round(eval(vBC_PIS+'-'+vICMS),2))
                    new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["PIS"]["PISAliq"]["vBC"] = new_vBC_PIS

                    vBC_COFINS = new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["COFINS"]["COFINSAliq"]["vBC"]
                    new_vBC_COFINS = str(round(eval(vBC_COFINS+'-'+vICMS),2))
                    new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["COFINS"]["COFINSAliq"]["vBC"] = new_vBC_COFINS

                    #################################################################################

                    #REGRA 2
                    pPIS = new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["PIS"]["PISAliq"]["pPIS"]
                    new_vPIS = str(round(eval(pPIS+'*'+new_vBC_PIS),2))
                    new_vPIS = str(round(eval(new_vPIS+'*0.01'),2))
                    new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["PIS"]["PISAliq"]["vPIS"] = new_vPIS

                    #REGRA 4
                    pCOFINS = new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["COFINS"]["COFINSAliq"]["pCOFINS"]
                    new_vCOFINS = str(round(eval(pCOFINS+'*'+new_vBC_COFINS),2))
                    new_vCOFINS = str(round(eval(new_vCOFINS+'*0.01'),2))
                    new_doc['nfeProc']['NFe']['infNFe']['det'][i]['imposto']["COFINS"]["COFINSAliq"]["vCOFINS"] = new_vCOFINS

                    #REGRA 5
                    new_doc['nfeProc']['NFe']['infNFe']["total"]["ICMSTot"]["vPIS"] = new_vPIS
                    new_doc['nfeProc']['NFe']['infNFe']["total"]["ICMSTot"]["vCOFINS"] = new_vCOFINS
            else:
                new_doc = doc.copy()
                vICMS = new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["ICMS"]["ICMS00"]["vICMS"]
                
                #REGRA 1 E REGRA 3
                vBC_PIS = new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["vBC"]
                new_vBC_PIS = str(round(eval(vBC_PIS+'-'+vICMS),2))
                new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["vBC"] = new_vBC_PIS

                vBC_COFINS = new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["vBC"]
                new_vBC_COFINS = str(round(eval(vBC_COFINS+'-'+vICMS),2))
                new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["vBC"] = new_vBC_COFINS

                #################################################################################

                #REGRA 2
                pPIS = new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["pPIS"]
                new_vPIS = str(round(eval(pPIS+'*'+new_vBC_PIS),2))
                new_vPIS = str(round(eval(new_vPIS+'*0.01'),2))
                new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["vPIS"] = new_vPIS

                #REGRA 4
                pCOFINS = new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["pCOFINS"]
                new_vCOFINS = str(round(eval(pCOFINS+'*'+new_vBC_COFINS),2))
                new_vCOFINS = str(round(eval(new_vCOFINS+'*0.01'),2))
                new_doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["vCOFINS"] = new_vCOFINS

                #REGRA 5
                new_doc['nfeProc']['NFe']['infNFe']["total"]["ICMSTot"]["vPIS"] = new_vPIS
                new_doc['nfeProc']['NFe']['infNFe']["total"]["ICMSTot"]["vCOFINS"] = new_vCOFINS
            
            fd.close()
            with open(os.path.join("..","output",xml[:-4]+" - ALTERADO.xml"), 'w') as result_file:
                print(f'Arquivo "{xml}" foi alterado com sucesso!\n')
                result_file.write(xmltodict.unparse(new_doc,full_document=False))
        if count == 0 :
            print("O CNPJ {cnpj} não foi encontrado em nenhum arquivo!\n".format(cnpj=self.__cpnj))         