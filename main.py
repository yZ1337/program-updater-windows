import os
import sys
import pyuac
import importlib

__author__ = "(c) oVeXz 2023"


def main():
    print('------ Checking for libraries ------')
    # Check for pyuac library
    try:
        importlib.import_module('pyuac')
        print('pyuac is already installed')
    except ImportError:
        print('pyuac is not installed. Installing now...')
        import subprocess
        subprocess.check_call(['pip', 'install', 'pyuac'])

    # Check for pypiwin32 library
    try:
        importlib.import_module('win32com.client')
        print('pypiwin32 is already installed')
        start()
    except ImportError:
        print('pypiwin32 is not installed. Installing now...')
        import subprocess
        subprocess.check_call(['pip', 'install', 'pypiwin32'])
        start()

# Input field
def start():
    os.system('cls')
    print("----------------------------------")
    print('{:^30s}'.format("Updater 1.3"))
    print('{:^30s}'.format("Made by: oVeXz"))
    print("----------------------------------")
    print()

    # Menu
    print('{:^30s}'.format("///// MENU /////"))
    print("-----")
    print("Check for upgradable packages [1]")
    print("Update all packages [2]")
    print("-----")
    print()
    os.system('color a')
    print("Enter option number: ")
    resultInput = input("Type: ")
    return resultInput

### CHECKS UPGRADABLE WINDOWS PACKAGES ###
def checkUpdatesPackages():
    os.system('cls')
    print('Getting upgradable applications...')
    os.system('color a')
    os.system('cmd /c "winget upgrade --include-unknown &"')
    print()
    os.system('cmd /c "color a & echo Done!"')
    print()
    print()
    print("If you want to update all packages type 'y'")
    print("If you want to go back type 'n'")
    updateYesNo = input("Type: ")
    if updateYesNo.strip() == "y":
        os.system('cls')
        os.system('cmd /c "winget upgrade --all &"')
        os.system('cls')
        os.system('color a')
        print("All packages up-to-date!")
        print()
        print("Go back? [y/n]")
        goBackYesNo = input("Type: ")
        if goBackYesNo.strip() == "y":
            os.startfile('update.py')
        else:
            raise SystemExit
    elif updateYesNo.strip() == "n":
        os.startfile('update.py')
    else:
        raise SystemExit


### UPGRADES ALL WINDOWS PACKAGES ###
def upgradePackages ():
    os.system('cls')
    os.system('color a')
    print("Updating all packages...")
    os.system('cmd /c "winget upgrade --all &"')
    os.system('cls')
    os.system('color a')
    print("All packages up-to-date!")
    print()
    goBackYesNo = input("Go back? [y/n]")
    if goBackYesNo.strip() == "y":
        os.startfile('update.py')
    else:
        raise SystemExit


if main() == "1":
    checkUpdatesPackages()

elif main() == "2":
    upgradePackages()

# Exits after 'exit' argument given
elif main() == "exit":
    raise SystemExit

# Restarts script if invalid argument given
else:
    print("Not valid option")
    os.startfile("update.py")


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()  # Already an admin here.