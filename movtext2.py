from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

input_path = "Cute Leopard Baby Walking In the Snow.mp4"
output_path = "output_moviepy_static.mp4"

clip = VideoFileClip(input_path)

# Create a text clip. Adjust fontsize, color, font path as needed.
txt = TextClip("Hello, this is a caption", fontsize=48, color='white', font='Arial-Bold') \
        .set_position(('center', 'bottom')) \
        .set_duration(clip.duration)

# Composite the text on the video
result = CompositeVideoClip([clip, txt])
result.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=clip.fps)
