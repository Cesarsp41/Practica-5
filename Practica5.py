import cv2
import numpy as np

imagen = cv2.imread("Bandera.jpg")
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) #Grises

cv2.imshow("Original",imagen)
cv2.moveWindow("Original",0,300)

cv2.imshow("Blanco y negro",gris)
cv2.moveWindow("Blanco y negro",1200,300)

opc = cv2.waitKey(0)

