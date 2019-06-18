import time

import numpy as np
from PIL import ImageGrab
import cv2 as cv


def convert_image_to_cv_image(captured_image):
    # Convert RGB to BGR
    return cv.cvtColor(np.array(captured_image), cv.COLOR_BGR2RGB)

def main():
    while True:
        time_before_render = time.perf_counter()
        # if bounding box is None then the entire screen is copied.
        screenshot = ImageGrab.grab(bbox=None)
        opencv_image = convert_image_to_cv_image(screenshot)

        cv.imshow('window', opencv_image)

        time_after_render = time.perf_counter()
        interval = (time_after_render - time_before_render) * 1000
        # it seems that 11 ~ 12 fps in QHD(2560 x 1440) for rendering.
        # anyway, I think it is enough to continue.
        print('Rendering inverval: {}', interval * 1000)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
