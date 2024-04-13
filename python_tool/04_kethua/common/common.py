# lib logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)

class StepStaus():
    SUCCESSED = "SUCCESSED"
    FAIL = "FAIL"
    OK = "1"
    NOT_OK = "0"

class Common_Steps():
    def __init__(self, module): 
        self.Module = module
        self.State = None
        self.Result = None
    def LetStart(self):
        self.State = "Start"
        logging.info(f"========================")
        logging.info(f"{self.State} genenrate VSMD with {self.Module}")
        logging.info(f"''''''''''''''''''''''''")

    def LetEnd(self):
        self.State = "End"
        logging.info(f"========================")
        logging.info(f"{self.State} genenrate VSMD with {self.Module} =====> {self.Result}")
        logging.info(f"''''''''''''''''''''''''")