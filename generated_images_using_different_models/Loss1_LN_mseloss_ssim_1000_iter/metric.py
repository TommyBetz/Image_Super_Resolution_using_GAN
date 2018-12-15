import matplotlib.pyplot as plt 
from skimage.measure import compare_ssim
from skimage.measure import compare_psnr

x = plt.imread('evaluate/valid_gen.png')
y = plt.imread('evaluate/valid_hr.png')

ssim = compare_ssim(x, y, multichannel = True)
psnr = compare_psnr(x, y)

print ("SSIM")
print (ssim)
print ("PSNR")
print (psnr)
