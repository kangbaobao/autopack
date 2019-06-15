from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QFileDialog,QPushButton,QComboBox,QLineEdit
from LocalData import LocalData
import pickle
import os
class kMianWiget(QWidget):
    labelWidth = 120
    #本地存储数据文件
    pickelFile = 'data.pkl'
    def __init__(self,parnet=None):
        super().__init__()
        self.initData()
        self.readLocalData()
        self.createUI()
        self.setWindowTitle("iOS自动打包工具")
    # 初始化数据
    def initData(self):
        #打开xcworkspace路径
        self._xcWorkFile = ''
        #export_directory 输出的文件夹
        self._export_directory = ''
        # build Configuration
        self.buildConfig = ''
        self.lData = None
    @property
    def export_directory(self):
        return self._export_directory
    @export_directory.setter
    def export_directory(self,value):
        self.lData.exportDir = value
        self.writerData()
        self._export_directory = value
    @property
    def xcWorkFile(self):
        return self._xcWorkFile
    @xcWorkFile.setter
    def xcWorkFile(self,value):
        self.lData.xcworkFile = value
        self.writerData()
        self._xcWorkFile = value

    # 读取本地化数据
    def readLocalData(self):
        if os.path.exists(self.pickelFile) is False:
            return
        with open(self.pickelFile,'rb') as f:
            self.lData = pickle.load(f)
            print('readLocalData : ',self.lData)
        
    # 初始化UI布局 
    def createUI(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        #xcworkspace 路径
        firstHlayout = QHBoxLayout()
        mainLayout.addLayout(firstHlayout)
        xcworkspaceLab = QLabel("xcworkspace路径：")
        xcworkspaceLab.setMinimumWidth(self.labelWidth)
        firstHlayout.addWidget(xcworkspaceLab)
        # 输入框
        xcworkspaceInput = QLineEdit()
        xcworkspaceInput.setPlaceholderText("选择xcworkspace/xcodeproj文件打开")
        # 设置显示效果
        xcworkspaceInput.setEchoMode(QLineEdit.Normal)
        xcworkspaceInput.textChanged.connect(lambda text : self.textChange(text,1))
        firstHlayout.addWidget(xcworkspaceInput,1)
        
        xcworkspaceBtn = QPushButton("open")
        xcworkspaceBtn.clicked.connect(lambda x: self.xcworkspaceFilehandler(xcworkspaceInput))
        firstHlayout.addWidget(xcworkspaceBtn)

        # 输出的文件相关视图
        twoHlayout = QHBoxLayout()
        mainLayout.addLayout(twoHlayout)
        exportLab = QLabel("ipa包导出路径：")
        exportLab.setMinimumWidth(self.labelWidth)
        twoHlayout.addWidget(exportLab)
        # 输入框
        exportInput = QLineEdit()
        exportInput.setPlaceholderText("选择导出的路径")
        # 设置显示效果
        exportInput.setEchoMode(QLineEdit.Normal)
        exportInput.textChanged.connect(lambda text : self.textChange(text,2))
        twoHlayout.addWidget(exportInput,1)
        exportBtn = QPushButton("open")
        exportBtn.clicked.connect(lambda x: self.exporthandler(exportInput))
        twoHlayout.addWidget(exportBtn)

        # build Configuration 配置
        threeHlayout = QHBoxLayout()
        mainLayout.addLayout(threeHlayout)
        buildConfLab = QLabel("build Configuration：")
        buildConfLab.setMinimumWidth(self.labelWidth)

        threeHlayout.addWidget(buildConfLab)
        # 下来选择框
        buildConfSel = QComboBox()
        buildConfSel.addItems(["Release","Debug"])
        buildConfSel.currentIndex = 1
        buildConfSel.currentIndexChanged.connect(lambda index: self.buildConfSelectChange(index,buildConfSel))
        threeHlayout.addWidget(buildConfSel,1)
        #
        mainLayout.addStretch(1)
        # 设置本地保存的文本
        if self.lData is not None:
            xcworkspaceInput.setText(self.lData.xcworkFile)
            exportInput.setText(self.lData.exportDir)
        else:
            self.lData = LocalData();
    #wirte 本地数据
    def writerData(self):
        with open(self.pickelFile,'wb') as f:
            pickle.dump(self.lData,f)
    # 文本变化监听槽函数
    def textChange(self,text,index):
        print("text : ",text)
        print("index: ",index)
        if index == 1:
            #xcworkspace路径
            self.xcWorkFile = text
        elif index == 2 :
            self.export_directory = text
        
    # 选择工程
    def xcworkspaceFilehandler(self,input):
        print("input : ",input)
        fileName = QFileDialog.getOpenFileName(self,"打开xcworkspace","~/Desktop")
        self.xcWorkFile = fileName[0]
        input.setText(fileName[0])
        print("fileName: ",fileName)
       

    #选择export_directory 输出的文件夹事件
    def exporthandler(self,input):
        print("input : ",input)
        fileName = QFileDialog.getExistingDirectory(self,"选择导出路径","~/Desktop")
        self.export_directory = fileName
        input.setText(fileName)
        print("fileName: ",fileName)
    #下拉框选择选择事件
    def buildConfSelectChange(self,index,cb):
        print("cb text: ",cb.currentText())
        self.buildConfig = cb.currentText()
        '''
        for count in range(cb.count()):
    			print( 'item'+str(count) + '='+ cb.itemText(count) )
			print( "Current index",i,"selection changed ",cb.currentText() )
        '''