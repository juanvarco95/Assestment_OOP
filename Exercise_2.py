import os

class FolderManager:
    def __init__(self, base_path):
        self.base_path = base_path
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            print(f"Created base folder: {base_path}")

    def create_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Folder created: {path}")
        else:
            print(f"Folder already exists: {path}")

    def list_folders(self):
        items = os.listdir(self.base_path)
        folders = [f for f in items if os.path.isdir(os.path.join(self.base_path, f))]
        print(f"Folders inside {self.base_path}: {folders}")
        return folders

    def delete_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if os.path.exists(path) and os.path.isdir(path):
            os.rmdir(path)  
            print(f"Folder deleted: {path}")
        else:
            print(f"Folder not found: {path}")