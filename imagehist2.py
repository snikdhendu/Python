import cv2
import matplotlib.pyplot as plt

def enhance_image(image_path):
    image=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error")
        return 
    equlized_image=cv2.equalizeHist(image)

    original_hist=cv2.calcHist([image],[0],None,[256],[0,256])
    equlized_hist=cv2.calcHist([equlized_image],[0],None,[256],[0,256])

    plt.figure(figsize=(12,6))
    plt.title('Histogram')
    plt.subplot([1,2,1])
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0,256])
    plt.plot(original_hist)
    plt.grid(True)

    plt.title('Equlized image and histogram')
    plt.subplot([1,2,2])

    plt.imshow(equlized_hist,cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    enhance_image_path='enhance_image.jpg'
    cv2.imwrite(enhance_image_path,equlized_image)
    

