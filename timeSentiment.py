# max tid - første tid / antal perioder
# Står på yyyy, mm, dd
import init as i

dtdata = i.load('hashtag_donaldtrump')
jbdata = i.load('hashtag_donaldtrump')

def getMaxDate(df):
    max = df.agg({"collected_at": "max"}).collect()[0]
    return max

def getMinDate(df):
    min = df.agg({"collected_at": "min"}).collect()[0]
    return min

dtMax = getMaxDate(dtdata)
dtMin = getMinDate(dtdata)

jbMax = getMaxDate(jbdata)
jbMin = getMinDate(jbdata)
