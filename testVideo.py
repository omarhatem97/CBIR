from FeatureExtractor import *

def retrieve_video(results,b2,g2,r2):
    """
    get the names and values of errors for the best match five videos in the database under threshold.
    :param results: list of histograms and files names of videos in database
    :param b2: database video green
    :param g2: database video red
    :param r2: query video blue
    :return: best match video name, list of the best five match videos under threshold
    """
    video_match = ""
    video_match_value = 0
    table_data = list()
    i = 0
    res = []
    for vid in results:
        arr = pickle.loads(vid[0])
        arr2= pickle.loads(vid[1])
        arr3 = pickle.loads(vid[2])
        arr4 = vid[3]
        histogram_generator1 = Histogram(dir, own)
        avg = histogram_generator1.match(b2,g2,r2,arr,arr2,arr3)
        table_data.append([arr4, round(avg, 5)])
        if i == 0:
          video_match = arr4
          video_match_value = avg
        else:
            if avg < video_match_value:
              video_match = arr4
              video_match_value = avg
        i += 1
    sorted_res = sorted(table_data, key=lambda x: x[1])
    k = 0

    for i in sorted_res:
      if k == 5:
        break
      elif i[1] < 0.4:
          res.append(i)
      k = k+1
    if (len(res) == 0):
      res.append(sorted_res[0])
      
    return res, video_match


video_path = r'./videos/'
dir = r'./test/'
rec = ['good_fish.MP4','good_ear.mp4','airplane.mp4','bad_dog.MP4','beach.mp4','dog.mp4']
own = rec[5]

f = FeatureExtractor()


results,b2,g2,r2 = f.test_video(dir, own)
res , vid = retrieve_video(results,b2,g2,r2)
print(res)
print(vid)