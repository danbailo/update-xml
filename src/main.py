from core import Xml
import utils

if __name__ == "__main__":

    args = utils.get_args()
    xml = Xml(args.file,args.cnpj)
    xml.update_fields()