from skimage import data, segmentation, color, exposure
from skimage import graph
from skimage.io import imread
from skimage import transform
from matplotlib import pyplot as plt


img = data.coffee()
# img = imread('court_photos/perfect_center_view.jpg')
img = imread('court_photos/center_view_1.jpg')
# img = exposure.rescale_intensity(img)
img = transform.resize(img, (1000, 1000, 3))
plt.imshow(img)
plt.show()
# exit(0)

# 


labels1 = segmentation.slic(img, compactness=5, n_segments=1000,
                            start_label=1)
out1 = color.label2rgb(labels1, img, kind='avg', bg_label=0)
plt.imshow(out1)
plt.show()
g = graph.rag_mean_color(img, labels1, mode='similarity')
labels2 = graph.cut_normalized(labels1, g)
out2 = color.label2rgb(labels2, img, kind='avg', bg_label=0)

fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(6, 8))

ax[0].imshow(out1)
ax[1].imshow(out2)

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()