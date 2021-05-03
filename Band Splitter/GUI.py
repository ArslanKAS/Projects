
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


extensions = ('*.jpg', '*.png', '*.tif')
# user_input = raw_input("Enter the path of your file: ")
user_input = path + '\*.jpg'

image_list = []
# for filename in glob.glob('D:\MyResearch\Band-splitter\*.jpg'):
for filename in glob.glob(user_input):
    im = Image.open(filename)
    image_list.append(im)

# glob.

createFolder('./R/')
createFolder('./G/')
createFolder('./B/')

outpath1 = './R/'
outpath2 = './G/'
outpath3 = './B/'

# src_fname, ext = os.path.splitext(filename)
# save_fnameR = os.path.join(outpath1, os.path.basename(src_fname)+'.jpg')
# save_fnameG = os.path.join(outpath2, os.path.basename(src_fname)+'.jpg')
# save_fnameB = os.path.join(outpath3, os.path.basename(src_fname)+'.jpg')
d = 0
for imgs in image_list:
    split = Image.Image.split(imgs)
    band_R = split[0]
    band_G = split[1]
    band_B = split[2]
    cv2.imwrite(os.path.join(outpath1, str(d) + 'R.jpg'), np.array(band_R))
    cv2.imwrite(os.path.join(outpath2, str(d) + 'G.jpg'), np.array(band_G))
    cv2.imwrite(os.path.join(outpath3, str(d) + 'B.jpg'), np.array(band_B))
    d = d + 1