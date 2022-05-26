from __future__ import division, absolute_import

global model_dir

model_dir = ''

def set_model_dir(input=''):
    global model_dir
    model_dir = input

def get_model_dir():
    return model_dir
