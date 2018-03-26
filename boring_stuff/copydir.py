import shutil
from datetime import datetime

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
        print("Copy {0} to {1} done".format(src, dest))
    except shutil.Error as e:
        print ("Copy {0} to {1} error:{2}".format(src, dest, e))
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

srcDir = "C:\\Program Files (x86)\\Steam\\userdata\\62752794\\262060\\remote\profile_1"
timestamp = datetime.now().strftime("%y%m%d%H%M%S")
destDir =  srcDir +"-" + timestamp

copyDirectory(srcDir, destDir)