import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    """
    Main Window 클래스
    """
    def __init__(self):
        """
        QMainWindow를 상속받아 Main Window를 생성
        """
        super().__init__()
        self.initUI()

    def center(self):

        # 창의 위치 및 크기 정보 파악
        qr = self.frameGeometry()

        # 모니터 화면의 가운데 위치 파악
        cp = QDesktopWidget().availableGeometry().center()

        # 화면 가운데 맞춤
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def initUI(self):

        # 타이틀
        self.setWindowTitle("크롤러 GUI")

        # 창 크기
        self.resize(1600, 900)

        # 화면 중앙 배치
        self.center()



        

        # 창 크기
        # self. setGeometry()
    


if __name__ == "__main__":

    # 프로그램 실행 클래스
    app = QApplication(sys.argv)

    # MainWindow 클래스 인스턴스 생성
    main = MainWindow()

    # Main Window UI를 보여주는 메서드 실행
    main.show()

    # 프로그램 실행
    app.exec_()