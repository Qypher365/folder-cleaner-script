import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import pywinstyles

folders = ['Documents', 'Images', 'Videos', 'Audio', 'Archives', 'Applications', 'Code', 'Fonts', 'System Files', 'Torrents', 'Others']

files_extension = {
    'Doc': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.rtf'],
    'Img': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.heic'],
    'Vid': ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm'],
    'Aud': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
    'Arc': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso'],
    'App': ['.exe', '.msi', '.apk', '.bat', '.sh', '.dmg', '.pkg'],
    'Cod': ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.php', '.json', '.xml', '.yml', '.ts', '.rb', '.go', '.cs', '.sql', '.ipynb'],
    'Fnt': ['.ttf', '.otf', '.woff', '.woff2'],
    'Sys': ['.dll', '.sys', '.ini', '.log'],
    'Tor': ['.torrent']
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Folder Cleaner')
        self.geometry('600x220')
        self.resizable(True, True)
        try:
            pywinstyles.apply_style(self, 'Explorer')
        except Exception:
            pass

        main = ttk.Frame(self, padding=12)
        main.pack(fill='both', expand=True)

        ttk.Label(main, text='Select folder to clean:').grid(row=0, column=0, sticky='w')

        self.path_var = tk.StringVar()
        self.entry = ttk.Entry(main, textvariable=self.path_var, width=45)
        self.entry.grid(row=0, column=1, padx=6, pady=6, sticky='w')
        self.moved_files = 0

        ttk.Button(main, text='Browse...', command=self.browse).grid(row=0, column=2, padx=6)

        self.clean_btn = ttk.Button(main, text='Clean', command=self.clean)
        self.clean_btn.grid(row=1, column=1, pady=10, sticky='e')

        self.status = ttk.Label(main, text='')
        self.status.grid(row=2, column=0, columnspan=3, sticky='w')

        main.grid_columnconfigure(1, weight=1)

    def browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)

    def clean(self):
        full_path = self.path_var.get().strip()
        if not full_path:
            messagebox.showerror("Error", "Please select a folder to clean.")
            return
        if not os.path.exists(full_path) or not os.path.isdir(full_path):
            messagebox.showerror("Error", "Path does not exist or is not a folder")
            return

        self.clean_btn.config(state='disabled')
        self.status.config(text='Cleaning...')
        self.update_idletasks()

        try:
            cleaned_path = os.path.join(full_path, "Cleaned")
            os.makedirs(cleaned_path, exist_ok=True)

            for folder in folders:
                os.makedirs(os.path.join(cleaned_path, folder), exist_ok=True)

            mapping = {
                'Doc': 'Documents', 'Img': 'Images', 'Vid': 'Videos', 'Aud': 'Audio',
                'Arc': 'Archives', 'App': 'Applications', 'Cod': 'Code', 'Fnt': 'Fonts',
                'Sys': 'System Files', 'Tor': 'Torrents'
            }

            for file in os.listdir(full_path):
                file_path = os.path.join(full_path, file)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(file)[1].lower()
                    moved = False
                    for key, extensions in files_extension.items():
                        if ext in extensions:
                            target_folder = mapping.get(key, 'Others')
                            shutil.move(file_path, os.path.join(cleaned_path, target_folder))
                            self.moved_files += 1
                            moved = True
                            break
                    if not moved:
                        shutil.move(file_path, os.path.join(cleaned_path, 'Others'))
                        self.moved_files += 1
            self.status.config(text=f'Cleaning completed. Output: {cleaned_path}')
            messagebox.showinfo("Done", f"Files moved to {cleaned_path}. Total files moved: {self.moved_files}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.clean_btn.config(state='normal')

if __name__ == '__main__':
    app = App()
    app.mainloop()
