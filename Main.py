import cv2 as cv
from matplotlib import pyplot as plt
from collections import defaultdict

scale = 35
origImg = cv.imread("l.jpg")
height, width = origImg.shape[:2]
dim = (int(width * scale / 100), int(height * scale / 100))


image = cv.cvtColor(origImg, cv.COLOR_BGR2LAB)

d = defaultdict(int)
for i in range(height):
    for j in range(width):
        d[image[i, j][0]] += 1

x = []
y = []
for k, v in d.items():
    x.append(k)
    y.append(v)

xMin = min(x)
xMax = max(x)
xLin = []
for pix in x:
    pixLin = (pix - xMin) * 255 / (xMax - xMin)
    xLin.append(pixLin)

plt.subplot(211)
plt.bar(x=x, height=y, width=1, color="black")
plt.xlim(right=255)
plt.subplot(212)
plt.bar(x=xLin, height=y, width=1, color="black")

for i in range(height):
    for j in range(width):
        pix = image[i, j][0]
        image[i, j][0] = (pix - xMin) * 255 / (xMax - xMin)

cv.imshow("Before", cv.resize(origImg, dim, interpolation=cv.INTER_AREA))
newImage = cv.cvtColor(image, cv.COLOR_LAB2BGR)
cv.imshow("After", cv.resize(newImage, dim, interpolation=cv.INTER_AREA))
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()