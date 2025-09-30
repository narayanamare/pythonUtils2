from moviepy.editor import VideoFileClip, concatenate_videoclips


# ----------------------------
# SETTINGS
# ----------------------------
# List of video files to combine
input_videos = ["mov1.mov", "mov2.mov", "mov3.mov"]

# Desired final duration
final_duration = 20  # seconds

# Output file
output_file = "final_20s_video.mov"

# ----------------------------
# LOAD & PREPARE CLIPS
# ----------------------------
clips = [VideoFileClip(v) for v in input_videos]

# Calculate how long each clip should be to fit total duration
equal_duration = final_duration / len(clips)

# Trim or speed up each clip to fit the equal duration
prepared_clips = []
for clip in clips:
    if clip.duration > equal_duration:
        # Trim if too long
        prepared_clips.append(clip.subclip(0, equal_duration))
    else:
        # Speed up if too short
        prepared_clips.append(clip.fx(lambda c: c.speedx(c.duration / equal_duration)))

# ----------------------------
# COMBINE CLIPS
# ----------------------------
final_clip = concatenate_videoclips(prepared_clips)

# Just in case it's slightly longer, cut it to exactly 20s
final_clip = final_clip.subclip(0, final_duration)

# ----------------------------
# EXPORT
# ----------------------------
final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

print(f"✅ Final video saved as {output_file}")
