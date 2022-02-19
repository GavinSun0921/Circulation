# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = []
hiddenimports += collect_submodules('paddle.fluid.proto')


block_cipher = None


a = Analysis(['Circulation.py'],
             pathex=[],
             binaries=[],
             datas=[('.\\img\\blank.png', '.\\img'), ('.\\module', '.\\module')],
             hiddenimports=hiddenimports,
             hookspath=['.'],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['matplotlib', 'pandas'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Circulation',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Circulation')
