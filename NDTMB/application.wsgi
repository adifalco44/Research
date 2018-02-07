import os, sys

PROJECT_DIR = os.path.join(os.path.split(os.path.realpath(__file__))[:-1])

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from run import app as application
