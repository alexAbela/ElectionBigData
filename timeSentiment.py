import initSentiment as i
from pyspark.sql.functions import col, lit, to_timestamp, to_date
from pyspark.sql.types import DateType
#dtdata = i.load('hashtag_donaldtrump')
#jbdata = i.load('hashtag_joebiden')
# max tid - første tid / antal perioder
# Står på yyyy, mm, dd

dtdata = i.load('dt10rated')

def getMaxDate(df):
    maxDate = df.agg({"created_at": "max"}).collect()[0]["max(created_at)"]
    return maxDate

def getMinDate(df):
    minDate = df.agg({"created_at": "min"}).collect()[0]["min(created_at)"]
    return minDate

def dateInfo(min, max):
    return (" data created from: " + str(min) + " to " 
    + str(max) + " created over a total of " + str(max-min))

dtMax = getMaxDate(dtdata)
dtMin = getMinDate(dtdata)

#jbMax = getMaxDate(jbdata)
#jbMin = getMinDate(jbdata)

print("Donald Trump" + dateInfo(dtMin, dtMax)) # Donald Trump data collected from: 2020-10-15 to 2020-11-08 collected over a total of 24 days, 0:00:00
#print("Joe Biden" + dateInfo(jbMin, Max)) # Joe Biden data collected from: 2020-10-15 to 2020-11-08 collected over a total of 24 days, 0:00:00

def sortDataAfterDate(df):
    return df.orderBy("created_at","collected_at")

dtsorted = sortDataAfterDate(dtdata).dropna(subset=['created_at'])
dtsorted = dtsorted.dropna(subset=['tweet'])

d1 = ("2020-10-15",  "2020-10-20")
d2 = ("2020-10-21",  "2020-10-26")
d3 = ("2020-10-27",  "2020-11-01")
d4 = ("2020-11-02",  "2020-11-08")


part1 = dtsorted.where(col('created_at').between(*d1))
part2 = dtsorted.where(col('created_at').between(*d2))
part3 = dtsorted.where(col('created_at').between(*d3))
part4 = dtsorted.where(col('created_at').between(*d4))

print(dtsorted.count())

print(part1.count()+part2.count()+part3.count()+part4.count())

print(part1.head())
print(part2.head())
print(part3.head())
print(part4.head())
