import sys
import os
os.system('tox -e py' + sys.version[:3].replace('.', ''))
