import matplotlib.pyplot as plt

def subplt (rows, cols, img, label):
  plt_img = img[:rows*cols]
  plt.figure(figsize=(rows*2,cols*2))
  
  for i in range(len(plt_img)):
    plt.subplot(rows, cols, i+1)
    plt.imshow(plt_img[i], cmap = 'gray')
    plt.title(label[i])
    plt.axis('off')
  
  return
