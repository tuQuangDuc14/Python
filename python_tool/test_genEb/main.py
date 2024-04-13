# lib logging
import logging
import subprocess

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)


def RunCmd(Command: list, Shell=None):
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

# remove project
options = ['-data', 'D:/test_genEb/workplace', 'deleteProject', '-d', 'EbProject']
command = ['C:/EB/tresos_28.2/bin/tresos_cmd.bat'] + options
RunCmd(command)

# import project
options = [r'-data', 'D:/test_genEb/workplace', r'importProject', '-c', 'D:/test_genEb/EbProject']
command = ['C:/EB/tresos_28.2/bin/tresos_cmd.bat'] + options
RunCmd(command)

# generate
options = [r'-data', 'D:/test_genEb/workplace', r'generate', "EbProject", '-o', 'D:/test_genEb/output']
command = ['C:/EB/tresos_28.2/bin/tresos_cmd.bat'] + options
RunCmd(command)