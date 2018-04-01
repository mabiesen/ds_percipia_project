from cli_JSON_Interface import ds_Fetch_Wrapper
import pprint
## Main Testing
dis = ds_Fetch_Wrapper()

#PASS
#dis.get_top_section_all_clients('contact')

#PASS
#dis.get_top_section_one_client(77,'product')

# pprint(dis.mydata.json_data["Amangiri"]["product"])

# PASSED
#dis.list_all_clients()

# PASSED
#dis.pretty_print_json()

dis.get_all_for_client(75)

# Passed
#dis.get_client_notes("Amangiri")

# Passed - both number and name
#dis.get_client_reference(77)

#
#dis.ssh_into(21,"Parallax")

#  NEED FORM ENTRY
# dis.goto_client_page(77)

# dis.open_vpn()
# dis.audit_clients()
