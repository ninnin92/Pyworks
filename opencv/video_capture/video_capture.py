import cv2

capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
    raise("IO Error")

capture.set(3, 1280)  # set video width
capture.set(4, 1024)  # set video hight


def video_cap_start(capture):
    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    while True:

        ret, image = capture.read()

        if ret is False:
            continue

        cv2.imshow("Capture", image)

        if cv2.waitKey(33) >= 0:
            cv2.imwrite("image.png", image)
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_cap_start(capture)
