ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>15</x>
      <y>61</y>
      <width>771</width>
      <height>481</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addButton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="editButton">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>10</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Редактировать</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
add_edit_ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>405</width>
    <height>354</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="formLayoutWidget">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>20</y>
      <width>331</width>
      <height>171</height>
     </rect>
    </property>
    <layout class="QFormLayout" name="formLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Название сорта</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Степень обжарки</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Молотый/ в зернах</string>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Описание вкуса</string>
       </property>
      </widget>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_5">
       <property name="text">
        <string>Цена, руб</string>
       </property>
      </widget>
     </item>
     <item row="5" column="0">
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>Объем упаковки, мл</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QLineEdit" name="variety_name"/>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="degree_of_roasting"/>
     </item>
     <item row="3" column="1">
      <widget class="QLineEdit" name="taste_descr"/>
     </item>
     <item row="4" column="1">
      <widget class="QLineEdit" name="price"/>
     </item>
     <item row="5" column="1">
      <widget class="QLineEdit" name="volume_ml"/>
     </item>
     <item row="2" column="1">
      <widget class="QComboBox" name="comboBox">
       <item>
        <property name="text">
         <string>Молотый</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>В зернах</string>
        </property>
       </item>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>210</y>
      <width>311</width>
      <height>61</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="closeButton">
       <property name="text">
        <string>Отмена</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="Button">
       <property name="text">
        <string>Сохранить</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>405</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''