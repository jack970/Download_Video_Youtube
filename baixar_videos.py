import os
from tkinter import *
from pytube import YouTube

class App():
    def __init__(self, master):
        self.master = master
        root = master
        root.title("Baixador de Vídeos")
        root.geometry('370x420')
        self.home()

    def home(self):
        titulo_label = Label(self.master,
            text="Baixador de Músicas\ndo Youtube", font=("Courier", 14))
        titulo_label.pack(pady=30)

        self.widget1 = Frame(self.master)
        self.widget1.pack()

        insira_label = Label(self.widget1, text="Insira a URL:")
        insira_label.pack()
        
        entrada_url = Entry(self.widget1, width=44)
        entrada_url.pack(pady=20)

        resultado = Label(self.master, text='')

        download_button = Button(self.widget1,
                text='Baixar', command= lambda: self.download_mp3(entrada_url, resultado))

        download_button.pack()
        resultado.pack(pady=20)

    def download_mp3(self, url, label):
        try:
            self.desktop = os.path.join(os.environ['USERPROFILE'], "desktop")
            yt = YouTube(url.get())
            title = yt.player_response['videoDetails']['title']
            label.config(text="Baixando:\n" + title)
            yt.streams.first().download(output_path=self.desktop, filename=title)
            self.conversao_mp3(title,label)
        except:
            label.config(text="Ocorreu um erro ao baixar!")

    def conversao_mp3(self,title, label):
        label.config(text="Convertendo para MP3")
        title = title + '.mp4'
        dirname = os.path.dirname(__file__)
        os.chdir(dirname + "//ffmpeg//bin")
        os.system("ffmpeg -i \"" + os.path.join(self.desktop, title) + "\" \"" +
        os.path.join(self.desktop, title.replace('mp4','mp3')) + "\"")

if '__main__' == __name__:
    root = Tk()
    App(root)
    
     
