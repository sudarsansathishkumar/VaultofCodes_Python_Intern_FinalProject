from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect("listdb.db")
c = conn.cursor()

c.execute("create table if not exists tasks(task text, status text);")

conn.commit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 600)
        MainWindow.setMinimumSize(QtCore.QSize(775, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/check-list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow QWidget {\n"
"    border: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #27303b;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setStyleSheet("background-color:#637182; border-radius: 8")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setStyleSheet("font-size: 25px; font-weight: 500; color: white;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)


        # Input field

        self.input_box = QtWidgets.QLineEdit(self.frame_4)
        self.input_box.setMinimumSize(QtCore.QSize(0, 40))
        self.input_box.setStyleSheet("background-color: white; border-radius: 8px; font-size: 20px; padding: 10px")
        self.input_box.setObjectName("input_box")
        self.verticalLayout_2.addWidget(self.input_box)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("QFrame {\n"
"background-color:transparent;\n"
"}\n"
"QPushButton {\n"
"background-color:#5494e3; border-radius: 8; color: white; font-weight: bold; font-size:12px; padding: 10px 20px; margin: 0px 10px;height: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"color: #5494e3;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(-1, 12, -1, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)


        # Action Buttons

        self.add_task_btn = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.additem())
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_task_btn.setIcon(icon1)
        self.add_task_btn.setObjectName("add_task_btn")
        self.horizontalLayout_2.addWidget(self.add_task_btn)
        self.markascomplete_btn = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.markascomplete())
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/approved.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.markascomplete_btn.setIcon(icon2)
        self.markascomplete_btn.setIconSize(QtCore.QSize(24, 24))
        self.markascomplete_btn.setObjectName("markascomplete_btn")
        self.horizontalLayout_2.addWidget(self.markascomplete_btn)
        self.undocompletion_btn = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.undocomplete())
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undocompletion_btn.setIcon(icon3)
        self.undocompletion_btn.setIconSize(QtCore.QSize(20, 20))
        self.undocompletion_btn.setObjectName("undocompletion_btn")
        self.horizontalLayout_2.addWidget(self.undocompletion_btn)
        self.delete_btn = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.delete())
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon4)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_2.addWidget(self.delete_btn)
        spacerItem1 = QtWidgets.QSpacerItem(9, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setStyleSheet("QFrame {\n"
"background-color:transparent;\n"
"}\n"
"QPushButton {\n"
"background-color:#5494e3; border-radius: 8; color: white; font-weight: bold; font-size:12px; padding: 10px 20px; margin: 0px 10px\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"color: #5494e3;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.View_all_btn = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.viewall())
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons/grid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.View_all_btn.setIcon(icon5)
        self.View_all_btn.setObjectName("View_all_btn")
        self.horizontalLayout.addWidget(self.View_all_btn)
        self.View_not_completed_btn = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.viewnotcompleted())
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icons/yumminky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.View_not_completed_btn.setIcon(icon6)
        self.View_not_completed_btn.setObjectName("View_not_completed_btn")
        self.horizontalLayout.addWidget(self.View_not_completed_btn)
        self.View_completed_btn = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.viewcompleted())
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icons/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.View_completed_btn.setIcon(icon7)
        self.View_completed_btn.setObjectName("View_completed_btn")
        self.horizontalLayout.addWidget(self.View_completed_btn)
        spacerItem3 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color:transparent; border-radius: 8")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        
        
        # List view
        
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.listWidget.setStyleSheet("""QListWidget
                                      {
                                          background-color: #637182;
                                          font-size: 25px;
                                      }
                                      QListWidget::item {
                                          margin: 0px 15px;
                                      }""")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        spacerItem5 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.viewall()
        
    def additem(self):
        text = self.input_box.text()
        if text != "":
            addtext = QtWidgets.QListWidgetItem(text)
            addtext.setForeground(QtCore.Qt.white)
            self.listWidget.addItem(addtext)
            cmd = f"insert into tasks values('{text}', 'progress');"
            c.execute(cmd)
            conn.commit()
            self.input_box.setText("")
        
    def viewall(self):
        self.listWidget.clear()
        self.View_all_btn.setStyleSheet("background-color: blue; color: white;")
        self.View_not_completed_btn.setStyleSheet("")
        self.View_completed_btn.setStyleSheet("")
        c.execute("select * from tasks;")
        record = c.fetchall()
        for rec in record:
            newtext = QtWidgets.QListWidgetItem(rec[0])
            if rec[1] == "completed":
                newtext.setForeground(QtCore.Qt.green)
            else:
                newtext.setForeground(QtCore.Qt.white)
                
            self.listWidget.addItem(newtext)
    
    def viewnotcompleted(self):
        self.listWidget.clear()
        self.View_all_btn.setStyleSheet("")
        self.View_not_completed_btn.setStyleSheet("background-color: blue; color: white;")
        self.View_completed_btn.setStyleSheet("")
        c.execute("select * from tasks where status='progress';")
        record = c.fetchall()
        for rec in record:
            newtext = QtWidgets.QListWidgetItem(rec[0])
            newtext.setForeground(QtCore.Qt.white)                
            self.listWidget.addItem(newtext)
    
    def viewcompleted(self):
        self.listWidget.clear()
        self.View_all_btn.setStyleSheet("")
        self.View_not_completed_btn.setStyleSheet("")
        self.View_completed_btn.setStyleSheet("background-color: blue; color: white;")
        c.execute("select * from tasks where status='completed';")
        record = c.fetchall()
        for rec in record:
            newtext = QtWidgets.QListWidgetItem(rec[0])
            newtext.setForeground(QtCore.Qt.green)                
            self.listWidget.addItem(newtext)
        
    def markascomplete(self):
        ind = self.listWidget.currentRow()
        if ind >= 0:
            obj = self.listWidget.item(ind)
            text = obj.text()
            cmd = f"select * from tasks where task='{text}'"
            c.execute(cmd)
            record = c.fetchone()
            if record[1] == "progress":
                cmd = f"update tasks set status='completed' where task='{record[0]}'"
                c.execute(cmd)
                conn.commit()
                obj.setForeground(QtCore.Qt.green)
    
    def undocomplete(self):
        ind = self.listWidget.currentRow()
        if ind >= 0:
            obj = self.listWidget.item(ind)
            text = obj.text()
            cmd = f"select * from tasks where task='{text}'"
            c.execute(cmd)
            record = c.fetchone()
            if record[1] == "completed":
                cmd = f"update tasks set status='progress' where task='{record[0]}'"
                c.execute(cmd)
                conn.commit()
                obj.setForeground(QtCore.Qt.white)
    
    def delete(self):
        ind = self.listWidget.currentRow()
        if ind >= 0:
            obj = self.listWidget.item(ind)
            text = obj.text()
            cmd = f"delete from tasks where task='{text}';"
            c.execute(cmd)
            conn.commit()
            self.listWidget.takeItem(ind)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo List"))
        self.label.setText(_translate("MainWindow", " ToDo List Application"))
        self.input_box.setText(_translate("MainWindow", ""))
        self.add_task_btn.setText(_translate("MainWindow", "Add task"))
        self.markascomplete_btn.setText(_translate("MainWindow", "Mark as Complete"))
        self.undocompletion_btn.setText(_translate("MainWindow", "Undo Completion"))
        self.delete_btn.setText(_translate("MainWindow", "Delete task"))
        self.View_all_btn.setText(_translate("MainWindow", "All"))
        self.View_not_completed_btn.setText(_translate("MainWindow", "Not Completed"))
        self.View_completed_btn.setText(_translate("MainWindow", "Completed"))
        
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
