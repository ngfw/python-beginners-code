# Python Setup Guide

This guide will help you install Python on your computer so you can run the code examples from "Learn Python Fast: From Zero to Coding Hero".

---

## ✅ Check if Python is Already Installed

Before installing, check if Python is already on your system:

### macOS / Linux
Open Terminal and run:
```bash
python3 --version
```

### Windows
Open Command Prompt and run:
```bash
python --version
```

**If you see `Python 3.8.x` or higher**, you're ready to go! Skip to [Verify Installation](#verify-installation).

**If you see an error** or a version lower than 3.8, continue with the installation steps below.

---

## 🐍 Installing Python

### Windows

#### Option 1: Download from Python.org (Recommended)

1. **Visit** [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Click** "Download Python 3.x.x" (latest version)
3. **Run** the installer
4. **⚠️ IMPORTANT**: Check ☑️ "Add Python to PATH"
5. **Click** "Install Now"
6. **Wait** for installation to complete
7. **Restart** your computer

#### Option 2: Microsoft Store

1. Open **Microsoft Store**
2. Search for **"Python 3.11"** (or latest version)
3. Click **"Get"** to install
4. Wait for installation

#### Verify Windows Installation
Open Command Prompt and run:
```bash
python --version
pip --version
```

### macOS

#### Option 1: Official Installer (Recommended for Beginners)

1. **Visit** [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Click** "Download Python 3.x.x" (latest version)
3. **Open** the downloaded `.pkg` file
4. **Follow** the installation wizard
5. **Click** "Install" when prompted

#### Option 2: Homebrew (For Advanced Users)

If you have Homebrew installed:
```bash
brew install python3
```

#### Verify macOS Installation
Open Terminal and run:
```bash
python3 --version
pip3 --version
```

### Linux (Ubuntu/Debian)

Python 3 usually comes pre-installed. If not:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Verify Linux Installation
```bash
python3 --version
pip3 --version
```

### Linux (Fedora/RHEL)

```bash
sudo dnf install python3 python3-pip
```

---

## ✅ Verify Installation

After installing, verify Python works correctly:

### Test Python Interactive Mode

**Windows:**
```bash
python
```

**macOS/Linux:**
```bash
python3
```

You should see:
```
Python 3.x.x ...
>>>
```

Type this and press Enter:
```python
>>> print("Hello, Python!")
```

You should see:
```
Hello, Python!
```

Type `exit()` to quit.

### Run Your First Script

1. **Create** a file called `test.py` with this content:
```python
print("Python is working!")
print("Python version:", __import__('sys').version)
```

2. **Run** the file:

**Windows:**
```bash
python test.py
```

**macOS/Linux:**
```bash
python3 test.py
```

You should see:
```
Python is working!
Python version: 3.x.x ...
```

---

## 🛠️ Setting Up a Code Editor

You'll need a text editor or IDE (Integrated Development Environment) to write Python code.

### Beginner-Friendly Options

#### 1. **VS Code** (Recommended)
- **Download**: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- **Why**: Free, powerful, beginner-friendly
- **After installing**:
  - Open VS Code
  - Click Extensions (left sidebar)
  - Search "Python"
  - Install the official Python extension by Microsoft

#### 2. **IDLE** (Comes with Python)
- **Already installed** with Python
- **How to open**:
  - **Windows**: Start Menu → IDLE
  - **macOS**: Applications → Python 3.x → IDLE
  - **Linux**: Run `idle3` in terminal
- **Why**: Simple, no setup needed

#### 3. **PyCharm Community Edition**
- **Download**: [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
- **Why**: Professional IDE, great for learning
- **Note**: Bigger download, more features

### Other Options
- **Sublime Text**: Lightweight, fast
- **Atom**: Customizable, open-source
- **Jupyter Notebook**: Great for data science

---

## 📚 Running Code from This Repository

Once Python is installed:

### 1. Navigate to Chapter Directory
```bash
cd path/to/python-for-beginners-code/chapter-01/examples
```

### 2. Run an Example

**Windows:**
```bash
python 01-hello-world.py
```

**macOS/Linux:**
```bash
python3 01-hello-world.py
```

### 3. Run Exercises

```bash
cd ../exercises
python exercise-01.py    # Windows
python3 exercise-01.py   # macOS/Linux
```

---

## 🚨 Common Installation Issues

### Issue: "Python is not recognized"

**Windows:**
- Python wasn't added to PATH during installation
- **Fix**: Reinstall Python and check ☑️ "Add Python to PATH"
- **Or manually add**: Search "Environment Variables" → Edit PATH → Add Python directory

**macOS/Linux:**
- Use `python3` instead of `python`
- Add alias: `echo "alias python=python3" >> ~/.bashrc`

### Issue: "Permission denied"

**macOS/Linux:**
- Use `python3` instead of `python`
- Or try: `chmod +x filename.py` then `./filename.py`

### Issue: "pip is not recognized"

**All Systems:**
```bash
python -m pip --version    # Windows
python3 -m pip --version   # macOS/Linux
```

If that works, use `python -m pip install` instead of `pip install`

### Issue: Multiple Python Versions

**Check all versions:**
```bash
python --version
python3 --version
python3.11 --version
```

**Use the specific version you want:**
```bash
python3.11 your_script.py
```

---

## 🎓 Next Steps

Once Python is installed:

1. ✅ Run `python3 --version` to verify
2. ✅ Test with the hello world example from chapter-01
3. ✅ Install a code editor (VS Code recommended)
4. ✅ Start Chapter 1 of "Learn Python Fast"!

---

## 💡 Tips for Success

- **Use a virtual environment** for larger projects (covered in the book)
- **Keep Python updated** - Check for updates quarterly
- **Install pip packages** as needed: `pip install package-name`
- **Use Python 3.8+** - This book requires Python 3.8 or higher

---

## 📬 Need Help?

If you're still having trouble:

1. Check the [Issues](https://github.com/yourusername/python-for-beginners-code/issues) on GitHub
2. Search on [StackOverflow](https://stackoverflow.com/questions/tagged/python)
3. Email: nick@gm-sunshine.com

---

**Ready to code?** Return to the [main README](README.md) and start Chapter 1!
