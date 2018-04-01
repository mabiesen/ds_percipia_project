import sys
import getopt
from cli_JSON_Interface import ds_Fetch_Wrapper
from cli_help import help_Info
# Commands
# -vpn              *open vpn program
# -ssh              *ssh to machine, need client and machine arg
# -client           *return whole client
# -t                *get client top tier values
# -l                *list of clients
# -w                *go to client's ds page
#
# -h
dis = ds_Fetch_Wrapper()
try:
    opts,args=getopt.getopt(sys.argv[1:],"s:t:n:l:w:c:r:h",['ssh=','section=','notes=','help','list-all','web=','client=','remote-info='])
    for opt,arg in opts:
        if opt in ["-h","--help"]:
            x = help_Info()
            x.print_all_help_info()
            sys.exit()

        elif opt in ["-l","--list-all"]:
            dis.list_all_clients()

        elif opt in ["-w","--web"]:
            print(arg)
            dis.goto_client_page(arg.strip())

        elif opt in ["-t","--section"]:
            myargs = arg.split(",")
            dis.get_top_section_one_client(myargs[0].strip(),myargs[1].strip())

        elif opt in ["-s","--ssh"]:
            myargs = arg.split(",")
            dis.ssh_into(myargs[0].strip(),myargs[1].strip())

        elif opt in ["-n","--notes"]:
            dis.get_client_notes(arg.strip())

        elif opt in ["-c","--client"]:
            dis.get_all_for_client(arg.strip())

        elif opt in ["-r","--remote-info"]:
            myargs = arg.split(",")
            dis.get_client_product_info(myargs[0].strip(),myargs[1].strip())

except getopt.GetoptError:
    print ("Error!  Let me assist : ) ......")
    x=help_Info()
    x.print_all_help_info()
    sys.exit(2)
