#python3 -m pip show yt-dlp
#python3 -m pip install yt-dlp
## make sure you’re inside (yolovenv)
pip install yt-dlp

import os
import yt_dlp

playlist_url = "https://www.youtube.com/playlist?list=PLHCNPOIaj2Wc8P5xAWq9g2DUrrbixoTOK"
output_dir = "downloads_720p"
os.makedirs(output_dir, exist_ok=True)

ydl_opts = {
    # video up to 720p + audio, merged to mp4
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    'merge_output_format': 'mp4',
    'outtmpl': os.path.join(output_dir, '%(playlist_index)s - %(title)s.%(ext)s'),
    'noplaylist': False,
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # ensures mp4
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print(f"All videos (with sound) downloaded to folder: {output_dir}")
