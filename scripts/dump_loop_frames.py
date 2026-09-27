# Let us extract frames from character.mp4 between 180 and 220 and between 15 and 45
# We can use ffmpeg to dump frames 185..215 and 20..40 to bmp or raw
import subprocess
import os

os.makedirs("/home/mmuhina/repo/port/portfolio-2.0/scripts/frames_loop", exist_ok=True)
# dump frames 20 to 40
cmd1 = "ffmpeg -y -i /home/mmuhina/repo/port/portfolio-2.0/public/character.mp4 -vf 'select=between(n\\,20\\,40)' -vsync 0 -s 320x180 /home/mmuhina/repo/port/portfolio-2.0/scripts/frames_loop/f_start_%02d.bmp"
# dump frames 190 to 215
cmd2 = "ffmpeg -y -i /home/mmuhina/repo/port/portfolio-2.0/public/character.mp4 -vf 'select=between(n\\,190\\,215)' -vsync 0 -s 320x180 /home/mmuhina/repo/port/portfolio-2.0/scripts/frames_loop/f_end_%02d.bmp"
subprocess.run(cmd1, shell=True)
subprocess.run(cmd2, shell=True)
print("Dumped frames")