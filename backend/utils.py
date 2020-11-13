#!/usr/bin/env python3

import sys

# helper functions should be defined in this file
def dbg_print(what):
    """
    prints to stderr ( in flask log)
    input: LIST of anything
    """
    print("[!!]>>>[DEBUG]: ", what, file=sys.stderr)


def dbg_print_mult(what):
    """
    prints to stderr ( in flask log)
    input: LIST of anything
    """
    for wtf in what:
        print("[!!]>>>[DEBUG]: ", wtf, file=sys.stderr)