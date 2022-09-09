import os
import random

import numpy as np
import cv2
import matplotlib.pyplot as plt

import util


output_dir = './output'

for iteration in range(2000):

    flag = np.ones((500, 1000, 4), dtype=np.uint8) * 255

    upper_bound = random.randint(0, 3)
    for j in range(upper_bound):
        rect_init_y = random.randint(0, 500)
        flag = cv2.rectangle(flag,
                             (0, rect_init_y),
                             (1000, rect_init_y + random.randint(0, 500)),
                             (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255),
                             -1)

    if random.randint(0, 1) == 0:
        flag = cv2.circle(flag,
                          (random.randint(0, 1000), random.randint(0, 500)),
                          random.randint(0, 500),
                          (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255),
                          -1)

    random_object = cv2.imread(os.path.join('.', 'imgs',
                                            os.listdir('./imgs')[random.randint(0, len(os.listdir('./imgs')) -1)]), -1)
    random_object = cv2.resize(random_object, (200, int(random_object.shape[0] * 200 / random_object.shape[1])))

    x0 = random.randint(0, 800)
    y0 = random.randint(0, 500 - int(random_object.shape[0] * 200 / random_object.shape[1]))

    flag = util.overlay_transparent(flag, random_object, x0, y0)

    cv2.imwrite(os.path.join(output_dir, '{}.png'.format(str(iteration).zfill(5))), flag)
