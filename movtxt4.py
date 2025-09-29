from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Input and output paths
input_path = "Cute Leopard Baby Walking In the Snow.mp4"
output_path = "output_with_text.mp4"

# Load video
clip = VideoFileClip(input_path)

# Create a Pillow image (RGBA) for text
txt_img = Image.new("RGBA", (clip.w, 100), (0, 0, 0, 0))  # transparent background
draw = ImageDraw.Draw(txt_img)

# Load a system font (adjust path if needed)
try:
    font = ImageFont.truetype("arial.ttf", 48)
except:
    font = ImageFont.load_default()

# Draw text onto the image
draw.text((clip.w // 2, 50), "Hello, this is a caption", font=font, fill="white", anchor="mm")

# Convert Pillow image to numpy array → MoviePy ImageClip
txt_clip = (ImageClip(np.array(txt_img))
            .set_duration(clip.duration)
            .set_position(("center", "bottom")))

# Combine video + text
final = CompositeVideoClip([clip, txt_clip])

# Export video
final.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=clip.fps)

print("✅ Video created with Pillow text overlay!")
