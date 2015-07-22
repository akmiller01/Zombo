# -*- mode: python -*-

block_cipher = None


a = Analysis(['zombo.py'],
             pathex=['Z:\\home\\alex\\git\\zombo'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
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
