# 라이브러리 불러오기
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
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
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
        self.toolbar = self.addToolBar("ToolBar")
        self.toolbar.setMovable(False) # 이동 금지

        # 시작 버튼
        start_tool = QAction(QIcon("./img/start.png"), "&Start", self)
        start_tool.setShortcut("Ctrl+Q")
        start_tool.setToolTip("Crawler Start")
        self.toolbar.addAction(start_tool)

        # 종료 버튼
        stop_tool = QAction(QIcon("./img/stop.png"), "&Stop", self)
        stop_tool.setShortcut("Ctrl+W")
        stop_tool.setToolTip("Crawler Stop")
        self.toolbar.addAction(stop_tool)

        # 저장 버튼
        save_tool = QAction(QIcon("./img/save.png"), "&Save", self)
        save_tool.setShortcut("Ctrl+S")
        save_tool.setToolTip("File Save")
        self.toolbar.addAction(save_tool)

        # 리셋 버튼
        reset_tool = QAction(QIcon("./img/reset.png"), "&Reset", self)
        reset_tool.setShortcut("Ctrl+R")
        reset_tool.setToolTip("Parameter Reset")
        self.toolbar.addAction(reset_tool)

    def left_panel(self):
        l_panel = QWidget()
        l_panel.setFixedWidth(300)  # 크기 고정
        left_layout = QVBoxLayout(l_panel)

        return l_panel

    def frame(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # QSplitter를 사용해 좌/우 패널 분할
        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(0)

        # 왼쪽 패널 (고정 크기)
        l_panel = self.left_panel()

        # 패널 추가
        splitter.addWidget(l_panel)

        # 메인 레이아웃에 추가
        main_layout.addWidget(splitter)

    def initUI(self):
        self.setWindowTitle("크롤러 GUI") # GUI 타이틀
        self.resize(1600, 900) # GUI 크기
        self.center() # 화면 가운데 정렬
        self.menu_bar() # 메뉴바 생성
        self.tool_bar() # 툴바 생성
        self.frame() # 프레임 2분할

if __name__ == "__main__":

    # 프로그램 실행
    app = QApplication(sys.argv)

    # MainWindow 클래스 인스턴스 생성
    main = MainWindow()

    # Main Window UI를 보여주는 메서드 실행
    main.show()

    # 프로그램 실행
    app.exec_()