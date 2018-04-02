import urllib2
import json
import numbers
import sys
import pprint


# responsible for fetching json
class load_Json:
    #PASS
    def get_data_from_web(self,thisurl):
        try:
            contents = urllib2.urlopen(thisurl).read()
            return contents
        except:
            print("Failed to retrievew data from url.")
            return "invalid"
    #PASS
    def load_json_data_from_string(self,str_data):
        try:
            j_data = json.loads(str_data)
            return j_data
        except:
            print("Failed to load json from a provided string")
            return "invalid"
    #PASS
    def load_json_data_from_file(self,filepath):
        try:
            j_data = json.load(open(filepath))
            return j_data
        except:
            print("Failed to load json from file")
            return "invalid"
    #PASS
    def write_json_to_file(self,filepath,strdata):
        try:
            with open(filepath,'w') as file:
                file.write(strdata)
        except:
            print("Could not write to file, maybe try changing filepath.")


# Responsible for accessing json data
class json_Data_Wrapper:

    # get field from specific level 2 entry
    def get_level_three_field(self,this_json,top_field_key,second_field_key,second_field_value,third_field_key,return_field_key):
        try:
            # get all products
            x =[]
            x = this_json[top_field_key]

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
    def get_level_two_field(self,this_json,top_field,check_field_key,check_field_value,return_field_key):
        x = this_json[top_field]
        for g in x:
            for a,b in g.iteritems():
                if a == check_field_key:
                    if b == check_field_value:
                        return g[return_field_key]
        return "invalid"

    #PASS
    def pretty_print_json(self, thisdata):
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
        pp.pprint(thisdata)
