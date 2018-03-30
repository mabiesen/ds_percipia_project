# responsible for business logic
# responsible for formatting and printing
import os
import subprocess
from manage_JSON_Data import json_Data_Wrapper

# responsible for business logic + printing
# user entries interface with json data here
class ds_Fetch_Wrapper:

    def __init__(self):
        self.mydata = json_Data_Wrapper("somesite",'name')

    def get_whole_company():
        pass

    # Contact, etc.
    def get_top_section_all_clients(self,this_field):
        print("Here are all clients listed by reference id:\n\n")
        for g in range(1,len(self.mydata.name_dict)):
           print(list(self.mydata.name_dict.keys())[g])
           print("\n")
           self.get_top_section_one_client(g,this_field)

    def get_top_section_one_client(self,this_client, this_field):
           somet = self.mydata.get_top_field_redirection(this_client,this_field)
           print("This is the section detail for client " + " for field " + field)
           for a in somet:
               try:
                   for b,c in a.iteritems():
                       if len(b) > 6:
                           print("\t" + b + ":\t" + str(c))
                       else:
                           print("\t" + b + ":\t\t" + str(c))
                   ct = ct + 1
               except:
                   pass
               print("\n")
           print("---------------------------------------------")


    def list_all_clients(self):
        print("Here is a list of clients and their associated table ID:\n\n")
        for x,y in self.mydata.name_dict.iteritems():
            print(str(y) + "\t" + x)

    # used to find empty contacts, empty products, empty
    def audit_clients():
        # Find all clients with blank phone numbers

        # Find all client contacts with blank phone number or email

        # etc.
        pass

    # open new bash shell, execute ssh
    def ssh_into(self,client,product):

        # Find machine IP, user, password
        ip = self.mydata.get_level_two_field(client,"product", "name", product,"ip")
        #num_word,top_field_key,second_field_key,second_field_value
        username = self.mydata.get_level_three_field(client,"product","name",product,"login","user")
        password = self.mydata.get_level_three_field(client,"product","name",product,"login","password")

        # before execupting putty, print info ip, uname, password
        print("CLIENT:\t\t" + str(client))
        print("PRODUCT:\t" + product)
        print("ip:\t\t" + ip)
        print("username:\t" + username)
        print("password:\t" + password)

        # Open putty, input and execute ssh
        cmd = "/cygdrive/c/Program\ Files/PuTTY/putty.exe -ssh "+ ip +" 22"
        print('Opening SSH connection with putty...')

        try:
            os.system(cmd)
        except:
            print("Failed.  Is putty installed?\n You may need to change the filepath\n")
            print("The current filepath/command-used is:\t" + cmd)


    # open vpn methods, possibly input data
    def open_vpn():
        pass

    def goto_client_page(self,client):
        # create url
        # if client is name, convert
        url = ""
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        if True:
            url = "https://ds.percipia.net/?site=" + str(client)
        else:
            client = self.mydata.name_dict[client]
            url = "https://ds.percipia.net/?site=" + str(client)

        subprocess.call(["cygstart", url])

    def get_client_reference(self, num_word):
        key, val = self.mydata.get_dict_entry(num_word)
        print(str(key) + "\t" + str(val))


    def pretty_print_json(self):
        self.mydata.pretty_print_json()
