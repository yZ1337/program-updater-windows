import os
import importlib

__author__ = "(c) oVeXz 2023"

# Input field
def main():
    os.system('cls')
    print("----------------------------------")
    print('{:^30s}'.format("Simple Windows Python Tool 1.4.1"))
    print('{:^30s}'.format("Made by: yZ"))
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
    if resultInput == "1":
        checkUpdatesPackages()

    elif resultInput == "2":
        upgradePackages()

    # Exits after 'exit' argument given
    elif resultInput == "exit":
        raise(exit)

    else:
        main()

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
            main()
        else:
            raise SystemExit
    elif updateYesNo.strip() == "n":
        main()
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
        main()
    else:
        raise SystemExit


if __name__ == "__main__":
        main() 
