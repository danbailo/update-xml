import xmltodict

with open('NF_000067228_ChaveAcesso_35190711272246000481550010000672281733208444.xml') as fd:
    doc = xmltodict.parse(fd.read()) 

    vICMS = doc['nfeProc']['NFe']['infNFe']['det']['imposto']["ICMS"]["ICMS00"]["vICMS"]
    
    #REGRA 1 E REGRA 3
    vBC_PIS = doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["vBC"]
    new_vBC_PIS = str(round(eval(vBC_PIS+'-'+vICMS),2))
    doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["vBC"] = new_vBC_PIS

    vBC_COFINS = doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["vBC"]
    new_vBC_COFINS = str(round(eval(vBC_COFINS+'-'+vICMS),2))
    doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["vBC"] = new_vBC_COFINS

    #################################################################################

    #REGRA 2
    pPIS = doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["pPIS"]
    new_vPIS = str(round(eval(pPIS+'*'+new_vBC_PIS),2))
    new_vPIS = str(round(eval(new_vPIS+'*0.01'),2))
    doc['nfeProc']['NFe']['infNFe']['det']['imposto']["PIS"]["PISAliq"]["vPIS"] = new_vPIS

    #REGRA 4
    pCOFINS = doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["pCOFINS"]
    new_vCOFINS = str(round(eval(pCOFINS+'*'+new_vBC_COFINS),2))
    new_vCOFINS = str(round(eval(new_vCOFINS+'*0.01'),2))
    doc['nfeProc']['NFe']['infNFe']['det']['imposto']["COFINS"]["COFINSAliq"]["vCOFINS"] = new_vCOFINS

    #REGRA 5
    doc['nfeProc']['NFe']['infNFe']["total"]["ICMSTot"]["vPIS"] = new_vPIS
    doc['nfeProc']['NFe']['infNFe']["total"]["ICMSTot"]["vCOFINS"] = new_vCOFINS

with open('result.xml', 'w') as result_file:
    result_file.write(xmltodict.unparse(doc,full_document=False))    