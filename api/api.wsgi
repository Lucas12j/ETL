#! /usr/bin/python3
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/api/')
from api import app as application

