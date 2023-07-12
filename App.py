from src.ipVideoCapture import IpVideoCapture

# Ip da camera que transmite o dados
# IP of the canera that transmits the data
IpVideoCapture().start("http://192.168.3.14:4747/video")
