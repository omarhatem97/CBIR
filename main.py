import cv2
from histogram import *
def main():
    """
    Prompts the user to stabilise and crop the query video before generating the same averaged greyscale, RGB and HSV
    histograms to compare with the database videos' previously stored histograms using distance metrics.
    :return: None
    """
    directory = "./recordings/"
    recordings = ["football.mp4", "beach.mp4", "bird-walking.mp4", "butterfly.mp4", "recording5.mp4", "recording3.mp4","vid1.mp4","vid2.mp4", "stable-recording5.avi"
    , "recording7.mp4", "recording8.mp4"]
    mismatches_directory = "./recordings/mismatches/"
    mismatches = ["mismatch1.mp4", "mismatch2.mp4"]
    file1 = recordings[10]

    histogram_generator1 = HistogramGenerator(directory, file1)
    histogram_generator1.generate_and_store_average_rgb_histogram()
    table_data,video_match = histogram_generator1.match()
    print("error is :",table_data)
    print("match is :",video_match)
if __name__ == "__main__":
    main()