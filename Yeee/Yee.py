from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import kivy.uix.image
from kivy.core.audio import SoundLoader



class MainLayout(FloatLayout):
    pass

class YeeApp(App):
    def build(self):
        return MainLayout()
    def play_sound(self ):
        print("Play")
        sound = SoundLoader.load('Yeee (online-audio-converter.com).wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

YeeApp().run()

