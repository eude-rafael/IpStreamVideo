import cv2
from src.fileNewName import FileNewName

class IpVideoCapture:
    def start(self, url):
        capture = cv2.VideoCapture(url)

        # Obtém as dimensões do vídeo de entrada
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = 30  # Define a taxa de quadros por segundo do vídeo de saída

        newName = FileNewName()
        name = newName.create_name()

        # Define o objeto VideoWriter para salvar o vídeo
        output = cv2.VideoWriter( './videos/'+name+'.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while True:
            _, frame = capture.read()
            cv2.imshow('livestream', frame)

            # Grava o quadro atual no vídeo de saída
            output.write(frame)

            if cv2.waitKey(1) == ord("q"):
                break

        capture.release()
        output.release()  # Fecha o objeto VideoWriter

cv2.destroyAllWindows()





