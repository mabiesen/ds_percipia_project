import urllib2
import json
import numbers
import sys
import pprint


# responsible for fetching json
class load_Json:

    def get_data_from_web(self,thisurl):
        try:
            contents = urllib2.urlopen(thisurl).read()
            return contents
        except:
            return "invalid"

    def load_json_data_from_web(self,str_data):
        try:
            j_data = json.loads(str_data)
            return j_data
        except:
            return "invalid"

    def load_json_data_from_file(self,filepath):
        try:
            j_data = json.load(open(filepath))
            return j_data
        except:
            return "invalid"

    def write_json_to_file(self,filepath,strdata):
        try:
            with open(filepath,'w') as file:
                file.write(strdata)
        except:
            print("Could not write to file, maybe try changing filepath.")


# Responsible for storing and accessing json data
class json_Data_Wrapper:

    #desirable fields: access, contact, note, product
    def __init__(self, thisurl, thisdictfield):
        self.json_filename = "C:\\Users\\mabie\\Downloads\\json_ds.txt"
        # instantiate json loader
        self.myjson = load_Json()
        self.json_data = self.myjson.load_json_data_from_web(self.myjson.get_data_from_web(thisurl))

        # if loading json data from web did not work, load from file
        if self.json_data != "invalid":
            self.myjson.write_json_to_file(self.json_filename, self.myjson.get_data_from_web(thisurl))
        else:
            self.json_data = self.myjson.load_json_data_from_file(self.json_filename)
            if self.json_data == "invalid":
                print("Could not get data from web or from file")
                print("Try again?  You can try changing filepath, if there is no existing file you'll need internet connection.")
                sys.exit()

        # second argument is a first level identifyer
        self.name_dict = self.set_by_top_field_dictionary(self.json_data,thisdictfield)

    # create our dictionary
    def set_by_top_field_dictionary(self,this_data, name):
        mydict = {}
        for i in range(0, len(this_data)):
            mydict[this_data[i][name]]= this_data[i]["id"]
        return mydict

    # get field from specific level 2 entry
    def get_level_three_field(self,num_word,top_field_key,second_field_key,second_field_value,third_field_key,return_field_key):
        try:
            # get all products
            x =[]
            x = self.get_top_field_redirection(num_word, top_field_key)

            # get the correct product, if multilple alert user but return first
            matches = []
            for g in x:
                if g[second_field_key] == second_field_value:
                    matches.append(g)

            # get the first login requested field
            value = matches[0][third_field_key][0][return_field_key]
            return value
        except:
            return "invalid"


    # get field from specific level 2 entry
    def get_level_two_field(self,num_word,top_field,check_field_key,check_field_value,return_field_key):
        x = []
        x = self.get_top_field_redirection(num_word, top_field)
        for g in x:
            for a,b in g.iteritems():
                if a == check_field_key:
                    if b == check_field_value:
                        return x[0][return_field_key]
        return "invalid"

    # overloading for get field data functions below
    def get_top_field_redirection(self,num_word, thisfield):
        if isinstance(num_word,numbers.Number):
            try:
                return self.json_data[this_client][this_field]
            except:
                return "invalid"
        else:
            try:
                return self.json_data[self.get_dict_entry(this_client)][this_field]
            except:
                return "invalid"

    def get_dict_entry(self,num_word):
        try:
            if not isinstance(num_word,numbers.Number):
                print num_word
                return num_word, self.name_dict[num_word]
            else:
                for x,y in self.name_dict.iteritems():
                    if y == num_word:
                        return x,y
            return "invalid","invalid"
        except:
            return "invalid","invalid"

    def pretty_print_json(self):
        # format for pprintt
        def my_safe_repr(object, context, maxlevels, level):
            typ = pprint._type(object)
            if typ is unicode:
                try:
                    object = str(object)
                except:
                    object = object
            return pprint._safe_repr(object, context, maxlevels, level)

        pp = pprint.PrettyPrinter(indent=2)
        pp.format = my_safe_repr
        pp.pprint(self.json_data)
