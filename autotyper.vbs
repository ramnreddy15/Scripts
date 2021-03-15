set wshshell = wscript.CreateObject("wscript.shell")
'wshshell.run "Notepad"
set shell = createobject("wscript.shell")
var2 = 1
var1 = inputbox("Type number")
strtimes = inputbox ("How many times would you like you type it?")
if not isnumeric(strtimes) then
	lol=msgbox("Please write a NUMBER nextime")
	wscript.quit
end if
msgbox "After you click ok the message will start in 5 seconds "
wscript.sleep(5000)
for var3=1 to strtimes
	for i=1 to 1
		var1 = var1 + var2
		shell.sendkeys(var1 &  "")
		Shell.SendKeys "{Enter}"
		'"+{Enter}"
		'wscript.sleep(150)
	next
	'Shell.SendKeys "{Enter}"
	wscript.sleep(250)
next

