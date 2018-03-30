from cli_JSON_Interface import ds_Fetch_Wrapper

## Main Testing
dis = ds_Fetch_Wrapper("blah",'name')

# PASSED
# dis.get_top_section_all_clients('contact')

# PASSED
# dis.get_top_section_one_client(21,'product')

# PASSED
dis.list_all_clients()

# PASSED
# dis.pretty_print_json()

# PASSED
dis.get_client_reference(73)

# PASSED
# dis.ssh_into(21,"Parallax")

#  NEED FORM ENTRY
# dis.goto_client_page(79)

# dis.open_vpn()
# dis.audit_clients()
