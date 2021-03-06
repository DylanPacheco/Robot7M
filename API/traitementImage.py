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
    #print (img.format,img.size, img.mode)
    
    largeur = img.size[0]
    hauteur = img.size[1]
    
    for i in range (0,largeur):
        for j in range (0,hauteur):
            tup = img.getpixel((i,j))
            #"""
            if tup[0] > 190 and tup[1] < 100 and tup[2] < 100:
                #couleur rouge
                img.putpixel((i,j),(255,0,0))
            elif tup[0] > 185 and tup[1] > 170 and tup[2] < 80:
                #couleur jaune
                img.putpixel((i,j),(255,255,0))
            elif tup[0] < 130 and tup[1] < 150 and tup[2] > 150:
                #couleur bleue
                #elif tup[0] < 80 and tup[1] < 110 and tup[2] > 150:
                img.putpixel((i,j),(0,0,255))
            elif tup[0] < 135 and tup[1] > 130 and tup[2] < 135:
                #couleur verte
                #elif tup[0] < 110 and tup[1] > 130 and tup[2] < 110:
                img.putpixel((i,j),(0,255,0))
            #"""
    
    
    print(img.size)

    img.show()

    #print(list(img.getdata()))
    
    #"""
    
    detect = [0,0,0,0]
    
    lfmin = 0
    hfmin = 0
    lfmax = 60
    hfmax = 40
    
    while lfmax <= largeur:
        for i in range (lfmin,lfmax):
            while hfmax <= hauteur:
                for j in range (hfmin,hfmax):
                    tup = img.getpixel((i,j))
                    if tup[0] == 255 and tup[1] == 0 and tup[2] == 0:
                        detect[0] = 1
                        print("Rouge trouvé")
                    elif tup[0] == 0 and tup[1] == 255 and tup[2] == 0:
                        detect[1] = 1
                        print("Vert trouvé")
                    elif tup[0] == 0 and tup[1] == 0 and tup[2] == 255:
                        detect[2] = 1
                        print("Bleu trouvé")
                    elif tup[0] == 255 and tup[1] == 255 and tup[2] == 0:
                        detect[3] = 1
                        print("Jaune trouvé")
                    if (detect[0] == 1 and detect[1] == 1) or (detect[2] == 1 and detect[3] == 1):
                        print("===========================================")
                        print("Balise trouvée aux coordonnées : ",i,j)
                        print("===========================================")
                hfmin += 40
                hfmax += 40
            detect = [0,0,0,0]
        lfmin += 60
        lfmax += 60
        hfmax = 40
        hfmin = 0
        
    #"""
    
    img.close()
