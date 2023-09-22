import time
import random
import tkinter as tk
import keyboard as keyb
from my import InvWin
from queue import Queue



class Meme(InvWin):


    def __init__(self):
        super().__init__()
        self.text_queue = Queue()
        self.running = True
        self.timer_running = False
        self.display_time = True
        self.playing_video = False

        self.start_time = 0
        self.meme_start_time = 0
        self.timer_label = None

        self.cena = random.randint(3,4)

        self.place_timelabel()
        self.meme_start()


    def run_meme_timer(self):
        if not self.running:
            return
        
        time_ = time.time() - self.meme_start_time

        if time_ > self.cena:
            self.cena = self.play_meme(
                'cena', 
                self.cena_audio, 
                self.cena,
                0.4675,
                0.533,
                1000 )
            
        self.root.after(20,self.run_meme_timer)


    def run_timer(self):
        if not self.timer_running:
            return

        float = time.time() - self.start_time
        time_str = self.format_time(float)

        if self.display_time:
            self.timer_label.lift()
            self.timer_label['text'] = time_str

        self.root.after(20,self.run_timer)
    

    def play_meme(self, keyname:str, audio:str, time_var : object, offx:int, offy:int, inc_time:int) -> int:
        """Returns incremented int value -> inc_time : int = Increment time for next call
        keyname : str = Get data frame from dictionary key,
        audio : str = Audio path,
        time_var : object =  class attr time referrence
        offx, offy : int = Label offset anchored to center,
        """
        if not self.playing_video:
            # keep condition from executing more than once in instant
            self.playing_video = True
            self.play_video(keyname, audio, offx, offy)
            # increment time trigger
            time_var += inc_time
            time_var = random.randint(time_var, time_var+200)
            # reset
            self.playing_video = False

            return time_var


    def format_time(self,time:float):
        # format float to str format
        hours = int(time / 3600) % 24
        mins = int(time / 60) % 60
        sec = time % 60
        
        return f'{hours:02d}:{mins:02d}:{sec:05.2f}'
    

    def timer_start(self):
        # starts timer
        self.start_time = time.time()
        self.run_timer()
    

    def meme_start(self):
        """start meme timer"""
        self.meme_start_time = time.time()
        self.run_meme_timer()


    def toggle_timer(self):
        self.timer_running = not self.timer_running
        if self.timer_running:
            self.timer_start()
        
    
    def show_timer(self):
        self.display_time = not self.display_time
        if not self.display_time:
            self.timer_label['text']=" "


    def place_timelabel(self):
        self.timer_label = tk.Label(
            text='00:00:00',
            font=(None,24),
            fg=self.text_color,
            bg=self.sac_color)

        self.timer_label.place(x=1150,y=30)

        keyb.add_hotkey('.+1', self.toggle_timer)
        keyb.add_hotkey('.+0', self.exit_)
        keyb.add_hotkey('.+2', self.show_timer)
    

    def exit_(self):
        self.runnin = False
        self.root.destroy()




if __name__=='__main__':
    app = Meme()
    app.main()
    input()

    pass