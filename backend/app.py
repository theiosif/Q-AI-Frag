#!/usr/bin/env python3

from   flask  import Flask, request, jsonify
from   utils  import dbg_print, dbg_print_mult
import pandas as pd
import numpy  as np
import sklearn
import time
import sys
import api
import os


# declare constants
HOST = '0.0.0.0'
PORT = 8081
# The classics
DEBUG = True

# initialize flask application
app = Flask(__name__)

@app.route('/api/frag', methods=['POST'])
def build():

    # move interpreter's $PWD into the models/ folder
    starting_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(starting_dir)
    os.chdir("models")

    # now this can be used for loading stuff from relative paths
    model_dir = os.getcwd()
    if DEBUG:
        dbg_print(f'model_dir: {model_dir}')

    # get parameters from request
    # parameters = request.get_json()
    parameters = {'first': 'hello', 'second':'world'}

    # typecast parameters to int
    # params['intParamName'] = float(params['intParamName'])
    

    # call function
    result = api.frag(parameters)
    
    return jsonify(result)


if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
