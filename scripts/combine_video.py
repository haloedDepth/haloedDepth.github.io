import sys
from moviepy.editor import VideoFileClip, CompositeVideoClip

def combine_videos(video_path_1, video_path_2, output_path):
    try:
        # Load the videos
        print("Loading videos...")
        clip1 = VideoFileClip(video_path_1)
        clip2 = VideoFileClip(video_path_2)

        print("Processing video 1 (1:1 aspect ratio)...")
        # Resize the first video to 1:1 aspect ratio
        min_dimension_1 = min(clip1.size)
        clip1 = clip1.resize(newsize=(min_dimension_1, min_dimension_1))

        print("Processing video 2 (9:7 aspect ratio)...")
        # Resize the second video to 9:7 aspect ratio
        clip2_aspect_ratio = 9 / 7
        clip2 = clip2.resize(height=int(clip2.w / clip2_aspect_ratio))

        print("Combining videos side by side...")
        # Position clips side by side
        clip1 = clip1.set_position("left")
        clip2 = clip2.set_position("right")

        # Create a composite video clip
        final_clip = CompositeVideoClip([clip1, clip2], size=(clip1.w + clip2.w, max(clip1.h, clip2.h)))

        # Write the output file
        print("Writing output video...")
        final_clip.write_videofile(output_path, codec="libx264", fps=24)

        return "Video combined successfully."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python combine_videos.py video1.mp4 video2.mp4 output.mp4")
        sys.exit(1)

    video_path_1 = sys.argv[1]
    video_path_2 = sys.argv[2]
    output_path = sys.argv[3]

    result = combine_videos(video_path_1, video_path_2, output_path)
    print(result)
