import_links_into_Evernote
==========================

A way to mass import urls into evernote
I wrote a program that imports a test file wiht html links into evernote
It is a combination of python and applescript. Fill in the path  your textfile in the
main programm. It will then import from the first line till the end. If you get stuck
at e.g. line 100, then alter the start line and continue importing.

You can alter the notebook where you want your notes in the applescript part. The programm will hang if
the notebook doesn't exist. Be careful with the urls to import. I wouldn't import url with javascript in it.

The code is not completely foolproof. Every now and again evernote might crash. This is the
reason why I build in a while loop and provide the option to change the start line.

I have found a lot of this code online. Feel free to use and improve it.

Yours truly,

Henk
