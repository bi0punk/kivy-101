import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

kivy.require('1.11.1')  # Reemplaza con tu versión de Kivy

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.label = Label(text="Presiona el botón para consultar la API")
        self.add_widget(self.label)

        self.button = Button(text="Consultar API")
        self.button.bind(on_press=self.consultar_api)
        self.add_widget(self.button)

    def consultar_api(self, instance):
        url = "https://tuapi.com/endpoint"  # Reemplaza con la URL de tu API
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            self.label.text = str(data)  # Muestra la respuesta en la etiqueta
        else:
            self.label.text = "Error en la consulta"

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
