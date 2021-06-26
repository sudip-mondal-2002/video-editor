from tkinter import filedialog, Label, Scale, Tk, Button, HORIZONTAL, GROOVE
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
import datetime

def mix():
    files = []

    def addFile():
        try:
            filePath = filedialog.askopenfilename(title='select', filetypes=[
                ("all video format", ".mp4"),
                ("all video format", ".flv"),
                ("all video format", ".avi"),
            ])
            files.append(VideoFileClip(filePath))
            l = Label(tk, text=filePath)
            l.pack()
        except:
            print("choose only videos")

    def mixFiles():
        final_clip = concatenate_videoclips(files)
        folder = filedialog.askdirectory()
        name = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        final_clip.write_videofile(folder+"/"+name+".mp4")

    def onClose():
        root.deiconify()
        tk.destroy()
    root.withdraw()
    tk = Tk()
    tk.config(bg="#232323")
    tk.protocol("WM_DELETE_WINDOW", onClose)
    addFileButton = Button(tk, text="+ Add a file",
                           bg="#232323", fg="#ffffff", command=addFile)
    addFileButton.pack()
    doneButton = Button(tk, text="Done", bg="#232323",
                        fg="#ffffff", command=mixFiles)
    doneButton.pack()
    tk.mainloop()


def mirror():
    try:
        filePath = filedialog.askopenfilename(title='select', filetypes=[
            ("all video format", ".mp4"),
            ("all video format", ".flv"),
            ("all video format", ".avi"),
        ])
        clip = VideoFileClip(filePath)
        clip_mirror = clip.fx(vfx.mirror_x)
        folder = filedialog.askdirectory()
        name = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        clip_mirror.write_videofile(folder+"/"+name+".mp4")
    except:
        print("choose only videos")

# def resize():
#     r=float(input("Enter your size : "))
#     clip_resize = clip1.resize(r)
#     clip_resize.write_videofile("Final render.mp4")

# def speed():
#     speedValue = float(input("Enter your speed : "))
#     clip_speed = clip1.fx(vfx.speedx, speedValue)
#     clip_speed.write_videofile("Final render.mp4")


def color():
    def onClose():
        root.deiconify()
        tk.destroy()
    def createVideo():
        try:
            clip_color = clip.fx(vfx.colorx, colorvalue)
            folder = filedialog.askdirectory()
            name = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
            clip_color.write_videofile(folder+"/"+name+".mp4")
        except Exception as e:
            print(e)
        root.deiconify()
        tk.destroy()
    try:
        filePath = filedialog.askopenfilename(title='select', filetypes=[
            ("all video format", ".mp4"),
            ("all video format", ".flv"),
            ("all video format", ".avi"),
        ])
        clip = VideoFileClip(filePath)
        colorvalue = float(1)
        tk = Tk()
        tk.config(bg="#232323")
        tk.protocol("WM_DELETE_WINDOW", onClose)
        root.withdraw()
        scale = Scale(tk, variable=colorvalue, orient=HORIZONTAL, bg = "#232323", fg ="#ffffff", from_=0, to =1, resolution=0.05)
        scale.pack()
        button = Button(tk, text="Done", bg = "#232323", fg ="#ffffff",command=createVideo)
        button.pack()
        tk.mainloop()
        
    except:
        print("choose only videos")

# def trim():
#     starting = int(input("Enter starting : "))
#     ending = int(input("Enter Ending : "))
#     clip_trim = clip1.cutout(starting, ending)
#     clip_trim.write_videofile("Final render.mp4")

# def audio():
#     audioClip = AudioClip("audio.mp3")
#     final_clip = clip1.set_audio(audioClip)
#     final_clip.write_videofile("Final render.mp4")


root = Tk()
root.title("Video Editor by Sudip Mondal")
root.geometry("750x200")
root.minsize(750, 200)
root.maxsize(750, 200)
root.config(bg="#232323")

mixBut = Button(root, text="Mix", relief=GROOVE,
                bg="#232323", fg="white", command=mix)
mixBut.pack(side="left", padx=20)
mixBut.config(width=8, height=3)

mirrorBut = Button(root, text="Mirror", relief=GROOVE,
                   bg="#232323", fg="white", command=mirror)
mirrorBut.pack(side="left", padx=20)
mirrorBut.config(width=8, height=3)

# resizeBut = Button(root, text="Resize", relief = GROOVE, bg="#232323", fg="white", command=resize)
# resizeBut.pack(side="left",padx = 20)
# resizeBut.config(width=8, height=3)

# speedBut = Button(root, text="Speed", relief = GROOVE, bg="#232323", fg="white", command=speed)
# speedBut.pack(side="left",padx = 20)
# speedBut.config(width=8, height=3)

colorBut = Button(root, text="Color", relief=GROOVE,
                  bg="#232323", fg="white", command=color)
colorBut.pack(side="left", padx=20)
colorBut.config(width=8, height=3)

# trimBut = Button(root, text="Trim", relief = GROOVE, bg="#232323", fg="white", command=trim)
# trimBut.pack(side="left",padx = 20)
# trimBut.config(width=8, height=3)

# audioBut = Button(root, text="Audio", relief = GROOVE, bg="#232323", fg="white", command=audio)
# audioBut.pack(side="left",padx = 20)
# audioBut.config(width=8, height=3)

root.mainloop()
