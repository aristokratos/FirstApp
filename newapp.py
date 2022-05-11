import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class babyApp(GridLayout):
    def __init__(self, **kwargs):
        super(babyApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Your Name'))
        self.y_name = TextInput( )
        self.add_widget(self.y_name)

        self.add_widget(Label(text='Your Scores'))
        self.y_scores = TextInput( )
        self.add_widget(self.y_scores)

        self.add_widget(Label(text='Your Gender'))
        self.y_gender = TextInput( )
        self.add_widget(self.y_gender)

        self.enter = Button(text = 'Enter here')
        self.enter.bind(on_press = self.submit_here)
        self.add_widget(self.enter)

    def submit_here(self, instance):
        print("Name of Student is "+self.y_name.text)
        print("Scores of Student is " + self.y_scores.text)
        print("Gender of Student is " + self.y_gender.text)
        print("")

class parentApp(App):
    def build(self):
        return babyApp()

if __name__ == "__main__":
    parentApp().run()