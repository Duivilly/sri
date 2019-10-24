import cv2
import numpy as np
import matplotlib.pyplot as plt

def extractImageBIC_part(path):
	#load image
	#0       = gray
	#without = rgb
	img= cv2.imread(path, 0)

	#edge histogram (texture)
	#img= cv2.Canny(img,100,200)

	#set the size in the view of image into 40%
	img= cv2.resize(img, (400, 400))

	#load histogram opencv
	#plt.hist(img.ravel(),256,[0,256])

	#load my histograms bic (border/interior)
	histogramBorder1= []
	for i in range(256):
		histogramBorder1.append(0)

	histogramInside1= []
	for i in range(256):
		histogramInside1.append(0)

	#load my histograms bic 2
	histogramBorder2= []
	for i in range(256):
		histogramBorder2.append(0)

	histogramInside2= []
	for i in range(256):
		histogramInside2.append(0)

	#load my histograms bic 3
	histogramBorder3= []
	for i in range(256):
		histogramBorder3.append(0)

	histogramInside3= []
	for i in range(256):
		histogramInside3.append(0)

	#load my histograms bic 4
	histogramBorder4= []
	for i in range(256):
		histogramBorder4.append(0)

	histogramInside4= []
	for i in range(256):
		histogramInside4.append(0)

	#load my histograms bic 5
	histogramBorder5= []
	for i in range(256):
		histogramBorder5.append(0)

	histogramInside5= []
	for i in range(256):
		histogramInside5.append(0)

	w= img.shape[1]
	h= img.shape[0]
	for i in range(h):
		for j in range(w):
			#escurece particionamento 1
			if(j >= 0 and j <= w/2):#col
				if(i >= 0 and i <= h/2):#lin
					#img[i][j]= 255 #branco
					#bic part1
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside1[pixel]= histogramInside1[pixel] + 1
						else:
							histogramBorder1[pixel]= histogramBorder1[pixel] + 1
			#escurece particionamento 2
			if(j >= w/2 and j <= w):#col
				if(i >= 0 and i <= h/2):#lin
					#img[i][j]= 0
					#bic part2
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside2[pixel]= histogramInside2[pixel] + 1
						else:
							histogramBorder2[pixel]= histogramBorder2[pixel] + 1
			#escurece particionamento 3
			if(j >= 0 and j <= w/2):#col
				if(i >= h/2 and i <= h):#lin
					#img[i][j]= 0
					#bic part3
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside3[pixel]= histogramInside3[pixel] + 1
						else:
							histogramBorder3[pixel]= histogramBorder3[pixel] + 1
			#escurece particionamento 4
			if(j >= w/2 and j <= w):#col
				if(i >= h/2 and i <= h):#lin
					#img[i][j]= 255
					#bic part4
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside4[pixel]= histogramInside4[pixel] + 1
						else:
							histogramBorder4[pixel]= histogramBorder4[pixel] + 1
			#escurece particionamento 5
			if(j >= w/4 and j <= (w/4)*3):#col
				if(i >= h/4 and i <= (h/4)*3):#lin
					#img[i][j]= 255
					#bic part5
					if(w > j+2 and h > i+2):
						pixel= int(img[i+1][j+1])
						#os quatro vizinhos mais proximos
						v1= int(img[i][j])
						v2= int(img[i][j+2])
						v3= int(img[i+2][j])
						v4= int(img[i+2][j+2])
						#os pixels sao da mesma cor entao estao no interior senao estao na borda
						if(pixel == v1 and pixel == v2 and pixel == v3 and pixel == v4):
							histogramInside5[pixel]= histogramInside5[pixel] + 1
						else:
							histogramBorder5[pixel]= histogramBorder5[pixel] + 1
	descriptor= []
	#add descriptor 1
	descriptor.append(histogramBorder1+histogramInside1)
	#add descriptor 2
	descriptor.append(histogramBorder2+histogramInside2)
	#add descriptor 3
	descriptor.append(histogramBorder3+histogramInside3)	
	#add descriptor 4
	descriptor.append(histogramBorder4+histogramInside4)
	#add descriptor 5
	descriptor.append(histogramBorder5+histogramInside5)
	return descriptor

image1= 'image_0018.jpg'
descriptor1= extractImageBIC_part(image1)
image2= 'image_0021.jpg'
descriptor2= extractImageBIC_part(image2)

def compareHistogramBIC_part(histogram1, histogram2, limiar):
    #bigger or equal 60% of similarity
    similarityMin= 0.6
    len_histogram1= len(histogram1[0])
    len_histogram2= len(histogram2[0])
    similarity= 0
    for n in range(len(histogram1)):
        equal= 0
        for i in range(len_histogram1):
            if abs(int(histogram1[n][i])-int(histogram2[n][i])) <= limiar:
            	equal= equal + 1
        similarity= (equal/len_histogram2)+similarity
    #5=parts
    similarityGet= similarity/5
    if similarityGet >= similarityMin:
        return [True, similarityGet]
    else:
        return [False, similarityGet]

r= compareHistogramBIC_part(descriptor1, descriptor2, 12)
print(r)
'''
img= cv2.imread(path, 0)
plt.subplot(121)
plt.imshow(img, cmap= 'gray')
plt.title('Image')
plt.xticks([])
plt.yticks([])
plt.show()
'''