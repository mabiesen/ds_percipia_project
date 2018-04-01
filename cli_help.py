

class help_Info:

    def __init__(self):
        self.helplist = {
        "l":"Alt:  --list-all.\n\tLists all clients and their ids.\n\tThis option requires no arguments.\n\tNOTE:  All commands can use either client name or id, this is useful!",
        "s":"Alt:  --ssh.\n\tSsh into selected product.\n\tThis option requires client and product, separated by comma",
        "t":"Alt:  --section.\n\tThis option gets all data for client and top level section.\n\tRequires client and section separated by comma",
        "w":"Alt:  --web.\n\tThis option takes you to client ds page (must be logged in).\n\tRequires client.",
        "n":"Alt:  --notes.\n\tThis option provides top level client notes.\n\tRequires client.",
        "c":"Alt:  --client\n\tGet all client data.\n\tRequires client.",
        "r":"Alt:  --remote\n\tProvide product connection info.\n\tRequires client and product separated by comma."
        }

    def print_all_help_info(self):
        print("\n")
        print("For first timers:  Use client ID!\nIt is easiest, especially for multipart names\nTo get client ID, pipe the -l option to grep for client.\n")
        for x,y in self.helplist.iteritems():
            print("-" + x + "\t" + y + "\n")
