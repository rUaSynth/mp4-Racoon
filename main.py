from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pytube import YouTube
import os

class YTracoon(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6, 0.7)
        self.window.pos_hint={"center_x":0.5, "center_y":0.5}

        #image widget
        self.window.add_widget(Image(source="racoonLogo.png"))

        #label widget
        self.greeting=Label(
            text="Enter video URL",
            font_size = 20,
            color='white'
            )
        self.window.add_widget(self.greeting)

        #user input
        self.user=TextInput(
            multiline=False,
            padding_y=(20,20),
            size_hint=(1, 0.5)
            )
        self.window.add_widget(self.user)

        #button widget for video download
        self.button=Button(text="Download",
            size_hint=(1,0.5),
            bold=True,
            background_color='red'
            )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        #button widget for audio only download
        self.button=Button(text="Download audio only",
            size_hint=(1,0.5),
            bold=True,
            background_color='red'
            )
        self.button.bind(on_press=self.callback_audio)
        self.window.add_widget(self.button)


        return self.window
    
    def callback(self, instance):
        dir = os.path.join("C:\\","YTracoonDownloads")
        if not os.path.exists(dir):
            os.mkdir(dir)
        my_video = YouTube(self.user.text)
        my_video=my_video.streams.get_highest_resolution()
        my_video.download(dir)

    def callback_audio(self, instance):
        dir = os.path.join("C:\\","YTracoonDownloads")
        if not os.path.exists(dir):
            os.mkdir(dir)
        my_video = YouTube(self.user.text)
        my_video=my_video.streams.get_audio_only()
        my_video.download(dir)



if __name__ == "__main__":
    YTracoon().run()
