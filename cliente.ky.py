
from kivy.app import App
from kivy.lang import Builder

GUI= Builder.load_file("teste.ky.txt")

class Meuapp(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"].text 
        self.root.ids["moeda2"].text 
        self.root.ids["moeda3"].text
        self.root.ids["moeda4"].text
      
        
    def pegar_cotação(self,moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisiçao = request.get(link)
        dic_requisiçao= requisiçao.json
        cotacao = dic_requisiçao[f"{moeda}BRL"]["bid"]
        return cotacao
    
        
        
        