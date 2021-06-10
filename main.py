import cv2
from histogram import *
import os
def main():
    """
    Prompts the user to stabilise and crop the query video before generating the same averaged greyscale, RGB and HSV
    histograms to compare with the database videos' previously stored histograms using distance metrics.
    :return: None
    """
    directory = "./test/"
    arr = os.listdir(directory)
    #print(arr)
    #recordings = ['airplane-window.mp4', 'autumn.mp4', 'beach.mp4', 'bird-walking.mp4', 'butterfly.mp4', 'candles.mp4', 'christmas.mp4', 'cloudy-sky.mp4', 'clown-fish.mp4', 'coffee-machine.mp4', 'cooking.mp4', 'crops-field.mp4', 'dark-city.mp4', 'disco-ball.mp4', 'dunes.mp4', 'dusk-city.mp4', 'earth.mp4', 'eiffel-tower.mp4', 'flower.mp4', 'flowing-river.mp4', 'food-market.mp4', 'gym-workout.mp4', 'ice-hockey.mp4', 'ice_cream.mp4', 'jellyfish.mp4', 'moon.mp4', 'offroad-car.mp4', 'people-dancing.mp4', 'photographer.mp4', 'playing-basketball.mp4', 'police-car.mp4', 'seal.mp4', 'shuttle-landing.mp4', 'sketching.mp4', 'spaghetti.mp4', 'strawberry-slicing.mp4', 'street-artist.mp4', 'surfer.mp4', 'sushi.mp4', 'swimming-pool.mp4', 'swing.mp4', 'timelapse-night.mp4', 'traffic.mp4', 'waves.mp4', 'wind-turbine.mp4', 'winter.mp4', 'work.mp4', 'workers.mp4', 'writing.mp4']
    # for i in  range(20):
    #     file = recordings[i]
    #     histogram_generator1 = Histogram(directory, file)
    #     histogram_generator1.generate_and_store_average_rgb_histogram()
    recordings = ['buff.mp4']
    file = recordings[0]
    histogram_generator1 = Histogram(directory, file)
    b,g,r = histogram_generator1.generate_and_store_average_rgb_histogram()
    table_data,video_match,res = histogram_generator1.match(b,g,r)
    print("error is :",table_data)
    print("match is :",video_match)
    if len(res)>0:
        print("result :",res)
if __name__ == "__main__":
    main()