import os
import tkinter
from tkinter import messagebox
from tkinter.colorchooser import askcolor

from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.filedialog as tkf

from humanseg import seg


class Application(ttk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master=master)
        self.pack()
        self.master = master

        self.color = tkinter.StringVar()
        self.image_final = None
        self.cachefilename = None
        self.filename = None
        self.outputdir = None

        self.__initLayout()

    def __initLayout(self):
        self.framePics = ttk.Labelframe(self, text='显示区')
        self.framePics.grid(row=0, column=0)
        self.framePics.configure(height=500)

        blank_img = Image.open('img/blank.png')
        blank_img = ImageTk.PhotoImage(blank_img)

        self.picOpenPreviewFrame = ttk.Labelframe(self.framePics, text='原图片', padding=10)
        self.picOpenPreviewFrame.grid(row=0, column=0, padx=10, pady=10)
        self.picOpenPreview = ttk.Label(self.picOpenPreviewFrame)
        self.picOpenPreview.pack()
        self.picOpenPreview.configure(image=blank_img)
        self.picOpenPreview.image = blank_img

        self.picOutputPreviewFrame = ttk.Labelframe(self.framePics, text='新图片', padding=10)
        self.picOutputPreviewFrame.grid(row=0, column=1, padx=10, pady=10)
        self.picOutputPreview = ttk.Label(self.picOutputPreviewFrame)
        self.picOutputPreview.pack()
        self.picOutputPreview.configure(image=blank_img)
        self.picOutputPreview.image = blank_img

        self.seg = ttk.Separator(self, orient=HORIZONTAL)
        self.seg.grid(row=1, column=0, pady=10)

        self.frameController = ttk.Labelframe(self, text='控制区')
        self.frameController.grid(row=1, column=0, padx=5, pady=5)

        self.leftFrame = ttk.Labelframe(self.frameController, text='执行')
        self.leftFrame.grid(row=0, column=0)

        self.middleFrame = ttk.Labelframe(self.frameController, text='选择颜色')
        self.middleFrame.grid(row=0, column=1, padx=22)

        self.rightFrame = ttk.Labelframe(self.frameController, text='导出')
        self.rightFrame.grid(row=0, column=2)

        btn_width = 8

        self.btnOpen = ttk.Button(self.leftFrame, text='选择图片', command=self.openFile)
        self.btnOpen.grid(row=0, column=0, padx=10, pady=10)
        self.btnOpen.configure(width=btn_width)
        self.btnRender = ttk.Button(self.leftFrame, text='转换底色', command=self.render)
        self.btnRender.grid(row=1, column=0, padx=10, pady=10)
        self.btnRender.configure(width=btn_width)

        self.colorChoose = ttk.Notebook(self.middleFrame)
        self.colorChoose.pack(expand=True, fill=BOTH)

        self.color1 = ttk.Frame(self.colorChoose)
        self.color.set('#CB061D')
        self.btn_red = ttk.Radiobutton(self.color1, text='红底', variable=self.color, value='#CB061D');
        self.btn_red.grid(row=0, column=0, padx=5, pady=25)
        self.btn_blue = ttk.Radiobutton(self.color1, text='蓝底', variable=self.color, value='#00A5F1');
        self.btn_blue.grid(row=0, column=1, padx=5, pady=25)

        self.color2 = ttk.Frame(self.colorChoose)
        self.btnChooseColor = ttk.Button(self.color2, text='选择颜色', command=self.chooseColor)
        self.btnChooseColor.pack(side=BOTTOM)

        self.colorChoose.add(self.color1, text='预设颜色')
        self.colorChoose.add(self.color2, text='自选颜色')

        self.btnExport_jpg = ttk.Button(self.rightFrame, text='JPG格式', command=self.export_jpg)
        self.btnExport_jpg.grid(row=0, column=0, padx=10, pady=10)
        self.btnExport_jpg.configure(width=btn_width)
        self.btnExport_png = ttk.Button(self.rightFrame, text='PNG格式', command=self.export_png)
        self.btnExport_png.grid(row=1, column=0, padx=10, pady=10)
        self.btnExport_png.configure(width=btn_width)

    def openFile(self):
        self.clear()
        buffer = tkf.askopenfilename()
        if buffer is not None and buffer != '':
            self.filename = buffer
        if self.filename is not None and self.filename != '':
            img = Image.open(self.filename)
            img = img.resize(size=(250, 350))
            img = ImageTk.PhotoImage(img)
            self.picOpenPreview.configure(image=img)
            self.picOpenPreview.image = img
            self.outputdir = seg(self.filename)

    def render(self):
        if self.outputdir is not None and self.outputdir != '':
            colorHEX = self.color.get()

            base_img = Image.open(self.outputdir)
            background = Image.new('RGBA', base_img.size, colorHEX)
            x, y = base_img.size
            background.paste(base_img, (0, 0, x, y), base_img)
            self.image_final = background
            self.cachefilename = f'{self.outputdir[:-3]}render.png'
            # print(self.outputFilename)
            self.image_final.save(self.cachefilename)

            resize_img = self.image_final.resize(size=(250, 350))
            img = ImageTk.PhotoImage(resize_img)
            self.picOutputPreview.configure(image=img)
            self.picOutputPreview.image = img

    def chooseColor(self):
        color_str = askcolor()
        self.color.set(str(color_str[1]))

    def export_jpg(self):
        if self.cachefilename is None or self.cachefilename == '':
            messagebox.showerror(message='还未转换图片')
        else:
            outputFilename = tkf.asksaveasfilename(initialdir=os.getcwd(), initialfile='未命名', defaultextension='.jpg',
                                                   title='Export As JPG',
                                                   filetypes=(('*.jpg', '*.jpeg'), ('All Files', '*.*')))
            if outputFilename is not None and outputFilename != '':
                jpg_image = self.image_final.convert('RGB')
                jpg_image.save(outputFilename)

    def export_png(self):
        if self.cachefilename is None or self.cachefilename == '':
            messagebox.showerror(message='还未转换图片')
        else:
            outputFilename = tkf.asksaveasfilename(initialdir=os.getcwd(), initialfile='未命名', defaultextension='.png',
                                                   title='Export As PNG',
                                                   filetypes=(('*.png', '*.png'), ('All Files', '*.*')))
            if outputFilename is not None and outputFilename != '':
                self.image_final.save(outputFilename)

    def clear(self):
        if self.outputdir is not None:
            os.remove(self.outputdir)
            self.outputdir = None

        if self.cachefilename is not None:
            os.remove(self.cachefilename)
            self.outputdir = None
