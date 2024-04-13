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
from common.common import StepStaus,Common_Steps

def Read_argument():
    # init parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="write args")
    # Options for tool
    parser.add_argument("-m", "--module", help="prepare generate compile execute report", nargs='+', default=None)
    parser.add_argument("-d", "--debug", help="enable debug", nargs='+', default=None)
    return parser.parse_args()

class mConfig():
    pass

class RunTool(Common_Steps):
    Mytest= None
    # chuws cacs bien khi init
    def __init__(self, module, debug): 
        self.Module = module

        if debug == '1':
            self.Debug = 1
        else:
            self.Debug = 0

        self.Myconfig = mConfig()
        super().__init__(self.Module)
    
    def Start(self):
        self.Result = StepStaus.FAIL
        self.LetStart()

        logging.info("dhhdhdd")
        if (self.Debug) != 1:
            self.Result = StepStaus.SUCCESSED
        else:
            self.Result = StepStaus.FAIL

        self.LetEnd()

if __name__ == '__main__':
    Argument = Read_argument()
    # print(Argument.options, Argument.debug)
    logging.info("module = %s  debug = %s",Argument.module[0],Argument.debug[0])
    RunNew = RunTool(Argument.module[0],Argument.debug[0])
    RunNew.Start()