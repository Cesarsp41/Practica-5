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
_,binaInv = cv2.threshold(imagen,10,255,cv2.THRESH_BINARY_INV)
_,binaInv2 = cv2.threshold(gris,10,255,cv2.THRESH_BINARY_INV)

cv2.imshow("Binario Inverso",binaInv)
cv2.moveWindow("Binario Inverso",0,300)
cv2.imshow("Binario inverso blanco y negro",binaInv2)
cv2.moveWindow("Binario inverso blanco y negro",1200,300)

opc = cv2.waitKey(0)
cv2.destroyAllWindows()

#Trunc

_,trunc = cv2.threshold(imagen,10,255,cv2.THRESH_TRUNC)
_,trunc2 = cv2.threshold(gris,10,255,cv2.THRESH_TRUNC)

cv2.imshow("Trunc",trunc)
cv2.moveWindow("Trunc",0,300)
cv2.imshow("Trunc blanco y negro",trunc2)
cv2.moveWindow("Trunc blanco y negro",1200,300)

opc = cv2.waitKey(0)
cv2.destroyAllWindows()
