from pathlib import Path
import subprocess, sys
root=Path(__file__).resolve().parent
for folder in sorted(root.glob('Project_*')):
    print('\\n'+'='*70+'\\n',folder.name)
    subprocess.run([sys.executable,str(folder/'train.py')],check=True)
print('All 22 project pipelines completed.')
