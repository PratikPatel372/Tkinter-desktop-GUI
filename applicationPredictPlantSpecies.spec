# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/ABCD/Desktop/Tkinter/applicationPredictPlantSpecies.py'],
             pathex=['C:\\Users\\ABCD\\Desktop\\Tkinter'],
             binaries=[],
             datas=[('C:/Users/ABCD/Downloads/robot.jpg', '.'), ('E:/DELHI(sonipat)(TRAINING)/CLASSIFICATION OF PLANT SEEDLING/plant-seedlings/labels data.npy', '.'), ('E:/DELHI(sonipat)(TRAINING)/CLASSIFICATION OF PLANT SEEDLING/plant-seedlings/my_model.h5', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='applicationPredictPlantSpecies',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\ABCD\\Downloads\\agriculture.ico')
