import cv2
import mediapipe as mp
import screeninfo

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()

desenho = mp.solutions.drawing_utils

contador = 0

while True:

    verificador, frame = webcam.read()
    if not verificador:
        break

    listas_rostos = reconhecedor_rostos.process(frame)

    if listas_rostos.detections:
        if contador >= 4:
            contador = 0
            cv2.destroyWindow("imagebackground")
        print('rosto encontrado!')
        for rosto in listas_rostos.detections:
            desenho.draw_detection(frame, rosto)
    else:
        contador += 1

    if contador == 4:

        screen = screeninfo.get_monitors()[0]
        width, height = screen.width, screen.height
        print('rosto não encontrado')
        imagem = cv2.imread("background.jpg")
        cv2.namedWindow("imagebackground", cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow("imagebackground", screen.x - 1, screen.y - 1)
        cv2.setWindowProperty("imagebackground", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("imagebackground", imagem)

    #cv2.imshow("detection", frame)

    key=cv2.waitKey(1000)
    if key == 27:
        break

webcam.release()
