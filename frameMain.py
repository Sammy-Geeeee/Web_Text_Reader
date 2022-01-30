# This is to define the main frame for the program


import tkinter as tk
from functions import *
import pyperclip


class FrameMain(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Some variables for the sizing of various things
        pad_ext = 5
        label_width = 5
    

        # Main frames
        self.frame_url = tk.Frame(self.master)
        self.frame_article = tk.Frame(self.master)
        # To position these frames
        self.frame_url.grid(row=0, column=0, padx=pad_ext, pady=pad_ext, sticky='n')  # To set the main frames in the window
        self.frame_article.grid(row=1, column=0, padx=pad_ext, pady=pad_ext, sticky='n')
        # To edit the frames and columns
        self.frame_url.columnconfigure([1], weight=1)  # To let the elements stretch
        self.frame_article.columnconfigure([0], weight=1)
        self.frame_article.rowconfigure([0], weight=1)
        

        # URL Frame widgets
        self.label_url = tk.Label(self.frame_url, width=label_width, text='URL')
        self.entry_url = tk.Entry(self.frame_url, width=1000)
        self.button_paste = tk.Button(self.frame_url, command=self.pasteUrl, text='Paste')
        self.button_generate = tk.Button(self.frame_url, command=self.showArticle, text='Display Article')
        # To position these widgets
        self.label_url.grid(row=0, column=0, padx=pad_ext, pady=pad_ext)
        self.entry_url.grid(row=0, column=1, padx=pad_ext, pady=pad_ext, sticky='ew')
        self.button_paste.grid(row=0, column=2, padx=pad_ext, pady=pad_ext)
        self.button_generate.grid(row=1, column=0, columnspan=3, padx=pad_ext, pady=pad_ext)


        # Article Frame Widgets
        self.scroll_article = tk.Scrollbar(self.frame_article)
        self.text_article = tk.Text(self.frame_article, width=1000, height=1000, yscrollcommand=self.scroll_article.set)
        # To position these widgets
        self.text_article.grid(row=0, column=0, padx=[pad_ext, 0], pady=pad_ext, sticky='nesw')
        self.scroll_article.grid(row=0, column=1, padx=[0, pad_ext], pady=pad_ext, sticky='ns')
        # Configurations for various things
        self.text_article.config(wrap=tk.WORD)
        self.scroll_article.config(command=self.text_article.yview)
        
        
    # Program Functions
    def pasteUrl(self):
        clipboard_text = pyperclip.paste()
        self.entry_url.delete(0, tk.END)
        self.entry_url.insert(0, clipboard_text)
    

    def showArticle(self):
        url = self.entry_url.get()
        article = findText(url)
        self.text_article.delete('1.0', tk.END)
        self.text_article.insert('1.0', article)
