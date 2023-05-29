import cv2

camera_id = 0
delay = 1
window_name = 'scan multiple QR codes'

qr_code_detector = cv2.QRCodeDetector()
capture_video = cv2.VideoCapture(camera_id)

while True:
    ret, frame = capture_video.read()

    if ret:
        ret_qr, decoded_info, points, _ = qr_code_detector.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    print(s)
                    # print([p.astype(int)])
                    # print(p)
                    #if detected green
                    color = (0, 255, 0)
                    #color based on status
                    if "HR38Z1309" in s:
                        color = (0, 0, 255)

                else:
                    color = (255, 0,0 )
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
                for s, p in zip(decoded_info, points):
                    text_color=(0,255,0)
                    if "HR38Z1309" in s:
                        # color based on status
                        text_color=(0, 0, 255)
                        s="CANCELLED "+s.split("--")[0]
                    img = cv2.putText(frame, s.split("--")[0], p[0].astype(int)-10,
                                          cv2.FONT_ITALIC, 0.5, text_color, 1, cv2.LINE_AA)

        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)
