# ds_percipia_project

## PURPOSE

You know how some clients block our access to the ds?

You know how burdensome it can be to log in/out of the ds?

This project aims to alleviate those burdens!!

Easily access information, ssh into machines, etc.

## USAGE

python cli.py runs the Program

must add arguments appropriate to output

see below for options

#### HELP INFO

-l Alt:  --list-all.  Lists all clients and their ids.  This option requires no arguments.  NOTE:  All commands can use either client name or id, this is useful!

-s Alt:  --ssh. Ssh into selected product. This option requires client and product, separated by comma

-t Alt:  --section. This option gets all data for client and top level section. Requires client and section separated by comma

-w Alt:  --web. This option takes you to client ds page (must be logged in). Requires client.

-n Alt:  --notes. This option provides top level client notes. Requires client.

-c Alt:  --client Get all client data. Requires client.

-r Alt:  --remote Provide product connection info. Requires client and product separated by comma.

-h Alt:  --help Display all of this information from the command line!!!
