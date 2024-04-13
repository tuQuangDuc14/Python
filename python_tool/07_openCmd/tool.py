import subprocess

class OpenTool():
    def __init__(self):
        pass
   
    def RunCmd(self,Command: list, Shell=None):
        UseShell = True
        if Shell:
            UseShell = False
        try:
            log = subprocess.run(Command, shell=UseShell, capture_output=True, text=True)
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
       
    def run(self):
        self.Path_EB = "D:/Install/Enterprise_Architect/AE_install/EA.exe"
        Rev, Log = self.RunCmd(self.Path_EB)
       