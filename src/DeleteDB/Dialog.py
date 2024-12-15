from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class Dialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.resize(420, self.height())
        
        self.setWindowTitle('Войдите под именем суперпользователя')
        
        login_lbl = QLabel('Логин', parent=self)
        self.__login_edt = QLineEdit(parent=self)
        
        password_lbl = QLabel('Пароль', parent=self)
        self.__password_edt = QLineEdit(parent=self)
        self.__password_edt.setEchoMode(QLineEdit.Password)
        
        ok_btn = QPushButton('ОК', parent=self)
        cancel_btn = QPushButton('Отмена', parent=self)
        
        lay = QVBoxLayout(self)
        
        lay_login = QVBoxLayout()
        lay_login.setSpacing(0)
        lay_login.addWidget(login_lbl)
        lay_login.addWidget(self.__login_edt)
        lay.addLayout(lay_login)
        
        lay_password = QVBoxLayout()
        lay_password.setSpacing(0)
        lay_password.addWidget(password_lbl)
        lay_password.addWidget(self.__password_edt)
        lay.addLayout(lay_password)
        
        layH = QHBoxLayout()
        layH.addStretch()
        layH.addWidget(ok_btn)
        layH.addWidget(cancel_btn)
        lay.addLayout(layH)
        
        cancel_btn.clicked.connect(self.reject)
        ok_btn.clicked.connect(self.finish)
    
    def finish(self):
        if self.login is None or self.password is None:
            return 
        self.accept()
    
    @property
    def login(self):
        result = self.__login_edt.text().strip()
        return result if result else None
    
    @property
    def password(self):
        result = self.__password_edt.text().strip()
        return result if result else None
    
    def get(self, data):
        data.login = self.login
        data.password = self.password
    
    def put(self, data):
        self.login = data.login
        self.password = data.password
