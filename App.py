import cv2



class IpVideoCapture:
    def start(self, url):
        capture = cv2.VideoCapture(url)

        # Obtém as dimensões do vídeo de entrada
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = 30  # Define a taxa de quadros por segundo do vídeo de saída

        # Define o objeto VideoWriter para salvar o vídeo
        output = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while True:
            _, frame = capture.read()
            cv2.imshow('livestream', frame)

            # Grava o quadro atual no vídeo de saída
            output.write(frame)

            if cv2.waitKey(1) == ord("q"):
                break

        capture.release()
        output.release()  # Fecha o objeto VideoWriter



videoCapture = IpVideoCapture()
videoCapture.start("http://192.168.3.14:4747/video")
