import ttkbootstrap as ttk
from Application import Application


def clear(root, app: Application):
    app.clear()
    root.quit()


if __name__ == '__main__':
    root = ttk.Window(title='图片处理')

    app = Application(master=root)

    root.protocol('WM_DELETE_WINDOW', lambda: clear(root, app))

    root.mainloop()
