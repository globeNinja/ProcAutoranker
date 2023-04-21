# ProcAutoranker
sets microsoft flight sim to high priority in windows or linux

If you use windows, you're going to need to run pip install win32api in order to access the windows specific functions.
Linux users should be able to run this off the bat(though untested because I only use windows).

Use task scheduler to run this python file on startup. (also requires python to be installed)

Here's how to hide the command prompt from the task scheduler
https://pureinfotech.com/prevent-command-window-appearing-scheduled-tasks-windows-10/#:~:text=Right%2Dclick%20the%20Task%20Scheduler,Click%20the%20Create%20Task%20option.&text=In%20the%20%E2%80%9CGeneral%E2%80%9D%20tab%2C,when%20the%20task%20runs%20automatically.)
