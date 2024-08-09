import cv2
import sys
from PySide6 import QtCore, QtGui, QtWidgets

class Test(QtWidgets.QMainWindow):

    def __init__(self):
        super(Test, self).__init__()
        self.resize(960, 700)
        self.title_wig = QtWidgets.QLabel(self)
        self.title_wig.setText("<h1> Title <\h1>")
        self.title_wig.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vid_label = QtWidgets.QLabel(self)
        self.vid_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.vid_label)


        """
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.title_wig)
        vbox.addWidget(self.vid_label)

        # self.setCentralWidget(vbox)
        self.setLayout(vbox)
        #return
        """
        self.setWindowTitle("WINDOW TITLE 123")
        self.camera = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)
            
        
    def update_frame(self):
        success, frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.vid_label.setPixmap(pixmap)
        #while True:
        #    pass
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Test()
    main_window.show()
    print("opened")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


"""
cap = cv2.VideoCapture(0)

cv2.namedWindow("test window", cv2.WINDOW_NORMAL)
cv2.moveWindow("test window", 200, 200)

while cap.isOpened():
    success, frame = cap.read()
    cv2.imshow("test window",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""