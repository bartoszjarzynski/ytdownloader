from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def closing_app():
    quit()

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget('text')
    screen.title('Pobieranie..')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Pobieranie zakończone!')

screen = Tk()
title = screen.title('DownloaderYT')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

link_field = Entry(screen, width=50)
link_label = Label(screen, text='Wpisz link: ', font=('Arial', 15))

path_label = Label(screen, text= 'DownloaderYT', font=('Arial', 10) )
select_btn = Button(screen, text='DownloaderYT',)
canvas.create_window(450, 490, window=path_label)


path_label = Label(screen, text= 'Gdzie zapisać plik:', font=('Arial', 11) )
select_btn = Button(screen, text='Wybierz', command=select_path)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

download_btn = Button(screen, text='Pobierz', command=download_file)
canvas.create_window(250, 390, window=download_btn)

close_btn = Button(screen, text='Wyjdz', command=closing_app)
canvas.create_window(250,450, window=close_btn)

screen.mainloop()