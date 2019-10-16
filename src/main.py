from core import Xml
import utils

if __name__ == "__main__":

    args = utils.get_args()

    # xml = Xml("../input","11272246000481")

    xml = Xml(args.file,args.cnpj)
    xml.update_fields()