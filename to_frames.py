import av
import os

# Define the directory where frames will be saved
frames_dir = "output_frames/"
if os.path.exists(frames_dir):
    for file in os.listdir(frames_dir):
        os.remove(os.path.join(frames_dir, file))
else:
    os.makedirs(frames_dir)

with av.open("Kanako Ganbareyo.mp4") as container:
    # Signal that we only want to look at keyframes.
    stream = container.streams.video[0]
    # stream.codec_context.skip_frame = "NONKEY"

    count = 0
    for frame in container.decode(stream):

        print(frame)
        frame.to_image().save(
            f"{frames_dir}frame.{count:04d}.jpg",
            quality=80,
        )
        count += 1