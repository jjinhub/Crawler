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

    def load_stylesheet(self):
        """QSS 스타일 파일을 로드하는 함수"""
        with open("./qss/style.qss", "r", encoding="utf-8") as f:
            stylesheet = f.read()
            self.setStyleSheet(stylesheet)

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

        # 검색어 입력 박스
        panel1 = QFrame()
        groupbox_1 = QGroupBox('검색어')
        form_layout = QFormLayout()
        groupbox_1.setLayout(form_layout)

        content_1 = QLineEdit(groupbox_1)
        content_1.setPlaceholderText("검색어를 입력하세요.")
        form_layout.addRow(content_1)
        left_layout.addWidget(groupbox_1)

        # 정렬 기준 박스
        panel2 = QFrame()
        groupbox_2 = QGroupBox('정렬 기준')

        # 라디오 버튼 생성
        radio1 = QRadioButton('정확도순')
        radio2 = QRadioButton('인기도순')
        radio3 = QRadioButton('연도순')
        radio4 = QRadioButton('제목순')
        radio5 = QRadioButton('저자순')
        radio6 = QRadioButton('발행기관순')
        radio1.setChecked(True)

        # 라디오 버튼을 세로로 배치하는 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(radio4)
        vbox.addWidget(radio5)
        vbox.addWidget(radio6)

        # 레이아웃을 그룹박스에 설정
        groupbox_2.setLayout(vbox)

        # 레이아웃에 그룹박스 추가
        left_layout.addWidget(groupbox_2)

        # 데이터 수집 개수 입력 박스
        panel3 = QFrame()
        groupbox_3 = QGroupBox('데이터 수집 개수')
        form_layout = QFormLayout()
        groupbox_3.setLayout(form_layout)

        content_3 = QLineEdit(groupbox_3)
        content_3.setPlaceholderText("데이터 수집 개수를 입력하세요.")
        form_layout.addRow(content_3)
        left_layout.addWidget(groupbox_3)

        # 빈 박스
        panel4 = QFrame()
        panel4_layout = QVBoxLayout(panel4)
        left_layout.addWidget(panel4)

        # 버튼 박스
        panel5 = QFrame()
        groupbox_5 = QGroupBox()  # 제목 추가

        # 진행 상황바 생성
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)  # 기본 범위 설정 (나중에 입력값으로 변경)
        progress_bar.setValue(0)  # 초기 값 0%
        progress_bar.setAlignment(Qt.AlignCenter)  # 텍스트 중앙 정렬
        progress_bar.setTextVisible(True)  # 진행률 텍스트 표시

        # 버튼 생성
        start_button = QPushButton("시작")
        stop_button = QPushButton("정지")
        save_button = QPushButton("저장")
        reset_button = QPushButton("초기화")

        # 가로 레이아웃 (시작, 정지 버튼 한 줄 배치)
        hbox = QHBoxLayout()
        hbox.addWidget(start_button)
        hbox.addWidget(stop_button)

        # 그룹박스 레이아웃 생성
        groupbox5_layout = QVBoxLayout(groupbox_5)
        groupbox5_layout.addWidget(progress_bar)  # 진행 상황바 추가 (윗줄)
        groupbox5_layout.addLayout(hbox)  # 시작, 정지 버튼 추가 (중간줄)
        groupbox5_layout.addWidget(save_button)  # 저장 버튼 추가 (아래줄)
        groupbox5_layout.addWidget(reset_button)

        # 그룹박스를 왼쪽 패널에 추가
        left_layout.addWidget(groupbox_5)

        # --- 진행상황 업데이트 함수 (3번째 입력값 기준) ---
        def start_crawling():
            total = content_3.text()
            if not total.isdigit():
                QMessageBox.warning(None, "입력 오류", "올바른 숫자를 입력하세요.")
                return

            total = int(total)
            progress_bar.setRange(0, total)  # 입력된 값으로 범위 설정
            progress_bar.setValue(0)  # 초기화

            for i in range(total + 1):
                progress_bar.setValue(i)  # 값 업데이트
                progress_bar.setFormat("({}/{}) {:.2f}%".format(i, content_3.text(), (i/int(content_3.text()))*100))
                progress_bar.setAlignment(Qt.AlignCenter)  # 텍스트 중앙 정렬
                QApplication.processEvents()  # UI 업데이트

        # 시작 버튼 클릭 시 진행상황 업데이트
        start_button.clicked.connect(start_crawling)

        # 파라미터 리셋
        def reset_fields(self):
            # 검색어 입력란 초기화
            content_1.clear()

            # 데이터 수집 개수 초기화
            content_3.clear()

            # 진행 상황바 초기화
            progress_bar.setValue(0)
            progress_bar.setFormat("(0/0) 0%")  # 기본 텍스트 설정

            # 라디오 버튼 초기화 (첫 번째 버튼 선택)
            radio1.setChecked(True)

        reset_button.clicked.connect(reset_fields)  # 초기화 함수 연결

        # 크기 비율 설정
        left_layout.setStretchFactor(panel1, 1)
        left_layout.setStretchFactor(panel2, 1)
        left_layout.setStretchFactor(panel3, 1)
        left_layout.setStretchFactor(panel4, 20)
        left_layout.setStretchFactor(panel5, 1)

        # 간격 설정 (예: 레이아웃 간 간격을 10픽셀로 설정)
        left_layout.setSpacing(20)

        return l_panel

    def right_panel(self):
        r_panel = QWidget()
        right_layout = QVBoxLayout(r_panel)

        # QGroupBox 생성
        groupbox = QGroupBox("데이터 수집 현황")

        # QGroupBox를 메인 레이아웃에 추가
        right_layout.addWidget(groupbox)

        return r_panel

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

        # 오른쪽 패널 (확장 가능)
        r_panel = self.right_panel()

        # 패널 추가
        splitter.addWidget(l_panel)
        splitter.addWidget(r_panel)

        # 메인 레이아웃에 추가
        main_layout.addWidget(splitter)

    def initUI(self):
        self.setWindowTitle("크롤러 GUI") # GUI 타이틀
        self.resize(1600, 900) # GUI 크기
        self.load_stylesheet()  # QSS 스타일 적용
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