# Challange Info

Name : Cat
Difficulty : Easy
Link : https://app.hackthebox.com/challenges/Cat

# Writeup

The challange includes a cat.ab file.
In order to obtain info on type of file I used file command.

file cat.ab

> cat.ab: Android Backup, version 5, Compressed, Not-Encrypted

After searching around I found out how to restore these backup files.

adb restore cat.ab

But this dosen't help much as it's hard to investigate changes made on android emulator after restoring backup so I searched further and found a github repo with a tool to convert android backup file to tar archive.

Tool link : https://github.com/nelenkov/android-backup-extractor

./abe.jar unpack cat.ab cat.tar

tar -xvf cat.tar

This gets all the files stored in the backup.
As usually the flags are stored in flag.txt file i tried using find for any file named flag.

find ./ flag

> find: ‘flag’: No such file or directory

This didn't work so to find any interesting files i used ls with recursive argument.

ls -R

The files which caught my eye were :-

./shared/0/Pictures:
IMAG0001.jpg  IMAG0002.jpg  IMAG0003.jpg  IMAG0004.jpg  IMAG0005.jpg  IMAG0006.jpg

In IMAG0004.jpg image the guy in the picture is holding some paper titled "TOP SECRET".
If you zoom in the picture in the end of the paper the flag was there.
