import cv2 as cv

img = cv.imread('lena.jpg', 0)

print(img)

cv.imshow('currImage', img)

k = cv.waitKey(0)  # & 0xFF

if k == ord('q'):
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('lena_copy.png', img)
    cv.destroyAllWindows()