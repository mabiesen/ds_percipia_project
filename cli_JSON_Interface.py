# responsible for business logic
# responsible for formatting and printing
import os
import subprocess
import numbers
from manage_JSON_Data import json_Data_Wrapper
from manage_JSON_Data import load_Json

# responsible for business logic + printing
# user entries interface with json data here
class ds_Fetch_Wrapper:

    def __init__(self):
        #instance to manage json data
        self.mydatamanager = json_Data_Wrapper()

        #instance to manage fetching json
        self.myfetcher = load_Json()

        #url to fetch
        self.fetchurl = "barnacles"

        #filename for json storage
        self.json_filename = "C:\\Users\\mabie\\Downloads\\json_ds.txt"

        # get json data
        self.json_data = self.myfetcher.load_json_data_from_string(self.myfetcher.get_data_from_web(self.fetchurl))

        # if loading json data from web did not work, load from file
        if self.json_data != "invalid":
            self.myfetcher.write_json_to_file(self.json_filename, self.myfetcher.get_data_from_web(self.fetchurl))
        else:
            self.json_data = self.myfetcher.load_json_data_from_file(self.json_filename)
            if self.json_data == "invalid":
                print("Could not get data from web or from file")
                print("Try again?  You can try changing filepath, if there is no existing file you'll need internet connection.")
                sys.exit()

        #create a dict of names and json for client
        self.name_json_dict = self.set_name_plus_json_dict_from_list(self.json_data,'name')

####################################################################
# DICTIONARY CREATION AND REFERENCE

    # Name dict with json
    def set_name_plus_json_dict_from_list(self, this_data, name):
        mydict = {}
        for i in range(0, len(this_data)):
            mydict[this_data[i][name]]= this_data[i]
        return mydict

    #  Get JSON from name or ID
    def get_json_from_name_or_id(self, num_word):
        try:
            try:
                num_word = int(num_word)
            except:
                pass
            if isinstance(num_word, numbers.Number):
                print("here")
                for x,y in self.name_json_dict.iteritems():
                    if y['id'] == num_word:
                        return y
            else:
                return self.name_json_dict[num_word]
        except:
            return {'id': 'invalid', 'name': 'invalid'}

########################### End Dictionary Methods ##########################

#############################################################################
# GENERICS, USED FOR GETTING THINGS FOR ALL CLIENTS
    # Contact, etc.
    def get_top_section_all_clients(self,this_field):
        print("Here are all clients listed by reference id:\n\n")
        for g,h in self.name_json_dict.iteritems():
           print(g)
           print("\n")
           self.get_top_section_one_client(h['name'],this_field)

    def get_top_section_one_client(self,this_client, this_field):
           client_field_json = self.get_json_from_name_or_id(this_client)[this_field]
           print("This is the section detail for client " +str(this_client)+ " for field " + this_field + "\n")
           self.mydatamanager.pretty_print_json(client_field_json)

    def list_all_clients(self):
        print("Here is a list of clients and their associated table ID:\n\n")
        for x,y in self.name_json_dict.iteritems():
            print(str(y["id"]) + "\t" + x)

    def pretty_print_json(self):
        self.mydatamanager.pretty_print_json(self.json_data)

########################### End Generics ###################################

###########################################################################
# BELOW THIS LINE FETCHES SPECIFIC CLIENT INFO

    # used to find empty contacts, empty products, empty
    def audit_clients():
        # Find all clients with blank phone numbers

        # Find all client contacts with blank phone number or email

        # etc.
        pass

    def get_client_product_info(self,client,product):
        client_json = self.get_json_from_name_or_id(client)
        # Find machine IP, user, password
        ip = self.mydatamanager.get_level_two_field(client_json,"product", "name", product,"ip")
        #num_word,top_field_key,second_field_key,second_field_value
        username = self.mydatamanager.get_level_three_field(client_json,"product","name",product,"login","user")
        password = self.mydatamanager.get_level_three_field(client_json,"product","name",product,"login","password")

        # before execupting putty, print info ip, uname, password
        print("CLIENT:\t\t" + client_json['name'])
        print("PRODUCT:\t" + product)
        print("ip:\t\t" + ip)
        print("username:\t" + username)
        print("password:\t" + password)


    # open new bash shell, execute ssh
    def ssh_into(self,client,product):
        client_json = self.get_json_from_name_or_id(client)
        # Find machine IP, user, password
        ip = self.mydatamanager.get_level_two_field(client_json,"product", "name", product,"ip")

        self.get_client_product_info(client,product)

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

    #
    def goto_client_page(self,num_word):
        client_json = self.get_json_from_name_or_id(num_word)
        url = "https://ds.percipia.net/?site=" + str(client_json['id'])
        subprocess.call(["cygstart", url])

    # return the ID and name of client
    def get_client_reference(self, num_word):
        client_json = self.get_json_from_name_or_id(num_word)
        print(str(client_json['id']) + "\t" + str(client_json['name']))

    def get_all_for_client(self,num_word):
        client_json = self.get_json_from_name_or_id(num_word)
        self.mydatamanager.pretty_print_json(client_json)

    def get_client_notes(self,num_word):
        client_json = self.get_json_from_name_or_id(num_word)
        print("Notes for Client " + client_json['name']+ "\n\n")
        print(client_json['note'])
