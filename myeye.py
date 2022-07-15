from cProfile import label
from cgi import print_arguments
import sys
from time import sleep, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from importlib_metadata import Sectioned
from itsdangerous import TimestampSigner
from matplotlib.pyplot import flag

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myeye.ui")[0]

#프로그램 시작 시간
stTime = QTime.currentTime()

timerVar = QTimer()
stopFlag = 0 # stop btn toggle var 

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Ui()
        self.timerVar = QTimer() #timer 함수 -> 프로그레스 바
        self.progressBar.setMaximum(3600) # set maximum
        self.timerVar.setInterval(1000)
        self.timerVar.timeout.connect(self.progressBarTimer)
        self.timerVar.start()
        self.stopBtn.clicked.connect(self.stopT)
        self.exitBtn.clicked.connect(QCoreApplication.instance().quit)
        self.position()

    def progressBarTimer(self) :
        self.time = self.progressBar.value()
        self.time += 1
        self.progressBar.setValue(self.time)

        #ProgressBar의 값이 최댓값 이상이 되면 Timer를 중단시켜 ProgressBar의 값이 더이상 증가하지 않게 합니다.
        if self.time >= self.progressBar.maximum() :
            self.timerVar.stop()
            self.saveMyEyes()

    def saveMyEyes(self):
        box = QMessageBox()

        #화면 중앙 찾기
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        
        #이미지 설정
        box.setWindowIcon(QtGui.QIcon('img/pepe.jpg'))
        box.setIconPixmap(QtGui.QPixmap('img/doc.jpg'))
        box.setWindowTitle("Warning!!")
        box.setInformativeText("1시간이 지났습니다!!!" + "일어나서 눈 좀 쉬고\n 목 근육을 풀어주세요! ")
        box.exec()  #박스 소환
        box.move(qr.topLeft())   # 박스 중앙으로 이동

        # 진행도 초기화
        self.progressBar.setValue(0)
        self.time = 0
        self.timerVar.start()

        
    
    def stopT(self):
        global stopFlag
        if stopFlag == 0 :
            self.timerVar.stop()
            stopFlag=1
        else:
            self.timerVar.start()
            stopFlag=0

    def Ui(self):
        self.setWindowOpacity(0.7)
        self.progressBar.setMinimumWidth(30)
        self.stopBtn.setMaximumWidth(30)
        self.exitBtn.setMaximumWidth(30)
        self.stopBtn.setStyleSheet(
            "color: rgb(58, 134, 255);"
            "background-color: white;"
            "border: 2px solid rgb(58, 134, 255);"
        )
        self.exitBtn.setStyleSheet(
            "color: rgb(255, 0, 99);"
            "background-color: white;"
            "border: 2px solid rgb(255, 0, 99);"
        )


    def position(self):
        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.setGeometry(0,0,30,sizeObject.height()-50)
        self.setWindowTitle("sdf")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()