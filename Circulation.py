from src.Application import Application
import ttkbootstrap as ttk


def clear(_root, _app: Application):
    _app.clear()
    _root.quit()


if __name__ == '__main__':
    root = ttk.Window(title='图片处理')
    root.place_window_center()

    app = Application(master=root)

    root.protocol('WM_DELETE_WINDOW', lambda: clear(root, app))

    root.mainloop()
