#pip install opencv-python-headless matplotlib

import cv2
import matplotlib.pyplot as plt

def display_histogram(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not read the image.")
        return

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# (specify image, 
    #specify chaneel for gray scale there is only 1 channel,
    # this is basically for mask if it is None histogram calculated for whole image, 
    # basically total number of bins , 
    # range )

    plt.figure(figsize=( 8, 6))  # 8 ,6 in inches
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.plot(hist)
    plt.grid(True)
    plt.show()

image_path = './image.jpg'
display_histogram(image_path)