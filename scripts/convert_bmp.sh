for f in 0 8 16 24 32 40 48 56; do
  ffmpeg -y -i /home/mmuhina/repo/port/portfolio-2.0/public/frames/frame_${f}.webp -s 320x180 /home/mmuhina/repo/port/portfolio-2.0/scripts/f${f}.bmp >/dev/null 2>&1
done
ls -la /home/mmuhina/repo/port/portfolio-2.0/scripts/f*.bmp