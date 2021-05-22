# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:28:01 2020

@authors: ssainis, pmartel

uses https://pypi.org/project/pyrankvote/ by Jon Tingvold
Modifying to extract candiate data from vote file
"""
import math
from tkinter import filedialog

import pyrankvote 
from pyrankvote import Candidate, Ballot

import pandas as pd
#from pandas import ExcelWriter
from pandas import ExcelFile

#
# get name of vote file
def  getFileName():
    
    fd = filedialog

    fileName = fd.askopenfilename(title = 'Select vote file',
                                  filetypes=[('Excel file','*.xlsx'),
                                             ('All files','*.*')])
    return fileName

##This runs if this code is run as a script
if __name__ == "__main__":
    status = 'ok'
    fileName =getFileName()
    if fileName == '' :
        status = 'Error: no file selected'
    else :
        try:
            df = pd.read_excel( fileName )
        except ValueError:
            status = 'Error: File ' + fileName + 'is not an Excel file'
        else :
##            print("Column Headings:")
##            print(df.columns)
            voterChoice = df[df.Timestamp.notnull()]
            columnHeaders = voterChoice.columns
            columnHeaders = columnHeaders.values.tolist()
            voterChoice = voterChoice.drop(columnHeaders[0:3], axis=1)
            ballotList = voterChoice.values.tolist()
            # cSet is all the candidates that received at least
            # one vote.  Right now, an empty cell shows as 'nan'
            cSet = set()
            for v in ballotList :
                cSet.update(v)
            print("cset")
            print(cSet)
            candidateList = []
            candidateName = []
            for c in cSet :
                # treat nil/nan as a special case
                if type(c) != type(1.) :  # this traps Not a Number
                    candidateList.append(Candidate(c))
                    candidateName.append(c)
            
            print("candidates")
            print( candidateList )

            ballots = []
            for i in range(len(ballotList)) :
                voter_ranking = []
                b = ballotList[i]
                for j in range(len(b)) :
                    #There should be a better way
                    for k in range(len(candidateList)) :
                        if b[j] == candidateList[k].name :
                            voter_ranking.append(candidateList[k])
                            break
                        continue
                    if k == len(candidateList) :
                        voter_ranking.append("")
                    continue
                
                ballots.append(Ballot(ranked_candidates = voter_ranking))  
                    
            for b in ballots:
                print(b)
                
        import multiple_seat_ranking_methods
        election_result = pyrankvote.instant_runoff_voting(candidateList, ballots)

        winners = election_result.get_winners()
        print(election_result)

    print( status )
    
###%% declare the candidates 
##
### electionSlate = ["C5", "C1",  "C6", "C3", "C4", "C2", "C7"]
### electionSlate = ["C5", "C6", "C3", "C4", "C2", "C7"]
### electionSlate = ["C5", "C6", "C3", "C4", "C7"]
##electionSlate = ["C6", "C3", "C4", "C7"]
##
##C5 = Candidate("C5")
##C1 = Candidate("C1")
##C6 = Candidate("C6")
##C3 = Candidate("C3")
##C4 = Candidate("C4")
##C2 = Candidate("C2")
##C7 = Candidate("C7")
##
### candidates = [C5, C1, C6, C3, C4, C2, C7]
### candidates = [C5, C6, C3, C4, C2, C7]
### candidates = [C5, C6, C3, C4, C7]
##candidates = [C6, C3, C4, C7]
##
##ballots = []
###%% import data from the xlsx or google sheet and extract the results
##
##import pandas as pd
##from pandas import ExcelWriter
##from pandas import ExcelFile
##
##df = pd.read_excel('SanitizedVoteData_05022021.xlsx')
##
###remember to check where the column starts.
##
###print("Column Headings:")
###print(df.columns)
##
##voterChoice = df[df.Timestamp.notnull()]
##columnHeaders = voterChoice.columns
##columnHeaders = columnHeaders.values.tolist()
##voterChoice = voterChoice.drop(columnHeaders[0:3], axis=1)
##voterChoice = voterChoice.values.tolist()
##for i in range(len(voterChoice)):
##    voter_ranking = []
##    for j in range(len(voterChoice[i][:])):
##        if not pd.isna(voterChoice[i][j]):
##            try:
##                index_value = electionSlate.index(voterChoice[i][j])
##                voter_ranking.append(candidates[index_value])
##            except ValueError :
##                pass 
##    ballots.append(Ballot(ranked_candidates = voter_ranking))
##
##
###%% assemble the ballot 
##
### ballots.append(Ballot(ranked-candidates = []))
##
###%% get election results 
##election_result = pyrankvote.instant_runoff_voting(candidates, ballots)
##
##winners = election_result.get_winners()
##print(election_result)
