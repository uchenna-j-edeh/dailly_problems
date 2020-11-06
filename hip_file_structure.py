

"""Given a hip file. Get the reference structure"""
import subprocess
import os
import tempfile
import shutil
import re

def _cmd(*args):
    """Run system command using subprocess"""
    print("Exzecuting the command: %s", list(args))
    p = subprocess.Popen(list(args))

    return p.communicate()


def process_hip_file(hip_file):
    if not os.path.exists(hip_file):
        raise IOError("{0} does not exist.".format(hip_file))
    all_files = []
    temp_dir = tempfile.mkdtemp()
    base_name = os.path.basename(hip_file)
    print(base_name)
    shutil.copyfile(hip_file, os.path.join(temp_dir, base_name))
    _cmd('cpio', '-idv', '<', os.path.join(temp_dir, hip_file))

    for root, _, files in os.walk(temp_dir):
        for name in files:
            filename = os.path.join(root, name)
            if hip_file != filename:
                all_files.append(name)

    shutil.rmtree(temp_dir)

    return {"references": all_files}

process_hip_file("/Users/uchenna/hip_files/big_smoke_test_1568808937.hip")

# /home/uchenna/hip-files/big_smoke_test_1568808937.hip





    




