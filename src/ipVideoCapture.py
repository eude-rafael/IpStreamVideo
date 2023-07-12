import cv2
from src.fileNewName import FileNewName

class IpVideoCapture:
    def start(self, url):
        capture = cv2.VideoCapture(url)

        # Obtém as dimensões do vídeo de entrada
        # Gets the dimensions of the input video
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fps = 30    # Define a taxa de quadros por segundo do vídeo de saída
                    # Sets the frames per second rate of the output video

        # Cria novo nome a cada arquivo
        # Create new name for each file
        name = FileNewName().create_name()

        # Define o objeto VideoWriter para salvar o vídeo
        # Sets the video VideoWriter object to save the video 
        output = cv2.VideoWriter( './videos/'+name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while True:
            _, frame = capture.read()
            
            # Mostrando video 
            # showing video
            cv2.imshow('livestream', frame)

            # Grava o quadro atual no vídeo de saída
            # Writes the current frame to the output video
            output.write(frame)

            if cv2.waitKey(1) == ord("q"):
                break

        # Encerra captura dos framers
        # End capture of framers 
        capture.release()

        # Salva video
        # save video
        output.release()  


# Fecha todas as janelas
# Close all  windows
cv2.destroyAllWindows()





