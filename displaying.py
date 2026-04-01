import cv2

image = cv2.imread("C:/Users/admin/Desktop/CV(Project)/python_image.png")

if image is not None:
    cv2.imshow("Image showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not the image")