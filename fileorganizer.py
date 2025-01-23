import os
import shutil

# Mevcut çalışma dizinini al
directory = os.getcwd()

# Dosya uzantıları ve hedef klasörler
file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    
    'csv': 'Data',
    'xlsx': 'Data', 
    
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
    
    'py': 'PythonScripts',
    'js': 'Scripts',
    'html': 'WebFiles',
    'css': 'WebFiles',
    'json': 'Data',
    'xml': 'Data',
    'ppt': 'Presentations',
    'pptx': 'Presentations',
    'iso': 'DiskImages',
    'dmg': 'DiskImages',
    'tar': 'Archives',
    'gz': 'Archives',
    '7z': 'Archives',
    'sql': 'Database',
    'db': 'Database',
    'log': 'Logs',
    'ini': 'Configurations',
    'cfg': 'Configurations',
    # İhtiyaca göre daha fazla uzantı eklenebilir
}

# Klasörleri oluştur
for folder in set(file_extensions.values()):
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Dosyaları taşı
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Sadece dosyaları işle (klasörleri değil)
    if os.path.isfile(file_path):
        # Dosya uzantısını al
        file_extension = filename.split('.')[-1].lower()

        # Uzantıya göre hedef klasörü belirle
        if file_extension in file_extensions:
            target_folder = file_extensions[file_extension]
            target_path = os.path.join(directory, target_folder, filename)

            # Dosyayı taşı
            shutil.move(file_path, target_path)
            print(f"{filename} taşındı -> {target_folder}")
        else:
            print(f"{filename} için uygun klasör bulunamadı.")