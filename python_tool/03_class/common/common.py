# lib logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)

class My_data():
    Test_Name = "TS_01"
    Variable = 123
    Value = "done"

class Common_test():
    def __init__(self, step, debug): 
        self.Steps = step
        self.Debug = debug
        self.Test = My_data()
        
    def Start(self):
        print("data")
        print(self.Steps)
        print(self.Debug)
        print(self.Test.Test_Name)
        logging.info("from file common")