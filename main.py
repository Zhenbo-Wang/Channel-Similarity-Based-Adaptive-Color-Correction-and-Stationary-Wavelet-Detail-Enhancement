import time
import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceCLAHE import RecoverCLAHE
from sceneRadianceHE import RecoverHE

start_time = time.time()
np.seterr(over='ignore')
if __name__ == '__main__':
    pass

folder = "E:/test"


path = folder + "/input"
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        img = cv2.imread(folder + '/input/' + file)
        sceneRadiance = RecoverCLAHE(img)
        cv2.imwrite('E:/output/' + prefix + '.png', sceneRadiance)

