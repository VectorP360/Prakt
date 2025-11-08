from time import sleep
import webbrowser
import os

class ScadaOpener:

    def open_in_browser(self, svg_code):

        my_file = open("TempFile", "w")
        my_file.write(svg_code)
        my_file.close()

        os.rename('TempFile', 'TempFile.svg')
        filepath = os.path.abspath('TempFile.svg')

        #sleep тут нужен что бы компьютер успел загрузить схему через браузер, иначе временный файл будет удалён до его открытия

        sleep(1)
        webbrowser.open(f'File://{filepath}')
        sleep(2)
        os.unlink('TempFile.svg')