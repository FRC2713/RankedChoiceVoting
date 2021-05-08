# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:28:01 2020

@author: ssainis

uses https://pypi.org/project/pyrankvote/ by Jon Tingvold
"""

import pyrankvote 
from pyrankvote import Candidate, Ballot

#%% declare the candidates 

# electionSlate = ["C5", "C6", "C3", "C7", "C2", "C4", "C1"]
#electionSlate = ["C6", "C3", "C7", "C2", "C4", "C1"]
electionSlate = ["C3", "C7", "C2", "C4", "C1"]

C5 = Candidate("C5")
C6 = Candidate("C6")
C3 = Candidate("C3")
C7 = Candidate("C7")
C2 = Candidate("C2")
C4 = Candidate("C4")
C1 = Candidate("C1")

#candidates = [C5, C6, C3, C7, C2, C4, C1]
#candidates = [C6, C3, C7, C2, C4, C1]
candidates = [C3, C7, C2, C4, C1]
ballots = []
#%% import C4 from the xlsx or google sheet and extract the results

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('Sanitized2020VoteData.xlsx')

#print("Column Headings:")
#print(df.columns)

voterChoice = df[df.Timestamp.notnull()]
columnHeaders = voterChoice.columns
columnHeaders = columnHeaders.values.tolist()
voterChoice = voterChoice.drop(columnHeaders[0:4], axis=1)
voterChoice = voterChoice.values.tolist()
for i in range(len(voterChoice)):
    voter_ranking = []
    for j in range(len(voterChoice[i][:])):
        if not pd.isna(voterChoice[i][j]):
            try:
                index_value = electionSlate.index(voterChoice[i][j])
                voter_ranking.append(candidates[index_value])
            except ValueError :
                pass 
    ballots.append(Ballot(ranked_candidates = voter_ranking))


#%% assemble the ballot 

# ballots.append(Ballot(ranked-candidates = []))

#%% get election results 
election_result = pyrankvote.instant_runoff_voting(candidates, ballots)

winners = election_result.get_winners()
print(election_result)
