# Databricks notebook source
"""
df - DataFrame To Be Modified
N - No Of Cells To Be Modified
ColList - Column Numbers Which Need To Be Modified [0-Based Indexing]
"""
def AnomolyInsertion(df,N,ColList=None):
    if(ColList):
        RLen,CLen = df.shape
        Col = df.columns.tolist()
        ColToAn = [Col[Ind] for Ind in ColList]
        ColLen = len(ColToAn)
        SampleData = []
        for i in df[ColToAn].sample(5).values.tolist():
            SampleData.extend(i)
        NanData = [np.nan]*ColLen
        SampleData.extend(NanData)
        for _ in range(N):
            Header = random.choice(ColToAn)
            Rec = random.randint(0,RLen-1)
            df[Header][Rec] = random.choice(SampleData)
    else:
        return "No Column Indexes"
