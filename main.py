import init as i
import cleanMethods as cm
import sentimentMethods as sm



def main(file, sqlContext):
    #Initiates the original csv file and selects the columns we need
    data = i.load(str(file))
    data = data.select('tweet', 'created_at', 'state', 'country').cache()

    #Filters for english and american tweets
    data = cm.filterEnglish(data, sqlContext)
    data = data.dropna(subset=['tweet']).cache()

    #Cleans the text in the tweets
    data = cm.clean(data, sqlContext).cache()

    #Analyses sentiment in tweets
    data = sm.analyse(data, sqlContext).cache()

    return data






