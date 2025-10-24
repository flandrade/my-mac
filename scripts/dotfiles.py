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

def install_cursor_settings():
    print("Installing Cursor settings...")
    cursor_settings_src = os.path.join(DOTFILES_DIR, "cursor", "cursor-settings.json")
    cursor_settings_dst = os.path.expanduser("~/Library/Application Support/Cursor/User/settings.json")

    # Create the destination directory if it doesn't exist
    cursor_user_dir = os.path.dirname(cursor_settings_dst)
    os.makedirs(cursor_user_dir, exist_ok=True)

    if os.path.exists(cursor_settings_src):
        # Remove existing file/symlink if it exists
        if os.path.exists(cursor_settings_dst) or os.path.islink(cursor_settings_dst):
            os.remove(cursor_settings_dst)

        # Create the symlink
        os.symlink(cursor_settings_src, cursor_settings_dst)
        print("Cursor settings symlink created successfully!")
    else:
        print(f"Warning: Cursor settings file not found at {cursor_settings_src}")

def install_ghostty_config():
    print("Installing Ghostty config...")
    ghostty_config_src = os.path.join(DOTFILES_DIR, "ghostty", "ghostty-config")
    ghostty_config_dst = os.path.expanduser("~/Library/Application Support/com.mitchellh.ghostty/config")

    # Create the destination directory if it doesn't exist
    ghostty_user_dir = os.path.dirname(ghostty_config_dst)
    os.makedirs(ghostty_user_dir, exist_ok=True)

    if os.path.exists(ghostty_config_src):
        # Remove existing file/symlink if it exists
        if os.path.exists(ghostty_config_dst) or os.path.islink(ghostty_config_dst):
            os.remove(ghostty_config_dst)

        # Create the symlink
        os.symlink(ghostty_config_src, ghostty_config_dst)
        print("Ghostty config symlink created successfully!")
    else:
        print(f"Warning: Ghostty config file not found at {ghostty_config_src}")

def main():
    fetch_dotfiles()
    install_dotfiles()
    install_cursor_settings()
    install_ghostty_config()
    print("Dotfiles installation completed!")

if __name__ == "__main__":
    main()
