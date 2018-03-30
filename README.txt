

Project flow:

User enters command, which instantiates and makes calls to interface, which
instantiates json wrapper

NOTE:  json data kept separate from wrapper for overhead and
separation of concerns

Numerical flow:

1.  cli
2.  cli_JSON interface
3.  JSON
