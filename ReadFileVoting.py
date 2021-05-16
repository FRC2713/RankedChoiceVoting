# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:28:01 2020

@authors: ssainis, pmartel
 Phil Martel is working on being able to read the voting file
 and extract the incandidates and other needed info directly
 
uses https://pypi.org/project/pyrankvote/ by Jon Tingvold
"""

import pyrankvote 
from pyrankvote import Candidate, Ballot

# get name of vote file using a open file dialog box
import tkinter
from tkinter import filedialog


fd = filedialog

fileName = fd.askopenfilename(title = 'Select vote file')



#%% declare the candidates 

# electionSlate = ["C5", "C1",  "C6", "C3", "C4", "C2", "C7"]
# electionSlate = ["C5", "C6", "C3", "C4", "C2", "C7"]
# electionSlate = ["C5", "C6", "C3", "C4", "C7"]
electionSlate = ["C6", "C3", "C4", "C7"]

C5 = Candidate("C5")
C1 = Candidate("C1")
C6 = Candidate("C6")
C3 = Candidate("C3")
C4 = Candidate("C4")
C2 = Candidate("C2")
C7 = Candidate("C7")

# candidates = [C5, C1, C6, C3, C4, C2, C7]
# candidates = [C5, C6, C3, C4, C2, C7]
# candidates = [C5, C6, C3, C4, C7]
candidates = [C6, C3, C4, C7]

ballots = []
#%% import data from the xlsx or google sheet and extract the results

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('SanitizedVoteData_05022021.xlsx')

#remember to check where the column starts.

#print("Column Headings:")
#print(df.columns)

voterChoice = df[df.Timestamp.notnull()]
columnHeaders = voterChoice.columns
columnHeaders = columnHeaders.values.tolist()
voterChoice = voterChoice.drop(columnHeaders[0:3], axis=1)
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
