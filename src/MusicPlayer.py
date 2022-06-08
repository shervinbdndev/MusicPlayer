try:
    import os
    import time
    import pickle
    import sv_ttk
    import tkinter
    import ntkutils
    import darkdetect
    import webbrowser
    from typing import Any
    from pygame import mixer
    from mutagen.mp3 import MP3
    from tkinter import filedialog
    from typing_extensions import Self
    from customtkinter.widgets.customtkinter_button import CTkButton
    from tkinter.ttk import (Notebook , Frame , Scrollbar , Scale as S)
    from tkinter.__init__ import (LabelFrame , DoubleVar , Listbox , Scale , Label)
    
    from Management import Materials

except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run The Application') from None

finally:
    ...
    






class MusicPlayerMainClass:
    def __init__(self : Self) -> None:
        super(MusicPlayerMainClass , self).__init__()
        self.root = tkinter.Tk()
        self.root.title(string='Music Player')
        self.root.geometry(newGeometry='400x700')
        self.root.resizable(width=False , height=False)
        self.root.iconbitmap(bitmap=os.path.join(os.path.abspath(path=os.path.dirname(p=__file__)) , r'images/icon.ico'))
        self.tabControl = Notebook(master=self.root)
        self.tabMusic = Frame(master=self.tabControl)
        self.tabList = Frame(master=self.tabControl)
        self.tabLang = Frame(master=self.tabControl)
        self.tabAbout = Frame(master=self.tabControl)
        self.tabControl.add(child=self.tabMusic , text='Song')
        self.tabControl.add(child=self.tabList , text='Playlist')
        self.tabControl.add(child=self.tabLang , text='Language')
        self.tabControl.add(child=self.tabAbout , text='About')
        self.tabControl.pack(expand=1 , fill=Materials.Alignments.both)
        self.songList : list = []
        self.volume = DoubleVar(master=self.tabMusic)
        self.current : int = 0
        self.pause : bool = True
        self.play : bool = False
        mixer.init()
        
        if (os.path.exists(path='songs.pickle')):
            with open(file='songs.pickle' , mode='rb') as F:
                self.playList = pickle.load(file=F)
        else:
            self.playList : list = []
        
        def getTheme() -> None:
            if (darkdetect.isLight()):
                sv_ttk.set_theme(theme='light')
                self.cover.configure(foreground=Materials.Colors.green)
                self.slider.configure(foreground=Materials.Colors.green)
                self.controls.configure(foreground=Materials.Colors.green)
                self.musicTime.configure(foreground=Materials.Colors.green)
                self.playListMusics.configure(foreground=Materials.Colors.green)
                self.btnLoadSong.configure(fg_color=Materials.Colors.green)
                self.btnPrev.configure(fg_color=Materials.Colors.white , hover_color=Materials.Colors.green)
                self.btnPause.configure(fg_color=Materials.Colors.white , hover_color=Materials.Colors.green)
                self.btnNext.configure(fg_color=Materials.Colors.white , hover_color=Materials.Colors.green)
                self.btnPA.configure(fg_color=Materials.Colors.green , bg_color=Materials.Colors.white)
                self.btnEN.configure(fg_color=Materials.Colors.green , bg_color=Materials.Colors.white)
                self.btnGithub.configure(fg_color=Materials.Colors.green , bg_color=Materials.Colors.white)
            if (darkdetect.isDark()):
                sv_ttk.set_theme(theme='dark')
                self.cover.configure(foreground=Materials.Colors.green)
                self.slider.configure(foreground=Materials.Colors.green)
                self.controls.configure(foreground=Materials.Colors.green)
                self.musicTime.configure(foreground=Materials.Colors.green)
                self.playListMusics.configure(foreground=Materials.Colors.green)
                self.btnLoadSong.configure(fg_color=Materials.Colors.green , bg_color=Materials.Colors.dark)
                self.btnPrev.configure(fg_color=Materials.Colors.dark , bg_color=Materials.Colors.dark , hover_color=Materials.Colors.green)
                self.btnPause.configure(fg_color=Materials.Colors.dark , bg_color=Materials.Colors.dark , hover_color=Materials.Colors.green)
                self.btnNext.configure(fg_color=Materials.Colors.dark , bg_color=Materials.Colors.dark , hover_color=Materials.Colors.green)
                self.btnPA.configure(fg_color=Materials.Colors.green , bg_color=Materials.Colors.dark)
                self.btnEN.configure(fg_color=Materials.Colors.green , bg_color=Materials.Colors.dark)
                self.btnGithub.configure(fg_color=Materials.Colors.green , bg_color=Materials.Colors.dark)
                ntkutils.dark_title_bar(window=self.root)
                
        def getLanguage(arg : Any) -> None:
            if (arg == 'pa'):
                self.tabControl.add(child=self.tabMusic , text='آهنگ')
                self.tabControl.add(child=self.tabList , text='لیست پخش')
                self.tabControl.add(child=self.tabLang , text='زبان')
                self.tabControl.add(child=self.tabAbout , text='درباره')
                self.root.title(string='موزیک پلیر')
                self.cover['text'] = 'آهنگ ها'
                self.controls['text'] = 'کنترل ها'
                self.playListMusics['text'] = f'لیست پخش - {len(self.playList)}'
                self.btnPA.configure(text='پارسی')
                self.btnEN.configure(text='انگلیسی')
                self.btnGithub.configure(text='گیتهاب')
            elif (arg == 'en'):
                self.tabControl.add(child=self.tabMusic , text='Song')
                self.tabControl.add(child=self.tabList , text='Playlist')
                self.tabControl.add(child=self.tabLang , text='Language')
                self.tabControl.add(child=self.tabAbout , text='About')
                self.root.title(string='Music Player')
                self.cover['text'] = 'Songs'
                self.controls['text'] = 'Controls'
                self.playListMusics['text'] = f'Playlist - {len(self.playList)}'
                self.btnPA.configure(text='Persian')
                self.btnEN.configure(text='English')
                self.btnGithub.configure(text='Github')
            
        def openGithub(arg : Any) -> None:
            if (arg == 'opgh'):
                webbrowser.open(url='https://github.com/shervinbdndev/')
                
        def loadSong(arg : Any) -> None:
            if (arg == 'load'):
                directory = filedialog.askdirectory()
                for root , dirs , files in os.walk(top=directory):
                    for file in files:
                        if (os.path.splitext(p=file)[1] == '.mp3'):
                            path = (f'{root}/{file}').replace('\\' , '/')
                            self.songList.append(path)
                with open(file='songs.pickle' , mode='wb') as F:
                    pickle.dump(self.songList , F)
                self.playList = self.songList
                self.playListMusics['text'] = f'Playlist - {len(self.playList)}'
                self.list.delete(first=0 , last=Materials.Constants.end)
                countSongs()
                
        def getSongInfo() -> None:
            currentTime = mixer.music.get_pos() / 1000
            convertedTime = time.strftime('%H:%M:%S' , time.gmtime(currentTime))
            global songLength
            songLength = MP3(self.playList[self.current]).info.length
            convertedSongLength = time.strftime('%H:%M:%S' , time.gmtime(songLength))
            currentTime += 1
            if (int(self.musicSlider.get()) == int(songLength)):
                self.musicTime.configure(text=f'{convertedSongLength}')
            elif (self.pause):
                pass
            elif (int(self.musicSlider.get()) == int(currentTime)):
                sliderPos = int(songLength)
                self.musicSlider.configure(to=sliderPos , value=int(currentTime))
            else:
                sliderPos = int(songLength)
                self.musicSlider.configure(to=sliderPos , value=int(self.musicSlider.get()))
                convertedTime = time.strftime('%H:%M:%S' , time.gmtime(int(self.musicSlider.get())))
                self.musicTime.configure(text=f'{convertedTime} / {convertedSongLength}')
                nextTime = int(self.musicSlider.get()) + 1
                self.musicSlider.configure(value=nextTime)
            self.musicTime.after(ms=1000 , func=getSongInfo)
                
        def previousSong(arg : Any) -> None:
            if (arg == 'prev'):
                if (self.current > 0):
                    self.current -= 1
                else:
                    self.current = 0
                self.list.itemconfigure(index=self.current)
                self.musicSlider['value'] = 0
                playSong()
            
        def pauseSong(arg : Any) -> None:
            if (arg == 'pause'):
                if (not self.pause):
                    self.pause = True
                    mixer.music.pause()
                    self.btnPause.configure(text='▶')
                else:
                    if (self.play is False):
                        playSong()
                    self.pause = False
                    mixer.music.unpause()
                    self.btnPause.configure(text='⏸')
            
        def playSong(event=None) -> None:
            if (event is not None):
                self.current = self.list.curselection()[0]
                for i in range(len(self.playList)):
                    self.list.itemconfigure(index=i)
            self.btnPause.configure(text='⏸')
            self.pause = False
            self.play = True
            mixer.music.load(filename=self.playList[self.current])
            self.cover['text'] = os.path.basename(p=self.playList[self.current])
            self.list.activate(index=self.current)
            self.list.itemconfigure(index=self.current)
            mixer.music.play(loops=0)
            getSongInfo()
            
        def musicSliderPlay(event=None) -> None:
            mixer.music.play(start=int(self.musicSlider.get()))
            
        def nextSong(arg : Any) -> None:
            if (arg == 'nxt'):
                if (self.current < len(self.playList) - 1):
                    self.current += 1
                else:
                    self.current = 0
                self.list.itemconfigure(index=self.current)
                self.musicSlider['value'] = 0
                playSong()
            
        def changeSongVolume(event=None) -> None:
            mixer.music.set_volume(self.slider.get())
            
        def countSongs() -> None:
            for index , song in enumerate(self.playList):
                self.list.insert(index , os.path.basename(p=song))
        
        self.cover = LabelFrame(
            master=self.tabMusic ,
            text='Song' ,
            font=(Materials.Fonts.normal , 12 , Materials.Fonts.bold) ,
        )
        
        self.cover.place(relx=0.5 , rely=0.25 , anchor=Materials.Alignments.center)
        
        self.cover.configure(width=360 , height=300)
        
        self.playListMusics = LabelFrame(
            master=self.tabList ,
            font=(Materials.Fonts.normal , 12 , Materials.Fonts.bold) ,
            text=r'Playlist - 0'
        )
        
        self.playListMusics.place(relx=0.5 , rely=0.44 , anchor=Materials.Alignments.center)
        
        self.playListMusics.configure(width=360 , height=550)
        
        self.scrollSongs = Scrollbar(
            master=self.tabList ,
            orient=Materials.Alignments.vertical
        )
        
        self.scrollSongs.place(relx=0.9 , rely=0.2 , anchor=Materials.Alignments.center)
        
        self.list = Listbox(
            master=self.tabList ,
            selectmode=Materials.Alignments.single ,
            yscrollcommand=self.scrollSongs.set ,
            width=59 ,
            height=32
        )
        
        self.list.place(relx=0.502 , rely=0.465 , anchor=Materials.Alignments.center)
        
        self.scrollSongs.configure(command=self.list.yview)
        
        self.controls = LabelFrame(
            master=self.tabMusic ,
            font=(Materials.Fonts.normal , 12 , Materials.Fonts.bold) ,
            bd=1 ,
            text='Controls' ,
            border=1 ,
            borderwidth=1
        )
        
        self.controls.place(relx=0.5 , rely=0.88 , anchor=Materials.Alignments.center)
        
        self.controls.configure(width=360 , height=100)
        
        self.btnLoadSong = CTkButton(
            master=self.tabList ,
            text= '+',
            corner_radius=6 ,
            text_font=(Materials.Fonts.normal , 25) ,
            width=50 ,
            height=40 ,
            border_width=0,
            cursor=Materials.Cursors.hand,
            command=lambda:loadSong(arg='load')
        )
        
        self.btnLoadSong.place(relx=0.11 , rely=0.9 , anchor=Materials.Alignments.center)
        
        self.btnPrev = CTkButton(
            master=self.tabMusic ,
            text= '⏮',
            corner_radius=10 ,
            text_font=(Materials.Fonts.normal , 22) ,
            width=5 ,
            height=20 ,
            border_width=0,
            cursor=Materials.Cursors.hand,
            command=lambda:previousSong(arg='prev')
        )
        
        self.btnPrev.place(relx=0.15 , rely=0.88 , anchor=Materials.Alignments.center)
        
        self.btnPause = CTkButton(
            master=self.tabMusic ,
            text= '▶',
            corner_radius=10 ,
            text_font=(Materials.Fonts.normal , 22) ,
            width=5,
            height=5,
            border_width=0,
            cursor=Materials.Cursors.hand,
            command=lambda:pauseSong(arg='pause')
        )
        
        self.btnPause.place(relx=0.33 , rely=0.88 , anchor=Materials.Alignments.center)
        
        self.btnNext = CTkButton(
            master=self.tabMusic ,
            text= '⏭',
            corner_radius=10 ,
            text_font=(Materials.Fonts.normal , 22) ,
            width=5,
            height=5,
            border_width=0,
            cursor=Materials.Cursors.hand,
            command=lambda:nextSong(arg='nxt')
        )
        
        self.btnNext.place(relx=0.51 , rely=0.88 , anchor=Materials.Alignments.center)
        
        self.btnPA = CTkButton(
            master=self.tabLang ,
            text= 'Persian',
            corner_radius=8 ,
            text_font=(Materials.Fonts.normal , 20) ,
            width=30,
            height=5,
            cursor=Materials.Cursors.hand,
            command=lambda:getLanguage(arg='pa')
        )
        
        self.btnPA.place(relx=0.33 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.btnEN = CTkButton(
            master=self.tabLang ,
            text= 'English',
            corner_radius=8 ,
            text_font=(Materials.Fonts.normal , 20) ,
            width=30,
            height=5,
            cursor=Materials.Cursors.hand,
            command=lambda:getLanguage(arg='en')
        )
        
        self.btnEN.place(relx=0.68 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.btnGithub = CTkButton(
            master=self.tabAbout ,
            text= 'Github',
            corner_radius=8 ,
            text_font=(Materials.Fonts.normal , 20) ,
            width=30,
            height=5,
            cursor=Materials.Cursors.hand,
            command=lambda:openGithub(arg='opgh')
        )
        
        self.btnGithub.place(relx=0.5 , rely=0.5 , anchor=Materials.Alignments.center)
        
        self.slider = Scale(
            master=self.tabMusic ,
            from_=0 ,
            to=1 ,
            orient=Materials.Alignments.horizantal ,
            variable=self.volume ,
            cursor=Materials.Cursors.hand ,
            command=changeSongVolume
        )
        
        self.musicSlider = S(
            master=self.tabMusic ,
            from_=0 ,
            to=100 ,
            orient=Materials.Alignments.horizantal ,
            value=0 ,
            command=musicSliderPlay ,
            cursor=Materials.Cursors.hand
        )
        
        self.musicSlider.place(relx=0.5 , rely=0.7 , width=300 , anchor=Materials.Alignments.center)
        
        self.musicTime = Label(
            master=self.tabMusic ,
            font=(Materials.Fonts.normal , 22 , Materials.Fonts.bold) ,
            text='00:00:00 / 00:00:00'
        )
        
        self.musicTime.place(relx=0.5 , rely=0.58 , anchor=Materials.Alignments.center)
        
        self.slider.set(value=1)
        
        mixer.music.set_volume(1)
        
        self.slider.place(relx=0.75 , rely=0.87 , width=100 , anchor=Materials.Alignments.center)
        
        self.list.bind(sequence='<Double-1>' , func=playSong)
        
        getTheme()
        
        self.root.mainloop()
        
        
        

if (__name__ == '__main__' and __package__ is None):
    MusicPlayerMainClass()