# copyfile(): copies content of file
# copy(): copyfile() + permissions mode + destination can be directory
# copy2(): copy() + copies metadata(file's creation and modification times)

import shutil

shutil.copy2("test","copfile") #src, #dst