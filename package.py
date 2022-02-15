import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '-w',
    '-F',
    '--noconfirm',
    '--clean',
    '-p',
    'D:\Anaconda\envs\GUIDemo\Lib\site-packages\paddle\libs',
    '--add-binary',
    'D:\Anaconda\envs\GUIDemo\Lib\site-packages\paddle\libs;.',
    '--add-data',
    '.\module;.\module',
    '--additional-hooks-dir',
    '.'
])
