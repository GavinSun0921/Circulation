import PyInstaller.__main__

paddle_path = 'D:\Anaconda\envs\GUIDemo\Lib\site-packages\paddle\\'
paddle_libs_path = f'{paddle_path}libs'

PyInstaller.__main__.run([
    'Circulation.py',
    '-D',
    '--noconfirm',
    '--clean',

    '--collect-submodules',
    'paddle.fluid.proto',

    '--add-data',
    '.\\img\\blank.png;.\\img',
    '--add-data',
    '.\\module\\*;.\\module',

    '--exclude-module',
    'matplotlib',

    '--exclude-module',
    'pandas',

'--exclude-module',
    'sklearn',

    '--additional-hooks-dir',
    '.',
    '--log-level',
    'WARN',
])

