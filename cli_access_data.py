import sys
import getopt
from cli_JSON_Interface import ds_Fetch_Wrapper
# Commands
# -vpn              *open vpn program
# -ssh              *ssh to machine, need client and machine arg
# -client           *return whole client
# -t                *get client top tier values
# -l                *list of clients
# -w                *go to client's ds page
#
# -h
# -sb               *suppress blanks
dis = ds_Fetch_Wrapper("https://ds.percipia.net/json.php?key=tzpbIHEDplsU_JRasqQJ",'name')
try:
    opts,args=getopt.getopt(sys.argv[1:],"st:hliw:")
    for opt,arg in opts:
        if opt=="-h":
            print 'help information'
            sys.exit()
        #pass - list dictionary all clients
        elif opt == "-l":
            dis.list_all_clients()
        #pass - go to client ds
        elif opt == "-w":       #BROKEN
            print(arg)
            dis.goto_client_page(arg.strip())
        #pass - go to client tier
        elif opt == "-t":
            myargs = arg.split(",")
            dis.get_top_section_one_client(myargs[0].strip(),myargs[1].strip())
        elif opt == "-s":
            myargs = arg.split(",")
            dis.ssh_into(myargs[0],myargs[1])
        elif opt == "-i":
            files = arg.split(",")
            print files
    #funtction(files)
except getopt.GetoptError:
    print 'help information'
    sys.exit(2)
