from core import Xml
import args

if __name__ == "__main__":
    args = args.get_args()
    xml = Xml(args.file,args.cnpj)    
    xml.update_fields()
    