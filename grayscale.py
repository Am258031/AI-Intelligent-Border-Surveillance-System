import cv2

image = cv2.imread("C:/Users/admin/Desktop/CV(Project)/python_image.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Could not load the image")