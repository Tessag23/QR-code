#using 'Open Source Computer Vision'
import cv2
import webbrowser

cap=cv2.VideoCapture(0)
detector=cv2.QRCodeDetector()
while True:
    _,img=cap.read()
    data,one, _=detector.detectAndDecode(img)
    if data:
        a=data
        cv2.destroyAllWindows()
        break
    cv2.imshow('qrcodescanner app',img)
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        break
b=webbrowser.open(str(a))
cap.release(a)
cap.release()
cv2.destroyAllWindows()