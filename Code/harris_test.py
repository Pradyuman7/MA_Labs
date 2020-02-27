from Code import harris
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("/Users/pd/PycharmProjects/MA_Labs/Images/bookshelf.jpg", cv2.IMREAD_GRAYSCALE)
res = harris.compute_harris_response(image)

plt.imshow(res)
