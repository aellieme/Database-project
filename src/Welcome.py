from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap


TEXT = '''
Для вашего удобства в интерфейсе нашего приложения 
представлены два основных раздела меню:

1. Справка — здесь можно найти информацию о нашем приложении 
и используемой библиотеке, которая лежит в основе его работы.

2. Режимы — в этом разделе мы разместили таблицы с данными
о рейсах, билетах, аэропортах, самолетах и авиакомпаниях. 
При переключении режимов появляется возможность добавлять,
редактировать, удалять данные, а также очищать таблицу полностью. 
'''


class Welcome(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        lbl1 = QLabel('ДОБРО ПОЖАЛОВАТЬ!')
        lbl1.setFont(self.font1())
        lbl1.setAlignment(Qt.AlignCenter)
        
        lbl2 = QLabel(TEXT)
        lbl2.setFont(self.font2())
        lbl2.setAlignment(Qt.AlignCenter)
        
        lbl3 = QLabel('СЧАСТЛИВОГО ПУТИ!\n')
        lbl3.setFont(self.font3())
        lbl3.setAlignment(Qt.AlignCenter)
        
        im_lbl = QLabel()
        im = QPixmap('icon-airplane.png').scaled(100, 100)
        im_lbl.setPixmap(im)
        im_lbl.setAlignment(Qt.AlignCenter)
        
        lay = QVBoxLayout()
        lay.addWidget(lbl1)
        lay.addWidget(lbl2)
        lay.addWidget(lbl3)
        lay.addWidget(im_lbl)
        lay.setAlignment(Qt.AlignCenter)
        
        self.setLayout(lay)
    
    def font1(self):
        f1 = QFont()
        f1.setPointSize(36)
        f1.setBold(True)
        return f1
    
    def font2(self):
        f2 = QFont()
        f2.setPointSize(24)
        return f2
    
    def font3(self):
        f3 = QFont()
        f3.setPointSize(24)
        f3.setBold(True)
        return f3
