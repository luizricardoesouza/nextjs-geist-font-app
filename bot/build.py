#!/usr/bin/env python3

import os
import platform
import subprocess
import shutil
from datetime import datetime

def create_release_folder():
    """Create a release folder with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    release_dir = f"release_{timestamp}"
    os.makedirs(release_dir, exist_ok=True)
    return release_dir

def copy_config_files(release_dir):
    """Copy necessary config files to release directory"""
    os.makedirs(os.path.join(release_dir, "config"), exist_ok=True)
    
    # Copy config files
    shutil.copy2("utils/config.py", os.path.join(release_dir, "config"))
    shutil.copy2("README.md", release_dir)
    
def build_executable():
    """Build the executable using PyInstaller"""
    system = platform.system().lower()
    
    print("Starting build process...")
    
    # Create release directory
    release_dir = create_release_folder()
    
    # Base PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',
        '--name=TibiaBot',
        '--add-data=utils/config.py:utils',
        'main.py'
    ]
    
    # Add platform-specific options
    if system == 'windows':
        cmd.extend(['--noconsole'])
        if os.path.exists('tibia.ico'):
            cmd.append('--icon=tibia.ico')
    
    try:
        # Execute build
        subprocess.run(cmd, check=True)
        
        # Copy executable to release directory
        executable_name = "TibiaBot.exe" if system == "windows" else "TibiaBot"
        shutil.copy2(
            os.path.join("dist", executable_name),
            os.path.join(release_dir, executable_name)
        )
        
        # Copy config files
        copy_config_files(release_dir)
        
        print(f"\nBuild completed successfully!")
        print(f"Release package created in: {release_dir}/")
        print("\nContents:")
        print(f"- {executable_name}")
        print("- config/")
        print("- README.md")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during build: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    build_executable()
