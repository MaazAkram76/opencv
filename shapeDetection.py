import cv2 as cv

img = cv.imread("shapes.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imgGray, 200, 255, cv.THRESH_BINARY_INV) # Use THRESH_BINARY_INV to invert the threshold
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
thresh_color = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)
cv.drawContours(thresh_color, contours, -1, (0, 255, 0), 4)

i = 0

for contour in contours:
    if i==0:     # here we are ignoring first counter because  !!!!!!!!!
                # findcontour function detects whole image as shape!!!!!!!!!!
        i=1
        continue
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    if len(approx)==3:
        print("Triangle, ")
    if len(approx)==4:
        print("Rectangle, ")
    if len(approx)>5:
        print("Dont know exactly")

cv.imshow("Contours on Shapes", thresh_color)
cv.waitKey(0)
cv.destroyAllWindows()
