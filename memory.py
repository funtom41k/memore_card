from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, correct, wrong1, wrong2, wrong3):
        self.question = question
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

list_questions = list()
list_questions.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))
list_questions.append(Question('Государственный язык Бразилии?', 'Португальский', 'Испанский', 'Бразильский', 'Итальянский'))
list_questions.append(Question('Какое самое маленько государство?', 'Ватикан', 'Мальта', 'Монако', 'Мальдивы'))
list_questions.append(Question('Какой самый большой остров в России?', 'Сахалин', 'Врангеля', 'Котельный', 'Новая Земля'))
list_questions.append(Question('Сколько независимых государств расположено в Южной Америке?', '12', '15', '7', '3'))
list_questions.append(Question('В каком веке была открыта Австралия?', '17', '16', '19', '18'))
list_questions.append(Question('Сколько субъектов на территори РФ?', '89', '72', '67', '86'))
list_questions.append(Question('Столица Бельгии?', 'Брюсель', 'Берлин', 'Бухарест', 'Париж'))
list_questions.append(Question('Сколько континентов на Земле?', '6', '5', '4', '7'))
list_questions.append(Question('Столица Нигерии?', 'Абуджа', 'Банжул', 'Мапуту', 'Хартум'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo Card')
main_win.resize(500, 350)

LBquestion = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')

#группа вопросов
RadioGroupBox = QGroupBox('Варианты ответов')
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Чулымцы')
ans3 = QRadioButton('Смурфы')
ans4 = QRadioButton('Алеуты')
answers  = [ans1, ans2, ans3, ans4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(ans1)
RadioGroup.addButton(ans2)
RadioGroup.addButton(ans3)
RadioGroup.addButton(ans4)

layot_quest_main = QHBoxLayout()
layot_quest1 = QVBoxLayout()
layot_quest2 = QVBoxLayout()

layot_quest1.addWidget(ans1)
layot_quest1.addWidget(ans2)
layot_quest2.addWidget(ans3)
layot_quest2.addWidget(ans4)

layot_quest_main.addLayout(layot_quest1)
layot_quest_main.addLayout(layot_quest2)
RadioGroupBox.setLayout(layot_quest_main)

#группа отвтеов
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
correct_ans = QLabel('Правильный ответ')
stat = QLabel('Рейтинг:')
                                                           
layout_ans_main = QVBoxLayout()
layout_ans_main.addWidget(result, alignment=Qt.AlignLeft)
layout_ans_main.addWidget(correct_ans, alignment=Qt.AlignCenter)
layout_ans_main.addWidget(stat, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_ans_main)

main_layout = QVBoxLayout()
layout_H1 = QHBoxLayout()
layout_H2 = QHBoxLayout()
layout_H3 = QHBoxLayout()

layout_H1.addWidget(LBquestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_H2.addWidget(RadioGroupBox)
layout_H2.addWidget(AnsGroupBox)

layout_H3.addStretch(1)
layout_H3.addWidget(button, stretch=2)
layout_H3.addStretch(1)

main_layout.setSpacing(5)
main_layout.addLayout(layout_H1, stretch=1)
main_layout.addLayout(layout_H2, stretch=5)
main_layout.addStretch(1)
main_layout.addLayout(layout_H3, stretch=2)
main_layout.addStretch(1)
main_win.setLayout(main_layout)
AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    LBquestion.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.correct) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2) 
    answers[3].setText(q.wrong3)
    correct_ans.setText(q.correct)
    show_question()

main_win.score = 0
main_win.total = 0

def check_answer():
    if answers[0].isChecked():
        result.setText('Правильно')
        main_win.score += 1
    else:
        result.setText('Неправильно')
    stat.setText('Рейтинг: ' + str(round(main_win.score / main_win.total * 100, 1)) + '%')
    show_result()
    print('Статистика')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг:', main_win.score / main_win.total * 100)

def next_question():
    curquestion = randint(0, len(list_questions) - 1)
    ask(list_questions[curquestion])
    main_win.total += 1
    print('Статистика')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    
next_question()

button.clicked.connect(click_OK)

main_win.show()
app.exec()