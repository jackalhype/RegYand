import os

def Config():
    if os.name == 'nt':
        geckodriver = 'geckodriver.exe'
        firefox_binary = 'C:\\Users\\SPARK PC\\AppData\\Local\\Mozilla Firefox\\firefox.exe'
    else:
        geckodriver = '/usr/local/bin/geckodriver'
        firefox_binary = 'firefox'
    cfg = {
        'geckodriver': geckodriver,
        'firefox_binary': firefox_binary,
    }
    return cfg