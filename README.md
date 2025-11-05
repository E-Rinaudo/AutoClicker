# AutoClicker

[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![ProtonMail][ProtonMail-shield]][ProtonMail-url]

**AutoClicker** is a small, cross-platform Python utility that automates repeated mouse clicks at the current cursor position. It's intended as a simple script and includes dialog so you can stop it when desired.

---

## Table of Contents

- [AutoClicker](#autoclicker)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Run the App](#run-the-app)
  - [Usage](#usage)
    - [Code Example](#code-example)
  - [License](#license)
  - [Contact](#contact)

---

## About

This project provides a minimal GUI to start an automated click loop, waits a short countdown to position the cursor, then clicks repeatedly until you stop it. It is useful for automated repetitive tasks.

[back to top](#autoclicker)

---

## Features

- Start/stop via a small confirmation dialog.
- Countdown before clicking begins so you can position the cursor.
- Periodic confirmation prompts so the script doesn't run unattended.
- Move the mouse to any screen corner to immediately abort.

[back to top](#autoclicker)

---

## Built With

- [![Python][Python-badge]][Python-url]
- [![Visual Studio Code][VSCode-badge]][VSCode-url]
- [![PyAutoGUI][PyAutoGui-badge]][PyAutoGUI-url]
- [![Mypy][Mypy-badge]][Mypy-url]
- [![Black][Black-badge]][Black-url]
- [![Docformatter][Docformatter-badge]][Docformatter-url]
- [![Pylint][Pylint-badge]][Pylint-url]
- [![Flake8][Flake8-badge]][Flake8-url]
- [![Ruff][Ruff-badge]][Ruff-url]
  
[back to top](#autoclicker)

---

## Getting Started

### Prerequisites

- [Python][Python-download]
- [Git][Git-download]

> Note:
>
> On Linux GUI automation behavior differs across display servers:
>
> - X11: PyAutoGUI works reliably.
> - Wayland: PyAutoGUI may not move the real cursor; consider running on X11.

### Setup

```bash
# Clone the repository
git clone https://github.com/E-Rinaudo/autoclicker.git # Using Git
gh repo clone E-Rinaudo/autoclicker # Using GitHub CLI

# Create a virtual environment
cd autoclicker
python -m venv venv

# Activate the virtual environment (all platforms)
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows
.\venv\Scripts\activate.bat # On Windows with CMD
.\venv\Scripts\activate.ps1 # On Windows with PowerShell
source venv/Scripts/activate # On Windows with Unix-like shells (e.g. Git Bash)

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
python autoclicker.py
```

Or use the provided shell script:

```bash
./run_clicker.sh
```

[back to top](#autoclicker)

---

## Usage

1. Start the program.
2. Click "OK" in the start dialog.
3. Move the mouse to the target location; a short countdown starts.
4. The program will begin clicking repeatedly at the current cursor position.
5. Every 10 seconds a dialog appears asking whether to continue or stop.
6. Move your mouse into any screen corner to trigger PyAutoGUI's failsafe and abort immediately.

### Code Example

An example from `autoclicker.py` showing the main workflow:

```py
auto_clicker = Clicker()

try:
    auto_clicker.start_clicker()
    auto_clicker.run_clicker()
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
    sys.exit(0)
```

[back to top](#autoclicker)

---

## License

Distributed under the MIT License. See [`LICENSE.txt`][license-url] for details.

[back to top](#autoclicker)

## Contact

If you have any questions, feedback, or just want to get in touch, feel free to reach out to me via email. Your feedback is appreciated as it helps me to continue improving.

- Email: <erinaudo.gh@w.ernode.com>  

You can also explore my GitHub profile.

- GitHub: [E-Rinaudo](https://github.com/E-Rinaudo)

[back to top](#autoclicker)

---

**Happy coding!**

<!-- SHIELDS -->
[stars-shield]: https://img.shields.io/github/stars/E-Rinaudo/thermo-tracker.svg?style=flat
[stars-url]: https://github.com/E-Rinaudo/thermo-tracker/stargazers
[license-shield]: https://img.shields.io/github/license/E-Rinaudo/thermo-tracker.svg?style=flat
[license-url]: https://github.com/E-Rinaudo/thermo-tracker/blob/main/LICENSE.txt
[ProtonMail-shield]: https://img.shields.io/badge/Proton%20Mail-6D4AFF?logo=protonmail&logoColor=fff
[ProtonMail-url]: erinaudo.gh@w.ernode.com

<!-- BADGES -->
[Python-badge]: https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=flat
[Python-url]: https://docs.python.org/3/
[VSCode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=flat
[VSCode-url]: https://code.visualstudio.com/docs
[PyAutoGUI-badge]: https://img.shields.io/badge/PyAutoGUI-**darkgreen**?logo=python&logoColor=ffdd54&style=flat
[PyAutoGUI-url]: https://autogui.readthedocs.io/en/latest/index.html
[Mypy-badge]: https://img.shields.io/badge/mypy-checked-blue?style=flat
[Mypy-url]: https://mypy.readthedocs.io/
[Black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[Black-url]: https://black.readthedocs.io/en/stable/
[Pylint-badge]: https://img.shields.io/badge/linting-pylint-yellowgreen?style=flat
[Pylint-url]: https://pylint.readthedocs.io/
[Ruff-badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[Ruff-url]: https://docs.astral.sh/ruff/tutorial/
[Flake8-badge]: https://img.shields.io/badge/linting-flake8-blue?style=flat
[Flake8-url]: https://flake8.pycqa.org/en/latest/
[Docformatter-badge]: https://img.shields.io/badge/formatter-docformatter-fedcba.svg
[Docformatter-url]: https://github.com/PyCQA/docformatter

<!-- PREREQUISITES LINKS -->
[Python-download]: https://www.python.org/downloads/
[Git-download]: https://git-scm.com
