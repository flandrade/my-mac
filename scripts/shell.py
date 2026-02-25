import subprocess
import os

ZDOTDIR = os.getenv("ZDOTDIR", os.path.expanduser("~"))

def clone_repository():
    print("Cloning Prezto repository...")
    subprocess.run(["git", "clone", "--recursive", "https://github.com/sorin-ionescu/prezto.git", f"{ZDOTDIR}/.zprezto"])

def install_fzf_tab():
    print("Installing fzf-tab plugin...")
    zpreztodir = f"{ZDOTDIR}/.zprezto"
    fzf_tab_path = f"{zpreztodir}/contrib/fzf-tab"

    if not os.path.exists(fzf_tab_path):
        subprocess.run(["git", "clone", "https://github.com/Aloxaf/fzf-tab", fzf_tab_path])
    else:
        print("fzf-tab already installed. Skipping.")

def create_zsh_configuration():
    print("Creating Zsh configuration...")
    if not os.path.exists(f"{ZDOTDIR}/.zprezto/runcoms"):
        print("Prezto runcoms directory not found. Exiting.")
        return

    rcfiles = subprocess.run(["find", f"{ZDOTDIR}/.zprezto/runcoms", "-maxdepth", "1", "-type", "f", "-name", "^[^.]*", "-exec", "basename", "{}", "+"], capture_output=True, text=True).stdout.split('\n')
    for rcfile in rcfiles:
        symlink_path = f"{ZDOTDIR}/.{os.path.basename(rcfile)}"
        if not os.path.exists(symlink_path):
            subprocess.run(["ln", "-s", f"{ZDOTDIR}/.zprezto/runcoms/{rcfile}", symlink_path])
        else:
            print(f"Symlink for {rcfile} already exists. Skipping.")

def set_default_shell():
    print("Setting Zsh as default shell...")
    current_shell = subprocess.run(["dscl", ".", "-read", "/Users/$(whoami)", "UserShell"], capture_output=True, text=True).stdout.strip()
    if current_shell != "/bin/zsh":
        subprocess.run(["chsh", "-s", "/bin/zsh"])
    else:
        print("Zsh is already the default shell. Skipping.")

def main():
    clone_repository()
    install_fzf_tab()
    create_zsh_configuration()
    set_default_shell()
    print("Prezto installation completed!")

if __name__ == "__main__":
    main()
