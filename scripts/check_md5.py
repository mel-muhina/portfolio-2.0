import hashlib

def get_md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

print("MD5 character.mp4:", get_md5('/home/mmuhina/repo/port/portfolio-2.0/public/character.mp4'))