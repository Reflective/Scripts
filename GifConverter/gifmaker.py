import imageio
import os

from numpy import source


# Definitions


def Gifmaker(inputPath, targetFormat):
    outputPath = (
        os.path.splitext(inputPath)[0]
        + targetFormat  # creates list with file name and target format
    )

    # {add var contents to formatted string}
    print(f"\n Converting\n {inputPath} \n to \n {outputPath}")

    # read original clip with imageio
    reader = imageio.get_reader(inputPath)

    # takes fps meta data from reader
    originalfps = reader.get_meta_data()["fps"]
    # additional fps based on original
    slowmo = originalfps * 2
    doubletime = originalfps / 2
    # writes output. change speed with second argument
    writer = imageio.get_writer(outputPath, fps=originalfps)
    # loops through and writes each frame in clip
    for frames in reader:
        writer.append_data(frames)
        print(f"Frame: {frames}")
    print("Done!")
    writer.close()


video = os.path.abspath("RobotWalk.mp4")
format = ".gif"

Gifmaker(video, format)
