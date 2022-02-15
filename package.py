import PyInstaller.__main__

paddle_path = 'D:\Anaconda\envs\GUIDemo\Lib\site-packages\paddle\\'
paddle_libs_path = f'{paddle_path}libs'

PyInstaller.__main__.run([
    'main.py',
    # '-w',
    '-F',
    '--noconfirm',
    '--clean',

    '--collect-submodules',
    'paddle.fluid.proto',

    '--add-data',
    '.\module;.\module',

    '--add-data',
    './img/blank.png;.',

    '--additional-hooks-dir',
    paddle_path,
    '--additional-hooks-dir',
    '.',
    '--log-level',
    'WARN',
])
