from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
#2.hafta
import json
#--


app = QApplication([])


#2.hafta
'''json'daki notlar'''
notes = {
    "Hoş Geldiniz!":{
        "metin":"Bu benim en sevdiğim not",
        "etiketler":["iyilik","talimat"]
    }
}


with open("notes_data.json","w") as file:
    json.dump(notes,file)
#--




'''Uygulama arayüzü'''
#uygulama penceresi parametreleri
notes_win =QWidget()
notes_win.setWindowTitle('Akıllı notlar')
notes_win.resize(900,600)


#uygulama penceresi widget'ları
list_notes =QListWidget()
list_notes_label = QLabel('Notların Listesi')


button_note_create =QPushButton('Not oluştur')
button_note_del = QPushButton('Not Sil')
button_note_save = QPushButton('Notu Kaydet')


field_tag = QLineEdit('')#sağ alttaki küçük kutucuk
field_tag.setPlaceholderText('Etiketi giriniz..')
field_text =QTextEdit()#soldaki büyük alan


button_tag_add =QPushButton('Nota ekle')
button_tag_del =QPushButton('Nottan çıkar')
button_tag_search =QPushButton('Notları etikete göre ara')


list_tags = QListWidget()
list_tags_label =QLabel('Etiket listesi')
#anahat düzenine göre widget'ların konumu


layout_notes = QHBoxLayout()#genel yatay hizalama
col_1 =QVBoxLayout()#1.dikey çizgi
col_1.addWidget(field_text)


col_2=QVBoxLayout()#2.dikey
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)


row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)


row_2=QHBoxLayout()
row_2.addWidget(button_note_save)


col_2.addLayout(row_1)#2.dikey çizgiye ekle
col_2.addLayout(row_2)#2.dikey çizgiye ekle


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)


row_3 =QHBoxLayout()
row_3.addWidget(button_tag_add)#butonlar
row_3.addWidget(button_tag_del)


row_4 =QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)#2.dikeye yatay çizgi ekle
col_2.addLayout(row_4)




#ekranı 3'e bölüyoruz
layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)


#2.hafta
def show_note():
    key=list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["metin"])#sola içeriği gönder
    list_tags.clear()
    list_tags.addItems(notes[key]["etiketler"])#etiketler gönder


def add_note():
    note_name, ok=QInputDialog.getText(notes_win,"Not ekle","Notun adı:")
    if ok and note_name !="":
        notes[note_name]={"metin":"", "etiketler": []}#sözlük yapısı
        list_notes.addItem(note_name)#notlar listesine ekle
        list_tags.addItems(notes[note_name]["etiketler"])
        print(notes)


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["metin"] =field_text.toPlainText()
        with open ("notes_data.json","w") as file:
            json.dump(notes,file,sort_keys=True)
        print(notes)
    else:
        print("Kaydedilecek not seçili değil")


def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open ("notes_data.json","w") as file:
            json.dump(notes,file,sort_keys=True)
        print(notes)
    else:
        print("Silinecek not seçili değil.")
#olay işlemeyi bağlama
list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
#--






#uygulamayı başlatma 
notes_win.show()


#2.hafta
with open("notes_data.json","r") as file:
    notes=json.load(file)
list_notes.addItems(notes)


#--
app.exec_()


