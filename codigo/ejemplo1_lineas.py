print("valeria yaretzi NC = 1341")
import cv2
import numpy as np
import os

# ==========================================
# EJEMPLO 1 - DETECCIÓN DE LÍNEAS
# Imagen: alcon.jpg
# ==========================================

# Ruta de la imagen
ruta_imagen = os.path.join("imagenes", "alcon.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

# Verificar imagen
if imagen is None:
    print("ERROR: No se pudo cargar alcon.jpg")
    print("Verifica que alcon.jpg esté dentro de la carpeta imagenes.")
    exit()

print("Imagen cargada correctamente.")

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes
bordes = cv2.Canny(gris, 50, 150)

# Detectar líneas
lineas = cv2.HoughLinesP(
    bordes,
    1,
    np.pi / 180,
    threshold=50,
    minLineLength=50,
    maxLineGap=10
)

# Crear copia de la imagen
resultado = imagen.copy()

# Dibujar líneas
if lineas is not None:

    print("Líneas detectadas:", len(lineas))

    for linea in lineas:
        x1, y1, x2, y2 = linea

        cv2.line(
            resultado,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

else:
    print("No se detectaron líneas.")

# Mostrar imágenes
cv2.imshow("Imagen original - alcon", imagen)
cv2.imshow("Bordes", bordes)
cv2.imshow("Deteccion de lineas", resultado)

print("Presiona una tecla para cerrar.")

cv2.waitKey(0)
cv2.destroyAllWindows()
print("valeria yaretzi NC = 1341")