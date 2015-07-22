# -*- mode: python -*-
a = Analysis(['zombo.py'],
             pathex=['C:\\git\\Zombo'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='zombo.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
