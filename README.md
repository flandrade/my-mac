# Python Scripts for macOS Setup

[![Build Status](https://github.com/flandrade/my-mac/workflows/build/badge.svg)](https://github.com/flandrade/my-mac/actions)

This repository contains Python scripts for setting up and configuring macOS systems. These scripts simplify the process of installing and configuring various components of a macOS development environment.

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

Run the scripts:

```
python install_packages.py
python dotfiles.py
python shell.py
setup.sh
```

To configure the terminal:

```
zsh
python shell.py
```

## 📌 Requirements

Ensure Python is installed on your macOS system. You can use [asdf](https://asdf-vm.com/#/core-manage-asdf-vm) to manage your Python installations.

## 🕹️ Credits and Inspiration

The idea for creating these Python scripts was inspired by various repositories and projects aimed at automating macOS setup and configuration.

- [Sebastián Estrella's devbox](https://github.com/sestrella/devbox)
- [Jeff Geerling’s mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook)
- [Adam Johnson's mac-ansible](https://github.com/adamchainz/mac-ansible)
- [Steven Loria's dotfiles](https://github.com/sloria/dotfiles)
- [Matiss Treinis's dots](https://github.com/Addvilz/dots)
- [Original OSX script by Mathias Bynens](https://github.com/mathiasbynens/dotfiles)
