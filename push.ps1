$date = Get-Date -Format "MM/dd/yyyy HH:mm:ss"
cd "B:\Notepad\CLOUD\notepad"
git commit -a -m $date
git push -u origin master
