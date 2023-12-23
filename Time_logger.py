import time


class TerminalPrinter():

    def write(self,message):
        print(f'{message}')

class FilePrinter():
    def write(self,message):
        with open('log.txt','a+', encoding='UTF-8') as file:
            file.write(f'{message}')
class Logger:


    def __init__(self):
        self.prefix = time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
    def log_terminal(self,message):
        TerminalPrinter().write(f'{self.prefix} --> {message}')

    def log_file(self,message):
        FilePrinter().write(f'{self.prefix} --> {message}')

    def log(self,message,object_class):
        object_class().write(f'{self.prefix} --> {message}')

logger = Logger()
logger.log('Hello world', FilePrinter)
logger.log('Hello World',TerminalPrinter)