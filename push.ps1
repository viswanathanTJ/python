$date = Get-Date -Format "MM/dd/yyyy HH:mm:ss"
cd "B:\Notepad\CLOUD\notepad"
git add .
git commit -m $date
git push -u origin master
