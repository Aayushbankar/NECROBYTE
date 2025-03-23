# Function: scan_directory(path)	Accepts a directory path, recursively lists all files and subdirectories
import os
import sys

# Lists to store paths
alt_root_fldr = []
alt_dirs = []
alt_files = []

def win_scan_the_target():
    for root, dirnames, filenames in os.walk("C:\\"):
        alt_root_fldr.append(root)
        for file in filenames:
            alt_files.append(os.path.join(root, file))
        for fldr in dirnames:
            alt_dirs.append(os.path.join(root, fldr))
    return alt_root_fldr, alt_dirs, alt_files

def posix_scan_the_target():
    for root, dirnames, filenames in os.walk("/"):
        alt_root_fldr.append(root)
        for file in filenames:
            alt_files.append(os.path.join(root, file))
        for fldr in dirnames:
            alt_dirs.append(os.path.join(root, fldr))
    return alt_root_fldr, alt_dirs, alt_files

def darwin_scan_the_target():
    # macOS is also POSIX, so similar logic
    return posix_scan_the_target()

def cstm_dir_scan(path):
    for root, dirnames, filenames in os.walk(path):
        alt_root_fldr.append(root)
        for file in filenames:
            alt_files.append(os.path.join(root, file))
        for fldr in dirnames:
            alt_dirs.append(os.path.join(root, fldr))
    return alt_root_fldr, alt_dirs, alt_files

def print_the_target():
    print("\n[Root Folders]")
    for root in alt_root_fldr:
        print(root)
    print("\n[Directories]")
    for d in alt_dirs:
        print(d)
    print("\n[Files]")
    for f in alt_files:
        print(f)

if __name__ == "__main__":
    ostype = sys.platform
    print(f"OS Type Detected: {ostype}\n")

    if ostype == "win32":
        win_scan_the_target()
        print_the_target()
    elif ostype == "linux":
        print(f"Scanning current working directory: {os.getcwd()}\n")
        cstm_dir_scan(os.getcwd())
        print_the_target()
    elif ostype == "darwin":
        darwin_scan_the_target()
        print_the_target()
    else:
        print("Unknown OS")
