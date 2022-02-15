import PyInstaller.__main__

paddle_path = 'D:\Anaconda\envs\GUIDemo\Lib\site-packages\paddle'
paddle_libs_path = f'{paddle_path}\libs'

PyInstaller.__main__.run([
    'main.py',
    '-w',
    '-F',
    '--noconfirm',
    '--clean',
    '-p',
    paddle_libs_path,
    '--add-binary',
    f'{paddle_libs_path};.',
    '--add-data',
    f'{paddle_path};{paddle_path}\fluid\proto',
    '--add-data',
    '.\module;.\module',
    '--additional-hooks-dir',
    '.',
    '--log-level',
    'WARN',
])
