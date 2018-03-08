import tensorflow as tf
from IPython.display import Image, display
import matplotlib.pyplot as plt
import numpy as np
import os
import inception
import cv2

pandaPath = "E:/python_programes/InceptionTf/testPIC/panda.jpg"
parrotPath = "E:/python_programes/InceptionTf/testPIC/Parrot.jpg"

inception.data_dir = "E:/python_programes/InceptionTf/model/"

inception.maybe_download()

model = inception.Inception()


def classify(image_path):
    image = cv2.imread(image_path)
    cv2.imshow("test", image)
    cv2.waitKey(0)
    pred = model.classify(image_path=image_path)
    model.print_scores(pred=pred, k=10, only_first_name=True)



classify(pandaPath)