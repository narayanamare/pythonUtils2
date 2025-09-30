from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load clips
clip1 = VideoFileClip("clip1.mp4").subclip(0, 7)  # trim to 7s
clip2 = VideoFileClip("clip2.mp4").subclip(0, 7)  # trim to 7s
clip3 = VideoFileClip("clip3.mp4").subclip(0, 6)  # trim to 6s

# Combine
final_clip = concatenate_videoclips([clip1, clip2, clip3])

# Ensure 20s duration (trim if slightly longer)
final_clip = final_clip.subclip(0, 20)

# Export
final_clip.write_videofile("final_20s_video.mp4", codec="libx264")
