import cv2
from histogram import *
def main():
    """
    Prompts the user to stabilise and crop the query video before generating the same averaged greyscale, RGB and HSV
    histograms to compare with the database videos' previously stored histograms using distance metrics.
    :return: None
    """
    directory = "./recordings/"
    recordings = ["recording1.mp4", "recording2.mp4", "recording3.mp4", "recording4.mp4"]

    file1 = recordings[3]

    histogram_generator1 = HistogramGenerator(directory, file1)
    b,g,r = histogram_generator1.generate_and_store_average_rgb_histogram()
    table_data,video_match = histogram_generator1.match(b,g,r)
    print("error is :",table_data)
    print("match is :",video_match)
if __name__ == "__main__":
    main()