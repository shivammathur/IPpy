import platform
import os

if platform.system() == 'Linux':
    os.system('sudo apt-get install iputils-ping')

os.system('python -m pip install --upgrade pip')
os.system('pip install tox codecov coveralls pytest-cov')
os.system('pip install -r requirements.txt')
os.system('pip install -r requirements_dev.txt')



