# lib parser
import argparse
# lib logging
import logging
import os
import subprocess

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)

class StepStatus():
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'
    OK = "1"
    NOT_OK = "0"


class CommonStep():
    def __init__(self,Module):
        self.Module = Module.upper()
        self.State = None
        self.Result = None

    def LetStart(self):
        self.State = "Start"
        logging.info(f"*************************************")
        logging.info(f" {self.State} generate VSMD report for module {self.Module}")
        logging.info(f"*************************************")

    def LetEnd(self):
        self.State = "End"
        logging.info(f"*************************************")
        logging.info(f" {self.State} generate VSMD report for module {self.Module} ===> [{self.Result}]")
        logging.info(f"*************************************\n")

    def RunCmd(Command: list, Shell=None):
        UseShell = True
        if Shell:
            UseShell = False
        try:
            log = subprocess.run(Command, shell=UseShell, capture_output=True, text=True)
            print(log)
            if type(log) == bytes:
                log = log.decode("utf-8")
            logging.info(log.args)
            if log.stdout:
                logging.info(log.stdout)
            if log.stderr:
                logging.info(log.stderr)
            if log.returncode:
                return False, str(log)
            else:
                return True, str(log)
        except subprocess.CalledProcessError as e:
            logging.error(e)
            return False, str(e)
    
# Create Director
def Make_Dir(path):
    if not os.path.isdir(path):
        os.makedirs(path, mode = 0o777, exist_ok= True)
        logging.info(f'Created Done {path}')
