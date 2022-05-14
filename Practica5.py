import cv2
import numpy as np

imagen = cv2.imread("Bandera.jpg")

#Blanco y negro
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) 

cv2.imshow("Original",imagen)
cv2.moveWindow("Original",0,300)
cv2.imshow("Blanco y negro",gris)
cv2.moveWindow("Blanco y negro",1200,300)

opc = cv2.waitKey(0)
cv2.destroyAllWindows()

#Binario
_,bina = cv2.threshold(imagen,10,255,cv2.THRESH_BINARY)
_,bina2 = cv2.threshold(gris,10,255,cv2.THRESH_BINARY)

cv2.imshow("Binario",bina)
cv2.moveWindow("Binario",0,300)
cv2.imshow("Binario blanco y negro",bina2)
cv2.moveWindow("Binario blanco y negro",1200,300)

opc = cv2.waitKey(0)
cv2.destroyAllWindows()

#Binario Inverso
