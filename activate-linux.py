import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

w = QWidget()
w.setWindowFlags(
    Qt.FramelessWindowHint |
    Qt.WindowStaysOnTopHint |
    Qt.Tool |
    Qt.X11BypassWindowManagerHint |
    Qt.WindowTransparentForInput
)
w.setAttribute(Qt.WA_TranslucentBackground)
w.setAttribute(Qt.WA_ShowWithoutActivating)
w.setAttribute(Qt.WA_TransparentForMouseEvents)

layout = QVBoxLayout(w)
layout.setContentsMargins(0, 0, 0, 0)
layout.setSpacing(0)

l1 = QLabel("Activate Linux")
l1.setStyleSheet("color: rgba(255,255,255,180); font-size: 22px; font-family: 'DejaVu Sans';")
l1.setAlignment(Qt.AlignRight)
l1.setAttribute(Qt.WA_TransparentForMouseEvents)

l2 = QLabel("Go to Settings to activate Linux.")
l2.setStyleSheet("color: rgba(255,255,255,150); font-size: 13px; font-family: 'DejaVu Sans';")
l2.setAlignment(Qt.AlignRight)
l2.setAttribute(Qt.WA_TransparentForMouseEvents)

layout.addWidget(l1)
layout.addWidget(l2)

w.resize(320, 70)
w.move(1280 - 320 - 25, 720 - 70 - 65)
w.show()

sys.exit(app.exec_())
