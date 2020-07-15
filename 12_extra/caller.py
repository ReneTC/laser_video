import sys
import subprocess

word = ""
words = [
"Quantum Jump",
"Stimulated Absorption",
"Spontaneous Emission",
"Meta-stable State",
"Selection Rules",
"Phosphorescence",
"Stimulated Emission",
"Optical Cavity",
"Gain Medium",
"Optical Pump",
"Population Inversion",
"Photoluminescence",
"Radiationless Transition",
"Output Coupler",
"High Reflector",
]
for i in range(0,len(words)):
    word = words[i]
    subprocess.call([sys.executable, 'words.py',word])
