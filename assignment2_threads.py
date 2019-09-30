import os
import shutil
from concurrent.futures import ThreadPoolExecutor


src_files = os.listdir('./folder_1')
for file_name in src_files:
    full_file_name = os.path.join('./folder_1', file_name)
    if os.path.isfile(full_file_name):
        executor = ThreadPoolExecutor(5)
        executor.submit(shutil.copy, full_file_name, './folder_thread')
