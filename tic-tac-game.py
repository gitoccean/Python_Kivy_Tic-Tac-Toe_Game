from kivy.app import App
from kivy.lang import Builder


class Tictactoe(App):
    def build(self):
        return Builder.load_file("tic-tac-game.kv")

    turn = 'x'
    winner = False

    def draw(self):
        if self.winner == False and \
                self.root.ids.btn1.disabled == True and \
                self.root.ids.btn2.disabled == True and \
                self.root.ids.btn3.disabled == True and \
                self.root.ids.btn4.disabled == True and \
                self.root.ids.btn5.disabled == True and \
                self.root.ids.btn6.disabled == True and \
                self.root.ids.btn7.disabled == True and \
                self.root.ids.btn8.disabled == True and \
                self.root.ids.btn9.disabled == True:
            self.root.ids.score.text = "Its a tie"

    def end_game(self, btn1, btn2, btn3):

        self.winner = True
        btn1.color = 'red'
        btn2.color = 'red'
        btn3.color = 'red'

        self.disable_all_button()

        self.root.ids.score.text = f'{btn1.text} win'

    def disable_all_button(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def win(self):
        if self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

        if self.root.ids.btn4.text != '' and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
            self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

        if self.root.ids.btn7.text != '' and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

            # Down
        if self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

        if self.root.ids.btn2.text != '' and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
            self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

        if self.root.ids.btn3.text != '' and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

            # Diagonal
        if self.root.ids.btn1.text != '' and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        if self.root.ids.btn3.text != '' and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

        self.draw()

    def presser(self, btn):
        if self.turn == "x":
            btn.text = 'x'
            btn.disabled = True
            self.root.ids.score.text = "o\'s turn!"
            self.turn = 'o'
        else:
            btn.text = 'o'
            btn.disabled = True
            self.root.ids.score.text = "x\'s turn!"
            self.turn = 'x'
        self.win()

    def restart(self):
        self.turn = 'x'

        # if u want to get id outside of function then self.root.ids.
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        self.root.ids.btn1.color = 'green'
        self.root.ids.btn2.color = 'green'
        self.root.ids.btn3.color = 'green'
        self.root.ids.btn4.color = 'green'
        self.root.ids.btn5.color = 'green'
        self.root.ids.btn6.color = 'green'
        self.root.ids.btn7.color = 'green'
        self.root.ids.btn8.color = 'green'
        self.root.ids.btn9.color = 'green'

        self.root.ids.score.text = "x\'s Goes First!"
        self.winner = False


Tictactoe().run()
