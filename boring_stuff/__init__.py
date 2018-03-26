import logging
import os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) +"\.."
LOG_DIR = os.path.join(ROOT_DIR, "log")

DATESTAMP1 = datetime.now().strftime("%Y%m%d")
TIMESTAMP1 = datetime.now().strftime("%Y%m%d_%H%M%S")
TIMESTAMP2 = datetime.now().strftime("%Y%m%d_%a_%I%M%S_%p")

LOGGING_LEVEL = logging.DEBUG
logfilename = os.path.join(LOG_DIR, DATESTAMP1+ ".log")
logging.basicConfig(filename=logfilename, level=LOGGING_LEVEL, format=' %(asctime)s - %(levelname)s - %(message)s')

console = logging.StreamHandler()
logging.getLogger('').addHandler(console)