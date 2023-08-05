
import os
import subprocess

# set environmental variables for local development here
os.environ['SECRET_KEY'] = 'mySuperSecureKey'

subprocess.call(['flask', 'run', '--port', '8006', '--debug'])
