import logging
import os
from datetime import datetime

## LOG_FILE - creates a time data log file in your logs folder.
# Code for creating the log path to create the LOG_FILE in your logs folder. 
 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

## logging.basicConfig - sets the rules for your logs on how it's written - enhances the time and date for each logging statement.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

