import cv2

image = cv2.imread("C:/Users/admin/Desktop/CV(Project)/python_image.png")

if image is not None:
    sucess = cv2.imwrite("output_python.png", image)
    if sucess:
        print("Image saved sucessfully as 'output_python.png")
    else:
        print("Failed to save an image")
else:
    print("Error: Could not load image")