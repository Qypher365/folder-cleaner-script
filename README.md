# 🧹 Folder Cleaner App

A simple and lightweight desktop application built with Python and Tkinter that organizes files in a selected directory by moving them into categorized subfolders — all in one click!

---

## 📦 Features

- Automatically categorizes files into the following directories:
  - **Documents** (.pdf, .txt, .docx, etc.)
  - **Images** (.jpg, .png, .gif, etc.)
  - **Videos** (.mp4, .mov, etc.)
  - **Audio** (.mp3, .wav, etc.)
  - **Archives** (.zip, .rar, etc.)
  - **Applications** (.exe, .msi, etc.)
  - **Code Files** (.py, .js, .html, etc.)
  - **Fonts, System Files, Torrents**, and more!
- Any unrecognized files are placed in an **Others** folder.
- Creates folders automatically directly inside an organized `Cleaned` folder.
- Follows Windows Explorer native style (using `pywinstyles`).

---

## 🛠 Requirements

- **Python 3.x**
- Windows OS (due to the Explorer window styling library, though the script logic is cross-platform).

Libraries used:
- `tkinter`, `os`, `shutil` (standard Python libraries)
- `pywinstyles` (for Windows native GUI styling)

---

## 🚀 Setup and Installation

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/Qypher365/folder-cleaner-script.git
   cd "Folder Cleaner Script"
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   ```bash
   python app.py
   ```

---

## 💡 How to Use

1. Launch the application.
2. Click the **"Browse..."** button and select the folder you want to clean up.
3. Click **"Clean"**.
4. The files will be organized into a `Cleaned` sub-directory within the selected folder. A popup will give you a summary of the total files moved!

---

## 📁 Folder Structure After Cleanup

All files will be sorted into a new subfolder called `Cleaned`, resulting in a structure like this:

```
YourDirectory/
└── Cleaned/
    ├── Applications/
    ├── Archives/
    ├── Audio/
    ├── Code/
    ├── Documents/
    ├── Fonts/
    ├── Images/
    ├── Others/
    ├── System Files/
    ├── Torrents/
    └── Videos/
```

---

## 🧑‍💻 Author

Made by Qypher365
