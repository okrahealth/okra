""" Command Line Interface utilities for Okra """
import sys

CLI_HELP = """
okra {task}

    {task}
        compute     Perform the 'compute' task.  

    {compute}

        repo        Check cache, clone repo if confirmed; create database and generate report.

    Optional Args

        -h --help   Print this help menu then exit.
"""
TASKS = ["compute"]

def print_help(good=True):
    print(CLI_HELP)
    if good:
        sys.exit(0)
    sys.exit(2)

def parse_args(args: list):
    """ Parse sys.argv arguments. """
        
    if len(args) < 2:
        sys.stderr.write("\nERROR: 'okra {task}' missing from cli\n")
        print_help()

    if args[1] == "compute":
        print("good one")

    else:
        sys.stderr.write("\nERROR: got {{task}}: {}, want one of {{task}}: {}\n".\
                format(args[1], ",".join(TASKS)))



    return True

