import os, sys, platform
print('\033[0;97m [√]\033[92m join whatsapp group')
os.system('xdg-open https://chat.whatsapp.com/GrzDGbFBOTt6gf7OmBUoWe')
os.system('clear')
print('\033[0;97m [√] \033[92mchecking for update')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
    print(system supported)
    import test
elif bit == '32bit':
    print("\033[1;90m [\033[1;91m system not supported \033[1;90m]");exit()
