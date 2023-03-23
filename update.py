import os

__author__ = "(c) oVeXz 2023"

print("----------------------------------")
print('{:^30s}'.format("Updater 1.1"))
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

# Input field
os.system('color a')
print("Enter option number: ")
resultInput = input("Type: ")


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


if resultInput.strip() == "1":
    checkUpdatesPackages()

elif resultInput.strip() == "2":
    upgradePackages()

# Exits after 'exit' argument given
elif resultInput.strip() == "exit":
    raise SystemExit

# Restarts script if invalid argument given
else:
    print("Not valid option")
    os.startfile("update.py")