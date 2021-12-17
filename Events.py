import cv2
import numpy as np

def dibujando (event,x,y,flag,param):
    #aqui se imprimen la informacion sobre los eventos que se estan realizando
    print('-----------------')
    print('event', event)
    print('x=',x)
    print('y=',y)
    print('flags',flag)
    
    #ejemplos de los difrentes eventos del mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen,(x,y),20,(255,255,255),2)
        cv2.putText(imagen, "presionaste el boton izquierdo",(x,y),2,1,(255,255,0),2)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(imagen,(x,y),20,(0,0,255),2)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(imagen,(x,y),10,(255,0,0),-1)

    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(imagen,(x,y),10,(0,255,0),-1)

    if event == cv2.EVENT_LBUTTONUP:
        cv2.putText(imagen, "Has dejado de presionar el boton izquierdo", (x,y),2,0.4,(255,255,0),1,cv2.LINE_AA)

    if event == cv2.EVENT_RBUTTONUP:
        cv2.putText(imagen, "Has dejado de presionar el boton derecho",(x,y),2,0.4,(0,255,255),1,cv2.LINE_AA)

imagen =np.zeros((480,640,3),np.uint8)
cv2.namedWindow('VENTANA DE PRUEBA')
cv2.setMouseCallback('VENTANA DE PRUEBA', dibujando)

while True:
    cv2.imshow('EVENTOS DEL MOUSE', imagen)

    k = cv2.waitKey(1) & 0xFF
    #al presionar sta tecla se limpia el contenido
    if k == ord('c'):
        imagen = np.zeros((480,640,3),np.uint8)
    elif k == 27:
        break
cv2.destroyAllWindows() 