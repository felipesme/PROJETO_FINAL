from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel)
from gui.menu import Ui_menu
#from gui.TelaSistema import Ui_Sistema

import sys


class Menu(QWidget, Ui_menu):
    def __init__(self):
        super(Menu, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Menu")

        # Ação do botão de Entrar
        # self.btn_entrar.clicked.connect(self.abrir_sistema)

    # def abrir_sistema(self):
    # consulta no banco para pegar a senha

    # if self.txt_senha.text() == "123":
    # self.w = Sistema()
    # self.w.show()
    # self.close()


# Executando a página inicial do sistema
# class Sistema(QMainWindow, Ui_Sistema):
# def __init__(self):
# super(Sistema, self).__init__()

# self.setupUi(self)
# self.setWindowTitle("Sistema")

# Definindo ações da barra de Menu
# self.Menu_Aluno.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Alunos))
# self.Menu_Professor.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Professores))
# self.Menu_Turmas.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Turmas))
# self.Menu_Disciplina.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Disciplina))
# self.Menu_Usuarios.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Usuarios))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Menu()
    w.show()
    app.exec()
