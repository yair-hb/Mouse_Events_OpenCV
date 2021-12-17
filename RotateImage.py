import cv2

def rotar (event,x,y,flag,param):
    global angulo, imagen_rotar

    if event == cv2.EVENT_LBUTTONDOWN:
        angulo = angulo + 15
        m = cv2.getRotationMatrix2D((ancho/2,alto/2),angulo,1)
        imagen_rotar = cv2.warpAffine(imagen,m,(ancho,alto))

    if event == cv2.EVENT_RBUTTONDOWN:
        angulo =angulo -15
        m = cv2.getRotationMatrix2D((ancho/2,alto/2),angulo,1)
        imagen_rotar = cv2.warpAffine(imagen,m,(ancho,alto))

imagen = cv2.imread('ave.jpg')
imagen_rotar = imagen.copy()
ancho = imagen.shape[1]
alto = imagen.shape[0]
angulo = 0
cv2.namedWindow('imagen a rotar')
cv2.setMouseCallback('imagen a rotar', rotar)

while True:
    cv2.imshow('IMAGEN DE PRUEBA',imagen)
    cv2.imshow('imagen a rotar', imagen_rotar)
    print('angulo=', angulo)
    if cv2.waitKey(1) & 0xFF ==27:
        break
cv2.destroyAllWindows()
