import cv2


def RecoverCLAHE(sceneRadiance):
    clahe = cv2.createCLAHE(clipLimit=1.3, tileGridSize=(4, 4))
    for i in range(3):
        sceneRadiance[:, :, i] = clahe.apply((sceneRadiance[:, :, i]))

    return sceneRadiance