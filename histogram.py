import csv
import math
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
from helpers import get_video_filenames, print_terminal_table

def _normalise_histogram(hist):
    """
    Normalise a histogram using OpenCV's "normalize" function.
    :param hist: the histogram to normalise
    :return: the normalised histogram
    """
    hist = cv2.normalize(hist, hist)
    return hist


def _get_frames_to_process(vc):
    """
    Returns the IDs of the frames to calculate a histogram for. 1 Frame Per Second.
    :param vc: the VideoCapture object to process
    :return: a list of integers representing the frames to process
    """
    frame_ids = list()
    total_frames = vc.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = vc.get(cv2.CAP_PROP_FPS)
    for i in range(1, int(total_frames) + 1, math.ceil(fps)):
        frame_ids.append(i)
    return frame_ids

class HistogramGenerator:
    colours = ('b', 'g', 'r')  # RGB channels
    bins = (8, 12, 3)  # 8 hue bins, 12 saturation bins, 3 value bins
    histcmp_methods = [cv2.HISTCMP_CORREL, cv2.HISTCMP_CHISQR, cv2.HISTCMP_INTERSECT, cv2.HISTCMP_HELLINGER]
    histcmp_3d_methods = ["earths_mover_distance", "energy_distance"]
    histogram_comparison_weigths = {  # weights per comparison methods
        'gray': 1,
        'rgb': 5,
        'hsv': 10
    }
    results_array = list()

    def __init__(self, directory, file_name):
        """
        Initialise variables and create a VideoCapture object for a mp4 file.
        :param directory: the directory where the video file is located
        :param file_name: the mp4 video file's name
        """
        self.directory = directory
        self.file_name = file_name

        # start capturing video
        self.video_capture = cv2.VideoCapture("{}{}".format(self.directory, self.file_name))
        self.check_video_capture()

        # dicts of lists to store histograms for each frame
        self.histograms_grey_dict = list()
        self.histograms_rgb_dict = {
            'b': list(),
            'g': list(),
            'r': list()
         }
        self.histograms_hsv_dict = list()

        # keep current ROI for re-use
        self.reference_points = list()
    def get_video_capture(self):
            """
            Returns the full VideoCapture object.
            :return: the VideoCapture object
            """
            return self.video_capture
    def get_results_array(self):
            """
            Returns the array with the resulting video results.
            :return: array of strings
            """
            return self.results_array
       
    def generate_and_store_average_rgb_histogram(self):
        """
        Generates a single RGB histogram by averaging all histograms of a video before normalising it and saving the
        results to a plain text file.
        :return: None
        """

        frames_to_process = _get_frames_to_process(self.video_capture)
        frame_counter = 0  # keep track of current frame ID to know to process it or not
        while self.video_capture.isOpened():
            ret, frame = self.video_capture.read()  # read capture frame by frame
            if ret:
                frame_counter += 1
                if frame_counter in frames_to_process:
                    for i, col in enumerate(self.colours):

                        histogram = cv2.calcHist([frame], [i], None, [256], [0, 256])
                        self.histograms_rgb_dict[col].append(histogram)

            else:
                break
        self.destroy_video_capture()

        avg_histogram = np.zeros(shape=(255, 1))  # array to store average histogram values
        for col, hists in self.histograms_rgb_dict.items():
            for i in range(0, 255):  # loop through all bins
                bin_sum = 0
                # get value for each colour histogram in bin i
                for arr_index in range(0, len(hists)):
                    bin_value = hists[arr_index].item(i)
                    bin_sum += bin_value
                # average all bins values to store in new histogram
                new_bin_value = bin_sum / len(hists)
                avg_histogram[i] = new_bin_value
            # normalise averaged histogram
            avg_histogram = _normalise_histogram(avg_histogram)
            
            # if not os.path.exists("./histogram_data/{}/".format(self.file_name)):
            #     os.makedirs("./histogram_data/{}/".format(self.file_name))
            # with open("./histogram_data/{}/hist-{}.txt".format(self.file_name, col), 'w') as file:
            #     file.write("# HSV Histogram shape: {0} [normalised]\n".format(avg_histogram.shape))
            #     for arr_2d in avg_histogram:
            #         file.write("# New slice\n")

            #         np.savetxt(file, arr_2d)
        #print(avg_histogram)
        b = np.zeros(shape=(255, 1))
        g = np.zeros(shape=(255, 1))
        r = np.zeros(shape=(255, 1))
        for col, hists in self.histograms_rgb_dict.items():
            for i in range(0, 255):  # loop through all bins
                if col == 'b':
                    b[i] =  avg_histogram[i]
                elif col == 'g':
                    g[i] =  avg_histogram[i]
                elif col == 'r':
                    r[i] =  avg_histogram[i]
        return b,g,r
        
                
 
  
    def match(self,b,g,r):
        video_match = ""
        video_match_value = 0
        method = ""
        csv_field_names = ["video", "score"]
        query_histogram = dict()
        # query_histogram = {
        #         'b': np.loadtxt("./histogram_data/{}/hist-b.txt".format(self.file_name), dtype=np.float32, unpack=False),
        #         'g': np.loadtxt("./histogram_data/{}/hist-g.txt".format(self.file_name), dtype=np.float32, unpack=False),
        #         'r': np.loadtxt("./histogram_data/{}/hist-r.txt".format(self.file_name), dtype=np.float32, unpack=False)
        #     }
        query_histogram = {
                'b': np.float32(b),
                'g': np.float32(g),
                'r': np.float32(r)
            }
        for m in self.histcmp_methods:
            if m == 0:
                method = "CORRELATION"
            elif m == 1:
                method = "CHI-SQUARE"
            elif m == 2:
                method = "INTERSECTION"
            elif m == 3:
                method = "HELLINGER"

        table_data = list()
        for i, file in enumerate(get_video_filenames("./footage/")):
            comparison = 0
            dbvideo_b_histogram = np.loadtxt("./histogram_data/{}/hist-b.txt".format(file), dtype=np.float32, unpack=False)
            dbvideo_g_histogram = np.loadtxt("./histogram_data/{}/hist-g.txt".format(file), dtype=np.float32, unpack=False)
            dbvideo_r_histogram = np.loadtxt("./histogram_data/{}/hist-r.txt".format(file), dtype=np.float32, unpack=False)

            comparison_b = cv2.compareHist(query_histogram['b'], dbvideo_b_histogram, m)
            comparison_g = cv2.compareHist(query_histogram['g'], dbvideo_g_histogram, m)
            comparison_r = cv2.compareHist(query_histogram['r'], dbvideo_r_histogram, m)
            comparison = (comparison_b + comparison_g + comparison_r) / 3

            # append data to table
            table_data.append([file, round(comparison, 5)])

            # write data to CSV file
            if i == 0:
                video_match = file
                video_match_value = comparison
            else:
                # Higher score = better match (Correlation and Intersection)
                if m in [0, 2] and comparison > video_match_value:
                    video_match = file
                    video_match_value = comparison
                # Lower score = better match
                # (Chi-square, Alternative chi-square, Hellinger and Kullback-Leibler Divergence)
                elif m in [1, 3, 4, 5] and comparison < video_match_value:
                    video_match = file
                    video_match_value = comparison
        for _ in range(0, self.histogram_comparison_weigths['rgb'], 1):
            self.results_array.append(video_match)
        # print("error is :",table_data)
        # print("match is :",video_match)
        return table_data,video_match
        


    def check_video_capture(self):
        """
        Checks if the VideoCapture object was correctly created.
        :return: None
        """
        if not self.video_capture.isOpened():
            print("Error opening video file")

    def destroy_video_capture(self):
        """
        Tidying up the OpenCV environment and the video capture.
        :return: None
        """
        self.video_capture.release()
        cv2.destroyAllWindows()






