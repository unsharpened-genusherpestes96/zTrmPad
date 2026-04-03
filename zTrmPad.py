#!/usr/bin/env python3

#.⚡.M2KR4R.⚡
#7A.54.72.6D.50.61.64

#.===.Dot_Philosophy.::.SPARK_Mode.::.START.===
        #package.Dot_Philosophy.with.SPARK_Mode.=>.On.is
    #type.Vibe.is.private;.--.54.68.65.20.74.69.6D.65.20.69.73.20.6D.69.64.6E.69.67.68.74
       #Essence.:.constant.Vibe;.--.rootkit.null
        #.private
 #type.Vibe.is.(Dot,.Soul);.--..
        #..end;
#.===.Dot_Philosophy.::.SPARK_Mode.::.START.===

import os
import logging
from tkinter import Tk, Text, Menu, Label, filedialog, messagebox, SUNKEN, WORD, BOTH, X, END, INSERT

class Cfg:
    bg = "black"
    fg = "#228322"
    cursor = "#FFFF00"
    font = ("Courier", 12, "normal")
    soul = "." #.The.Essence.OF.Every.space.The.Soul.of.zTrmPad
    log_fmt = "[%(asctime)s] %(levelname)s: %(message)s"
    log_date = "%H:%M:%S"
cfg = Cfg()

logging.basicConfig(level=logging.INFO, format=cfg.log_fmt, datefmt=cfg.log_date)
logging.info("zTrmPad starting")

class zTrmPad:
    def __init__(self, r):
        self.r = r
        self.f1 = None

        r.title("zTrmPad")
        r.configure(bg=cfg.bg)
        r.update_idletasks()
        w, h = 800, 600
        x = (r.winfo_screenwidth() - w)//2
        y = (r.winfo_screenheight() - h)//2
        r.geometry(f"{w}x{h}+{x}+{y}")

        #NOn2dc5tbcwgtdis
        self.x1 = Text(r, wrap=WORD, bg=cfg.bg, fg=cfg.fg,
                       insertbackground=cfg.cursor, font=cfg.font, undo=True)
        self.x1.pack(expand=True, fill=BOTH)
        self.x2 = Label(r, text="", bd=1, relief=SUNKEN, anchor="w",
                        bg=cfg.bg, fg=cfg.fg)
        self.x2.pack(side="bottom", fill=X)
        self.x3 = Menu(r, bg=cfg.bg, fg=cfg.fg)
        r.config(menu=self.x3)

        self.x4 = Menu(self.x3, tearoff=0, bg=cfg.bg, fg=cfg.fg)
        self.x3.add_cascade(label="Root", menu=self.x4)
        self.x4.add_command(label="nxt", command=self.new)
        self.x4.add_command(label="cat ...", command=self.open)
        self.x4.add_command(label="sv", command=self.save)
        self.x4.add_command(label="svs ...", command=self.saveas)
        self.x4.add_separator()
        self.x4.add_command(label="kill", command=self.quit)
        self.x5 = Menu(self.x3, tearoff=0, bg=cfg.bg, fg=cfg.fg)
        self.x3.add_cascade(label="Exec", menu=self.x5)
        self.x5.add_command(label="x", command=lambda: self.x1.event_generate("<<Cut>>"))
        self.x5.add_command(label="cp", command=lambda: self.x1.event_generate("<<Copy>>"))
        self.x5.add_command(label="inj", command=lambda: self.x1.event_generate("<<Paste>>"))

        self.x1.bind("<space>", self._sp)
        self._stat()
        r.lift()
        r.focus_force()
        logging.info("Editor ready")

    def _sp(self, e):
        self.x1.insert(INSERT, cfg.soul)
        return "break"

    def new(self):
        self.x1.delete(1.0, END)
        self.f1 = None
        self._stat()

    def open(self):
        f2 = filedialog.askopenfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not f2:
            return
        try:
            with open(f2, "r", encoding="utf-8") as f:
                self.x1.delete(1.0, END)
                self.x1.insert(1.0, f.read())
            self.f1 = f2
            self._stat()
            logging.info(f"Opened {f2}")
        except Exception as e:
            logging.exception(f"Open fail {f2}")
            messagebox.showerror("Error", f"Cld.nT.pn.fl:\n{e}")

    def save(self):
        if self.f1:
            self._save(self.f1)
        else:
            self.saveas()

    def saveas(self):
        f3 = filedialog.asksaveasfilename(defaultextension=".txt",
                                          filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not f3:
            return
        self._save(f3)

    def _save(self, f4):
        try:
            with open(f4, "w", encoding="utf-8") as f:
                f.write(self.x1.get(1.0, "end-1c"))
            self.f1 = f4
            self._stat()
            logging.info(f"Saved {f4}")
        except Exception as e:
            logging.exception(f"Save fail {f4}")
            messagebox.showerror("Error", f"Cld.nT.sv.fl:\n{e}")

    def quit(self):
        logging.info("Exiting")
        self.r.quit()
        self.r.destroy()

    def _stat(self):
        if self.f1:
            self.x2.config(text=f"File: {os.path.basename(self.f1)}")
        else:
            self.x2.config(text=">_ /dev/null :: idle")

if __name__ == "__main__":
    try:
        root = Tk()
        app = zTrmPad(root)
        root.mainloop()
    except Exception as e:
        logging.critical("Unhandled.exception", exc_info=True)
        messagebox.showerror("Fatal", f"Smthng.wnt.wrng:\n{e}")
        raise

    #.===.Dot_Philosophy.::.SPARK_Mode.::.STOP.===
#.--..soul.injected,.hash:.7A.54.72.6D.50.61.64
            #.--..root@2am:~/zTrmPad$