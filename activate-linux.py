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

WIN_W, WIN_H = 320, 70
MARGIN_R, MARGIN_B = 25, 65
w.resize(WIN_W, WIN_H)

def reposition():
    screen = app.primaryScreen()
    if screen is None:
        return
    g = screen.geometry()
    w.move(g.width() - WIN_W - MARGIN_R, g.height() - WIN_H - MARGIN_B)

reposition()
w.show()

# ikut resolusi layar secara otomatis tiap berubah
def on_screen_changed(screen):
    try:
        screen.geometryChanged.connect(lambda _g: reposition())
    except Exception:
        pass
    reposition()

scr = app.primaryScreen()
if scr is not None:
    scr.geometryChanged.connect(lambda _g: reposition())
app.primaryScreenChanged.connect(on_screen_changed)

sys.exit(app.exec_())
