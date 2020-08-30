<img
  src="https://raw.githubusercontent.com/flandrade/my-mac/master/media/ansible-256.png?token=ABTZYEODR7AZUVHRN5JN4US7KVV44"
  width="256px"
  alt="Ansible logo"
  title="Ansible logo"
  align="right"
/>

# My macOS setup with Ansible Playbooks

This repository contains a few Ansible playbooks to setup, configure, and maintain
my Mac. This sets up a full local development environment with a single command.
It takes most of the effort out of installing and configuring everything manually.

Everything needed to use and customize these playbooks is all documented here.
Feel free to explore, adapt, or copy code for your playbook!

Star me on GitHub — thanks! ⭐

## ⚠️ Enter, stranger, but take heed ⚠️

If you want to give this a try, you should first fork or clone this repository,
review, and remove the setting you don’t want or need from the code.

**You should not apply this configuration on your own Mac** because it can break
or replace your settings. Use it at your own risk!

## 📖 What's in?

This Ansible role does four tasks. Here are the details:

- **App installations:** Command-line tools and applications installed with the
  fantastic [Ansible's Homebrew role] by Jeff Geerling. It installs and
  configures packages, taps, and cask apps according to [supplied variables].

- **zsh installation:** This role configures [zsh] and installs the configuration
  framework [prezto]. Check out the [zsh role].

- **Dotfile configuration:** This playbook downloads dotfiles from my
  [dotfile repository] and it symlinking them with [Stow]. You can replace
  the repository and use your own but make sure you're using [Stow]. This
  playbook also installs and configures [vscode], you can change the extensions
  by modifying the [supplied variables]. Check out the [dotfiles role].

- **OSX configuration:** This small playbook runs a script to modify the default
  macOS preferences. Go through the [.macos file] and adjust the settings to your
  preferences. You can find more settings at the [original script] by Mathias
  Bynens. Check out the [osx role].

In summary, you can override most of my settings by modifying the
[supplied variables] in `group_vars/local/main.yml`.

## 📌 Requirements

Ensure Apple's command-line tools are installed:

```
xcode-select --install
```

Install [asdf] and [asdf-python] to build and install Python.


## 🚀 Get Started

Clone this repository to your local drive:

```
git clone git@github.com:flandrade/my-mac.git
cd my-mac
```

Install Python with asdf:

```
asdf install
```

Create a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```
pip install -r requirements.txt
```

Install Ansible Galaxy requirements to install required Ansible roles:

```
$ ansible-galaxy install -r requirements.yml
```

Run the main playbook and enter your account password when prompted:

```
ansible-playbook main.yml -K
```

## 🔍 Running a Specific Playbook

You can filter which part of the provisioning process to run by specifying a playbook.
These can be `applications.yml`, `dotfiles.yml`, `osx.yml`, and `shell.yml`.

```
ansible-playbook playbooks/osx.yml
```

## 🔨 Things That Still Need to Be Done Manually

This playbook takes most of the effort out of installing and configuring
everything, but there are a few steps that still need to be done manually.

- **Get the environment ready to run Ansible:** This requires installing Homebrew,
  using Homebrew to install asdf, cloning the repository, and using asdf to
  install Ansible.

- **Configure applications:** It requires configuring personal accounts, but also
  changing app settings like iTerm.

## 🕹️ Credits and Inspiration

I first got the idea of starting this project from
[Sebastián Estrella's devbox repo](https://github.com/sestrella/devbox). You can
learn a lot by looking at how other people set up their development environment.
If you want to get started and create your Ansible roles, check out these GitHub
repositories for more inspiration:

- [Jeff Geerling’s repo](https://github.com/geerlingguy/mac-dev-playbook)
- [Adam Johnson's repo](https://github.com/adamchainz/mac-ansible)
- [Steven Loria's dotfiles](https://github.com/sloria/dotfiles)
- [Matiss Treinis's repo](https://github.com/Addvilz/dots)
- OSX [original script] by Mathias Bynens

[asdf]: https://asdf-vm.com/#/core-manage-asdf-vm
[asdf-python]: https://github.com/danhper/asdf-python
[Ansible's Homebrew role]: https://galaxy.ansible.com/geerlingguy/homebrew
[zsh]: https://github.com/sorin-ionescu/prezto
[prezto]: https://github.com/sorin-ionescu/prezto
[Stow]: https://www.gnu.org/software/stow/
[dotfile repository]: https://github.com/flandrade/dotfiles
[original script]: https://github.com/mathiasbynens/dotfiles
[vscode]: https://code.visualstudio.com/

[supplied variables]: https://github.com/flandrade/my-mac/blob/master/group_vars/local/main.yml
[.macos file]: https://github.com/flandrade/my-mac/tree/master/roles/osx/files/setup.sh
[dotfiles role]: https://github.com/flandrade/my-mac/tree/master/roles/dotfiles
[osx role]: https://github.com/flandrade/my-mac/tree/master/roles/osx
[zsh role]: https://github.com/flandrade/my-mac/tree/master/roles/zsh
