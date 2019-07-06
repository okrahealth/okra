"""Functions for interacting with jupyter notebook(s)"""

import nbformat as nbf
import os

def create_playbook(owner_info, directory = '.'):
    nb = nbf.v4.new_notebook()
    nb_name = owner_info[0] + '_' + owner_info[1] + '_' + owner_info[2] + '.ipynb'
    nbf.write(nb, os.path.join(directory, nb_name))
    return os.path.join(directory, nb_name)
