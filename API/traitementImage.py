from PIL import Image
import glob, os, sys

#size = 128, 128


for infile in glob.glob("*.jpg"):
    try:
      img = Image.open(infile)
    except IOError:
      print ('Erreur sur ouverture du fichier')
      sys.exit(1)
    # affichage des caractéristiques de l'image
    # print (img.format,img.size, img.mode)
    img.show()
    #print(list(img.getdata()))
    img.close()
