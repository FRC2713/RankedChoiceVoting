# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:28:01 2020

@authors: ssainis, pmartel

uses https://pypi.org/project/pyrankvote/ by Jon Tingvold
Modifying to extract candiate data from vote file
"""
import math
from tkinter import filedialog
from pyrankvote import Candidate, Ballot
from multiple_seat_ranking_methods import *
from pyrankvote.helpers import CompareMethodIfEqual, ElectionManager, ElectionResults
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Run STV vote for n captains")
parser.add_argument("-n", "--numberOfCaptains", help="The number of captains that you would like to elect.",default=3)


# get name of vote file
def  getFileName():
    
    fd = filedialog

    fileName = fd.askopenfilename(title = 'Select vote file',
                                  filetypes=[('Excel file','*.xlsx'),
                                             ('All files','*.*')])
    return fileName

# run the election for the given number of captains to elect
def runElection(numberOfCaptains):
    status = 'ok'
    fileName =getFileName()


    if fileName == '' :
        return 'Error: no file selected'
    else :
        try:
            df = pd.read_excel( fileName )
        except ValueError:
            return 'Error: File ' + fileName + 'is not an Excel file'
        else :
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

            candidateList = []
            candidateName = []
            for c in cSet :
                # treat nil/nan as a special case
                if type(c) != type(1.) :  # this traps Not a Number
                    candidateList.append(Candidate(c))
                    candidateName.append(c)
            
            print("\ncandidates")
            print( candidateName )

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
                        continue #k
                    continue #j
                
                ballots.append(Ballot(ranked_candidates = voter_ranking))  
                    
            print( "\nFound {} ballots".format(len(ballots)))
            # for b in ballots:
            #     print(b)

        election_result =\
        single_transferable_vote(
        candidates = candidateList,
        ballots = ballots,
        number_of_seats = numberOfCaptains )
        
        winners = election_result.get_winners()
        print(election_result)

        return "OK"


## This runs if this code is run as a script
if __name__ == "__main__":
    status = 'OK'

    args = parser.parse_args()
    try:
        numberOfCaptains = int(args.numberOfCaptains)
        if numberOfCaptains <= 0 :
            status = 'Error: invalid number of captains to elect.'
        else :
            status = runElection(numberOfCaptains)

    except ValueError:
        status = 'Error: must provide a number of captains to elect.'

    print(status)
    
