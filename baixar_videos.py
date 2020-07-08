import os
from tkinter import *
from pytube import YouTube

class App():
    def __init__(self, master):
        self.master = master
        root = master
        root.title("Baixador de Vídeos")
        root.geometry('370x420')
        self.desktop = os.path.join(os.environ['USERPROFILE'], "desktop")
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
                text='Baixar', command= lambda:
                                 self.download_mp4(entrada_url, resultado))

        download_button.pack()
        resultado.pack(pady=20)

    def download_mp4(self, url, label):
        
        try:
            yt = YouTube(url.get())
        except:
            label.config(text="Error. Cheque sua Conexão!")
        
        title = self.verificaTitle(yt.title)
        label.config(text="Baixando:\n" + title)
        yt.streams.first().download(output_path=self.desktop, filename=title)
        self.conversao_mp3(title,label)

    def verificaTitle(self, title):
        if "#" in title:
            title = title[:title.index("#")]
        return title

    def conversao_mp3(self,title, label):
        label.config(text="Convertendo\n" + title + "para MP3")
        titlemp4 = title + '.mp4'
        dirname = os.path.dirname(__file__)
        os.chdir(dirname + "//ffmpeg//bin")
        command_conversion = ("ffmpeg -i \"" + os.path.join(self.desktop, titlemp4) + "\" \"" +
                            os.path.join(self.desktop, title + '.mp3') + "\"")
        os.system(command_conversion)
        self.remove_old_file( titlemp4, self.desktop)
        

    def remove_old_file(self, title, dest):
        os.remove( os.path.join(dest, title))

if '__main__' == __name__:
    root = Tk()
    App(root)
    
     
