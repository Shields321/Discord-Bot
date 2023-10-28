import os
while(1):
    startApp = os.path.dirname(__file__)+"\\MelusineBot.py"

    with open(startApp) as f:

        exec(f.read())