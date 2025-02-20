import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

    def menu_bar(self):

        # menuBar 메서드를 통해 QMenuBar 클래스의 인스턴스 생성
        menubar = self.menuBar()

        # addMenu 메서드를 사용하여 Setting라는 이름을 가진 QMenu 클래스의 인스턴스를 생성
        setting_menu = menubar.addMenu("Setting")

        # addAction 메서드를 사용하여 Option Menu가 클릭되었을 때, Start라는 텍스트의 QAction 인스턴스를 생성
        # start_action = option_menu.addAction("Start")

    def tool_bar(self):

        # 툴바 생성
        self.toolbar = self.addToolBar("ToolBar")
        self.toolbar.setMovable(False)

        # 버튼 생성
        start_tool = QAction(QIcon("./img/start.png"), "&Start", self) # 시작 버튼
        stop_tool = QAction(QIcon("./img/stop.png"), "&Stop", self) # 정지 버튼

        # 단축키 설정
        start_tool.setShortcut("Ctrl+Q") # 시작
        stop_tool.setShortcut("Ctrl+W") # 정지

        # 툴팁 설정
        start_tool.setToolTip("Crawler Start") # 시작
        stop_tool.setToolTip("Crawler Stop") # 정지

        # 툴바에 버튼 추가
        self.toolbar.addAction(start_tool)
        self.toolbar.addAction(stop_tool)

    def frame(self):

        # 메인 위젯 생성
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 메인 레이아웃 생성
        main_layout = QVBoxLayout(main_widget)

        # 좌우 프레임 생성
        left_frame = QFrame()
        left_frame.setFrameShape(QFrame.Panel | QFrame.Sunken)
        right_frame = QFrame()
        right_frame.setFrameShape(QFrame.Panel | QFrame.Sunken)

        # 좌우 레이아웃 생성
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        button_1 = QPushButton("button_1")
        button_2 = QPushButton("button_2")

        left_layout.addWidget(button_1)
        right_layout.addWidget(button_2)

        left_frame.setLayout(left_layout)
        right_frame.setLayout(right_layout)

        spliter = QSplitter(Qt.Horizontal)
        spliter.addWidget(left_frame)
        spliter.addWidget(right_frame)

        main_layout.addWidget(spliter)

    def initUI(self):
        """
        Main Window 초기 화면 설정
        """
        # 타이틀
        self.setWindowTitle("크롤러 GUI")

        # 창 크기
        self.resize(1600, 900)

        # 화면 중앙 배치
        self.center()

        # 메뉴바 생성
        self.menu_bar()

        # 툴바 생성
        self.tool_bar()

        # 화면 프레임 분할
        self.frame()


if __name__ == "__main__":

    # 프로그램 실행 클래스
    app = QApplication(sys.argv)

    # MainWindow 클래스 인스턴스 생성
    main = MainWindow()

    # Main Window UI를 보여주는 메서드 실행
    main.show()

    # 프로그램 실행
    app.exec_()