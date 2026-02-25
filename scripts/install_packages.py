import subprocess

# Define Homebrew taps, packages, and cask packages
homebrew_taps = [
    "heroku/brew",
    "homebrew/cask-fonts",
    "homebrew/core"
]

homebrew_packages = [
    "asdf",
    "bat",
    "broot",
    'bruno'
    "catimg",
    "coreutils",
    "curl",
    "diff-so-fancy",
    "exa",
    "git",
    "gpg",
    "grep",
    "htop",
    "imagemagick",
    "jpegoptim",
    "mailpit",
    "ncdu",
    "nmap",
    "ngrok",
    "nvm",
    "optipng",
    "pipx",
    "postgresql",
    "redis",
    "speedtest_cli",
    "stow",
    "stripe/stripe-cli/stripe",
    "the_silver_searcher",
    "tldr",
    "tmate",
    "tmux",
    "trash",
    "tree",
    "vim",
    "watch",
    "wget",
    "zsh",

]

homebrew_cask_packages = [
    "cursor",
    "cyberduck",
    "discord",
    "docker",
    "firefox",
    "font-fira-code",
    "ghostty",
    "gimp",
    "google-chrome",
    "inkscape",
    "iterm2",
    "kindle",
    "maccy",
    "ngrok",
    "notion",
    "postman",
    "slack",
    "spotify",
    "the-unarchiver",
    "visual-studio-code",
    "zoom",
    "whatsapp",
    "postgres-unofficial"
]

def run_command(command):
    """Run a shell command and continue on error."""
    try:
        print(f"Running command: {' '.join(command)}")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}\n{e}")

def install_homebrew():
    """Install Homebrew if not already installed."""
    try:
        subprocess.run(["brew", "--version"], check=True)
        print("Homebrew is already installed.")
    except subprocess.CalledProcessError:
        print("Homebrew is not installed. Installing Homebrew...")
        subprocess.run(
            '''/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"''',
            shell=True,
            check=True
        )

def tap_homebrew_repositories(taps):
    """Tap Homebrew repositories."""
    for tap in taps:
        run_command(["brew", "tap", tap])

def install_homebrew_packages(packages):
    """Install Homebrew packages."""
    for package in packages:
        run_command(["brew", "install", package])

def install_homebrew_cask_packages(cask_packages):
    """Install Homebrew cask packages."""
    for cask_package in cask_packages:
        run_command(["brew", "install", "--cask", cask_package])

def main():
    install_homebrew()
    tap_homebrew_repositories(homebrew_taps)
    install_homebrew_packages(homebrew_packages)
    install_homebrew_cask_packages(homebrew_cask_packages)
    print("All specified packages and cask applications have been installed.")

if __name__ == "__main__":
    main()
