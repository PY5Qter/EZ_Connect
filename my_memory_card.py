from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
 
app = QApplication([])
 
btn_OK = QPushButton('Ответить') 
btn_OK1 = QPushButton('назад') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=5) 
layout_line3.addStretch(1)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK1, stretch=1) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
 
def test():
    ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
    show_result() либо show_question() '''
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

def test1():
    ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
    show_result() либо show_question() '''
    if 'назад' == btn_OK1.text():
        show_question1()

def show_question1():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK1.setText('назад')


answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
q1 = Question(
    'Гос.язык Португалии',
    'Португальский', 
    'Английский', 'Испанский', 'Французский'
)
questions_list.append(q1)

q2 = Question(
    'Когда была Козахско-Динозаворская война?',
    '1256г до н.э.', 
    '5000г до н.э.', '3498г до н.э.', '2473г до н.э.'
)
questions_list.append(q2)

q3 = Question(
    'Лучшие карты в клеш рояль?',
    'Грибные', 
    'Легендарные', 'Эпические', 'Все'
)
questions_list.append(q3)

q4 = Question(
    'Кто подстрелил Пушкина на дуэли?',
    'Дантесс', 
    'Лермонтов', 'Лев Толстой', 'Сталин'
)
questions_list.append(q4)

q5 = Question(
    'У какого животного самый большой мозг?',
    'синий кит', 
    'мышь', 'дельфин', 'слон'
)
questions_list.append(q5)

q6 = Question(
    'Сколько звезд поставишь?',
    '5', 
    '4', '3', '2'
)
questions_list.append(q6)

q7 = Question(
    'Жили были дед и...',
    'баба', 
    'внучка', 'кошка', 'собачка'
)
questions_list.append(q7)

q8 = Question(
    'как зовут главного героя в фильме "Веном"?',
    'Эдди', 
    'Веном', 'Элизабет', 'Крис'
)
questions_list.append(q8)

q9 = Question(
    'Эгар из игры BS сильный?',
    'среднее', 
    'да', 'нет', 'возможно'
)
questions_list.append(q9)

q10 = Question(
    'Кто убил Альбуса Дамболдора?',
    'Проффесор Снек', 
    'Драко', 'Гермиона', 'Рон Уизли'
)
questions_list.append(q10)

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked:
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_OK) # проверяем, что панель ответов показывается при нажатии на кнопку
btn_OK1.clicked.connect(test)

window.score = 0
window.total = 0

window.resize(400, 300)
next_question()
window.show()
app.exec()