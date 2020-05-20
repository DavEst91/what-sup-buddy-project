import cv2
import numpy as np

#loading model
net = cv2.dnn.readNetFromCaffe("src/face_detection/opencv/deploy.prototxt", "src/face_detection/opencv/res10_300x300_ssd_iter_140000_fp16.caffemodel")

def face_detection(route_to_image):
    image = cv2.imread(route_to_image)
    image_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (W, H) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    # pass the blob through the network and obtain the detections and
    # predictions
    detections = net.forward()[0,0,0]
    confidence=detections[2]
    if confidence > 0.7:
        x0, y0, x1, y1 = detections[3:7]*np.asarray([H,W,H,W]).astype(int)
        x0, y0, x1, y1=int(x0),int(y0),int(x1),int(y1)
        roi = image_gray[y0:y1, x0:x1]
        roi = cv2.resize(roi, (48, 48))
        roi=(roi/255).reshape((1,48,48,1))
        return roi
    else:
        return False