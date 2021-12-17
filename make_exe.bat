rmdir /s /q __pycache__
del loguru_helper.exe
pyinstaller -F -w loguru_helper.py
move dist\loguru_helper.exe loguru_helper.exe
del loguru_helper.spec
rmdir /s /q __pycache__
rmdir /s /q build
rmdir /s /q dist
rem pause()