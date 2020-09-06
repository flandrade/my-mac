<img
  src="https://raw.githubusercontent.com/flandrade/my-mac/master/media/ansible-256.png?token=ABTZYEODR7AZUVHRN5JN4US7KVV44"
  width="256px"
  alt="Ansible logo"
  title="Ansible logo"
  align="right"
/>

# My MacOS Setup with Ansible

[![Build Status](https://github.com/flandrade/my-mac/workflows/build/badge.svg)](https://github.com/flandrade/my-mac/actions)

This repository contains Ansible playbooks to setup, configure, and maintain
my Mac. They set up a full local development environment with a single command.
As a result, they take most of the effort out of installing and configuring
everything manually.

Everything needed to use and customize these playbooks is documented here. Feel
free to explore, adapt, or copy code for your playbook!

## ⚠️ Enter, stranger, but take heed ⚠️

If you want to give this a try, you should first fork or clone this repository
to review and remove the settings you don’t need.

**You should not apply this configuration on your Mac** because it can break
or replace your settings. Use it at your own risk!

## 📖 What's in?

These Ansible playbooks do four tasks. Here are the details:

- **App installations:** Command-line tools and applications installed with the
  fantastic [Ansible's Homebrew role] by Jeff Geerling. It installs and
  configures packages, taps, and cask apps according to [supplied variables].

- **zsh installation:** The [zsh role] configures [zsh] and installs the
  configuration framework [prezto].

- **Dotfile configuration:** This role downloads the dotfiles from my
  [dotfile repository] and it symlinks them with [Stow]. It's possible to
  replace this repository and use your own but make sure you're using [Stow].
  In addition, this role also configures [vscode]: you can change the
  installed extensions by modifying the [supplied variables]. Check out the
  [dotfiles role] for more details.

- **OSX configuration:** The [osx role] runs a script to modify the default
  macOS preferences. Go through the [.macos file] and adjust the settings to
  your preferences. You can find more settings at the [original script] by
  Mathias Bynens.

In summary, you can override most of my settings by modifying the [supplied variables]
in `group_vars/local/main.yml`.

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

You can filter which part of the provisioning process to run by specifying a
playbook:

- `applications.yml`: installs packages, taps, and cask with Homebrew.
- `dotfiles.yml`: configures the applications dotfiles.
- `osx.yml`: runs a script to modify the default macOS preferences.
- `shell.yml`: configures zsh and installs prezto.

For example:

```
ansible-playbook playbooks/osx.yml
```

## 🔨 Things That Still Need to Be Done Manually

This playbook takes most of the effort out of installing and configuring
everything, but there are a few steps that still need to be done manually.

- **Get the environment ready to run Ansible:** This step requires installing
  Homebrew, using Homebrew to install asdf, cloning the repository, and using
  asdf to install Ansible.

- **Configure applications:** This requires configuring personal accounts, but
  also changing app settings like iTerm.

## 🕹️ Credits and Inspiration

I first got the idea of starting this project from
[Sebastián Estrella's repo](https://github.com/sestrella/devbox). It's clear
that we can learn a lot by looking at how other people set up their development
environment. If you want to get started and create your Ansible roles, check
out these GitHub repositories for more inspiration:

- [Jeff Geerling’s repo](https://github.com/geerlingguy/mac-dev-playbook)
- [Adam Johnson's repo](https://github.com/adamchainz/mac-ansible)
- [Steven Loria's dotfiles](https://github.com/sloria/dotfiles)
- [Matiss Treinis's repo](https://github.com/Addvilz/dots)
- OSX [original script] by Mathias Bynens

[asdf]: https://asdf-vm.com/#/core-manage-asdf-vm
[asdf-python]: https://github.com/danhper/asdf-python
[ansible's homebrew role]: https://galaxy.ansible.com/geerlingguy/homebrew
[zsh]: https://github.com/sorin-ionescu/prezto
[prezto]: https://github.com/sorin-ionescu/prezto
[stow]: https://www.gnu.org/software/stow/
[dotfile repository]: https://github.com/flandrade/dotfiles
[original script]: https://github.com/mathiasbynens/dotfiles
[vscode]: https://code.visualstudio.com/
[supplied variables]: https://github.com/flandrade/my-mac/blob/master/group_vars/local/main.yml
[.macos file]: https://github.com/flandrade/my-mac/tree/master/roles/osx/files/setup.sh
[dotfiles role]: https://github.com/flandrade/my-mac/tree/master/roles/dotfiles
[osx role]: https://github.com/flandrade/my-mac/tree/master/roles/osx
[zsh role]: https://github.com/flandrade/my-mac/tree/master/roles/zsh
