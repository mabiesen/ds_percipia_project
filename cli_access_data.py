import sys
import getopt

# Commands
# -vpn              *open vpn program
# -ssh              *ssh to machine, need client and machine arg
# -client           *return whole client
# -contacts         *get all contacts
# -methods          *get all methods
# -lc               *list of clients
# -web              *go to client's ds page
#
# -h
# -sb               *suppress blanks


def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:o",["ifile=","ofile="])
   except:
       pass

if __name__ == "__main__":
   main(sys.argv[1:])
