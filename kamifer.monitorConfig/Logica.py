from PyQt5 import QtCore
import subprocess
import os

class Logica:

    def detectar_monitores(self):
        output = [l for l in subprocess.check_output(["xrandr"]).decode("utf-8").splitlines()]
        return  [l.split()[0] for l in output if " connected " in l]

    def cmdline(self, command):
        process = subprocess.Popen(
            args=command,
            stdout= subprocess.PIPE,
            shell=True
        )
        return process.communicate()[0]

    def get_actual_brightness(self):
        brillos = [l.replace("\tBrightness: ", "") for l in self.cmdline("xrandr --verbose | grep -i brightness").decode("utf-8").splitlines()]
        monitores = self.detectar_monitores()

        print (monitores)
        print(brillos)

        myMonitors = dict()
        indice = 0
        for monitor in monitores:
            print(monitor)
            if(len(brillos) > indice):
                myMonitors[monitor] = brillos[indice]
            indice = indice + 1

        return myMonitors


