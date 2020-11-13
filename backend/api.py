#!/usr/bin/env python3

from   utils    import dbg_print, dbg_print_mult
from   datetime import datetime as dt
import pandas   as     pd
import numpy    as     np
import pickle
import sys
import os


# dummy API service function
def frag(parameters):
    return {'called': 'yes',
            'result': f'your input: {parameters["input"]}, it works!'}


