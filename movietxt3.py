from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Input and output paths
input_path = "Cute Leopard Baby Walking In the Snow.mp4"
output_path = "output_with_text.mp4"

# Load video
clip = VideoFileClip(input_path)

# Create text overlay using Pillow (method='caption')
txt = (TextClip("Hello, this is a caption",
                fontsize=48,
                color='white',
                font='Arial-Bold',   # you can use 'Arial', 'Times', etc.
                method='caption')    # <-- forces Pillow backend
       .set_position(("center", "bottom"))  # bottom center
       .set_duration(clip.duration))        # show for entire video

# Combine text with video
final = CompositeVideoClip([clip, txt])

# Export result
final.write_videofile(output_path,
                      codec="libx264",
                      audio_codec="aac",
                      fps=clip.fps)

print("✅ Video created with text overlay using Pillow!")
