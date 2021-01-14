import init as i
import time
import cleanMethods as cm
import sentimentMethods as sm

"""
Our 'main' script which we can run in the pyspark and it will run the data through all of our methods. 
This is instead of having to hardcode the cleaning process every time we want to clean a new dataset
"""

def handleData(filename, sqlContext):
    start_time = time.time()
    #Initiates the original csv file and selects the columns we need
    data = i.load(str(filename))
    data = data.repartition(3)
    #Selecting only the fields we need in order to make the dataset as small as possible
    data = data.select('tweet', 'created_at', 'state', 'country').cache()

    print('Initiating filtering for english')

    #Filters for english and american tweets
    data = cm.filterEnglish(data, sqlContext)
    data = data.dropna(subset=['tweet']).cache()

    print("--- %s seconds ---" % (time.time() - start_time))

    print('Initiating cleaning of tweets')

    #Cleans the text in the tweets
    data = cm.clean(data, sqlContext).cache()
    data = data.dropna(subset=['tweet']).cache()

    print("--- %s seconds ---" % (time.time() - start_time))

    print('Initiating cleaning of Analysis of tweets')

    #Analyses sentiment in tweets
    data = sm.analyse(data, sqlContext).cache()

    print("--- %s seconds ---" % (time.time() - start_time))

    data = data.coalesce(1)
    return data






