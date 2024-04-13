# lib parser
import argparse
# lib logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)

# Liệt kê các file và thư mục 
import glob
import os
from common.common import Common_test

def Read_argument():
    # init parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="write args")
    # Options for tool
    parser.add_argument("-o", "--options", help="prepare generate compile execute report", nargs='+', default=None)
    parser.add_argument("-d", "--debug", help="enable debug", nargs='+', default=None)
    return parser.parse_args()

class My_variable():
    Test_Name = "TS_01"
    Variable = 123
    Value = "done"

class RunTool():
    Mytest= None
    # chuws cacs bien khi init
    def __init__(self, step, debug): 
        if debug == '1':
            self.Debug = 1
        else:
            self.Debug = 0
        # set step 
        self.Steps = step
        # set Test
        self.Mytest = My_variable()
        print("Init ok ")
    
    def Start(self):
        x = os.path.join('F:\ThoNV_FrameWork\Z_FileC', "*.c")
        y = glob.glob(x)
        # print(self.Debug)
        # print(self.Steps)
        # print(self.Mytest.Test_Name)
        # print(self.Mytest.Variable)
        # print(self.Mytest.Value)
        Common_test(self.Debug, self.Steps).Start()

if __name__ == '__main__':
    Argument = Read_argument()
    # print(Argument.options, Argument.debug)
    logging.info("options = %s  debug = %s",Argument.options[0],Argument.debug[0])
    RunNew = RunTool(Argument.options[0],Argument.debug[0])
    RunNew.Start()