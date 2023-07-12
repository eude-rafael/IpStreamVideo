from src.ipVideoCapture import IpVideoCapture



videoCapture = IpVideoCapture()
videoCapture.start("http://192.168.3.14:4747/video")
