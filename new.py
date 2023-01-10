from skimage import color
import numpy as np
import cv2
import math
def SuperPixel(image):
    lab = color.rgb2lab(image)
    lol = []
    for x, a in enumerate(lab):
        for y, b in enumerate(a):
            temp = np.append([y, x], [b])
            lol.append(temp)
    lol = np.array(lol)
    return lol

def make_superPixel(h, w,img):
    return [img[h,w][0],img[h,w][1],img[h,w][2], h, w]

def initial_cluster_center(S,img,img_h,img_w,clusters):
    h = S // 2
    w = S // 2
    while h < img_h:
        while w < img_w:
            clusters.append(make_superPixel(h, w,img))
            w += S
        w = S // 2
        h += S
    return clusters

rgb = cv2.imread('lol.jpg')
img = cv2.resize(rgb, (400,400))

img = color.rgb2lab(img)
k = 100 
m = 20    # Constant for normalizing the color proximity, range of m = [1,40]
img_h = img.shape[0]
img_w = img.shape[1]

N = img_h * img_w 
S = int(math.sqrt(N /k))

clusters = []
tag = {}
# initialize the distance between pixels and cluster center as infinity
dis = np.full((img_h, img_w), np.inf)
#super_image = SuperPixel(img)
clusters = initial_cluster_center(S,img,img_h,img_w,clusters)
print(len(clusters))
for i in clusters:
    print(i)
