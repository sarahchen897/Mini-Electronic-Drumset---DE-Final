import subprocess
def snare(file_path):
    subprocess.call(['aplay', file_path])
snare("snare2.wav")