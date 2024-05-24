import subprocess
import os

DOTFILES_DIR = os.path.expanduser("~/dotfiles")

def fetch_dotfiles():
    if not os.path.exists(DOTFILES_DIR):
        print("Fetching dotfiles from GitHub...")
        subprocess.run(["git", "clone", "https://github.com/flandrade/dotfiles", DOTFILES_DIR])
    else:
        print("Dotfiles directory already exists. Skipping fetch.")

def install_dotfiles():
    print("Installing dotfiles...")
    packages = [d for d in os.listdir(DOTFILES_DIR) if os.path.isdir(os.path.join(DOTFILES_DIR, d))]
    for package in packages:
        package_dir = os.path.join(DOTFILES_DIR, package)
        if not os.path.exists(package_dir):
            continue
        installed_packages = subprocess.run(["stow", "--list", package], capture_output=True, text=True).stdout.split('\n')
        if not any(f"stow: {package}" in output for output in installed_packages):
            print(f"Installing {package}...")
            subprocess.run(["stow", package], cwd=DOTFILES_DIR)
        else:
            print(f"{package} is already installed. Skipping.")

def main():
    fetch_dotfiles()
    install_dotfiles()
    print("Dotfiles installation completed!")

if __name__ == "__main__":
    main()
