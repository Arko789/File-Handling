[README.md](https://github.com/user-attachments/files/33233238/README.md)
<div align="center">

# 📁 Python File Handling

**A beginner-friendly collection of Python examples for working with text and binary files.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Topics](https://img.shields.io/badge/Topics-File%20I%2FO%20%7C%20Pickle-blueviolet)](#-what-youll-learn)
[![Status](https://img.shields.io/badge/Project-Learning%20 რესource-success)](#)

</div>

---

## 🧭 Contents

- [✨ What you'll learn](#-what-youll-learn)
- [🗂️ Project structure](#️-project-structure)
- [🚀 Getting started](#-getting-started)
- [▶️ Run an example](#️-run-an-example)
- [📝 Notes](#-notes)

## ✨ What you'll learn

| Area | Examples in this repository |
|---|---|
| 📝 **Text files** | Read file contents, write lines, display content, and copy selected lines to another file |
| 🔎 **Text processing** | Count character occurrences and filter lines based on their contents |
| 📦 **Binary files** | Read and write binary data using Python's `pickle` module |
| 📚 **Book records** | Store book details and practise reading book records |
| 🎓 **Student records** | Practise saving student information to a binary file |
| 🔁 **Revision** | Short read and write-lines exercises |

## 🗂️ Project structure

```text
File-Handling/
├── Binary/
│   ├── record input Book.py
│   ├── show all books.py
│   ├── show details of specific author Book.py
│   ├── read and write student.dat.py
│   └── show input.py
├── Text/
│   ├── open + read.py
│   ├── read content.py
│   ├── show lines.py
│   ├── write_lines newstuff.py
│   ├── copy to another file.py
│   └── no. of occurence.py
├── revision/
│   ├── 1read.py
│   └── 2writelines.py
├── new.txt
└── README.md
```

## 🚀 Getting started

**Requirements:** Python 3. No third-party packages are needed for the basic text-file examples; the binary-record examples use Python's built-in `pickle` module.

1. [Install Python](https://www.python.org/downloads/) if it isn't installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run one example at a time.

```bash
git clone https://github.com/Arko789/File-Handling.git
cd File-Handling
python "Text/read content.py"
```

## ▶️ Run an example

Choose a script and run it from the repository root. For example:

```bash
python "revision/1read.py"
python "revision/2writelines.py"
python "Text/write_lines newstuff.py"
python "Binary/record input Book.py"
```

Some scripts prompt for input and create or overwrite files such as `new.txt`, `newstuff.txt`, `Book.dat`, or `student.dat`.

## 📝 Notes

- **Run scripts individually.** These are practice exercises, not one combined application.
- **Check file paths before running.** A few scripts contain absolute Windows paths from the original development environment. Replace them with paths that work on your computer, or use relative paths.
- **Keep data files in the expected location.** Relative paths are resolved from the program's current working directory.
- **Be careful with write mode (`w`/`wb`).** It can overwrite an existing file.
- **Use `pickle` only with trusted data.** Never unpickle files from an untrusted source.

---

<div align="center">

Made for practising Python file handling, one example at a time. 🐍

</div>
