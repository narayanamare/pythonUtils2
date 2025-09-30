from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Load a video file
video_clip = VideoFileClip("Cute Leopard Baby Walking In the Snow.mp4")

# Add a text overlay
text = TextClip("Hello, World!", fontsize=70, color='white')
# Set the duration and position of the text
text = text.set_duration(5).set_position('center')

# Combine the video and text
final_video = CompositeVideoClip([video_clip, text])

# Write the final video file
final_video.write_videofile("output_video.mp4", codec='libx264')
