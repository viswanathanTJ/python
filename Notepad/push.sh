cd /mnt/SSD/Notepad/Notepad
git add .
git commit -m "$(date +"%D %T")"
GIT_SSH_COMMAND='ssh -i /mnt/SSD/Notepad/.ssh/id_ed25519 -o IdentitiesOnly=yes' git push -u origin master
echo "Script successful"
# -----BEGIN OPENSSH PRIVATE KEY-----
#b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
#QyNTUxOQAAACBFcCMqWZXQeoSKwC+AN5FE65xGLpC6UrmuiGa9abryOAAAAJiZxpQwmcaU
#MAAAAAtzc2gtZWQyNTUxOQAAACBFcCMqWZXQeoSKwC+AN5FE65xGLpC6UrmuiGa9abryOA
#AAAEADGVgK/LB8NlHTo26wlJHXVnuDE0uFyst7US76vOON6kVwIypZldB6hIrAL4A3kUTr
#nEYukLpSua6IZr1puvI4AAAAE3Zpc3dhMms1OUBnbWFpbC5jb20BAg==
#-----END OPENSSH PRIVATE KEY-----