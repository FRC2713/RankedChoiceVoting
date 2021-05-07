# -*- coding: utf-8 -*-
"""
Created on Tue May 19 07:28:25 2020

@author: ssainis
"""


import pyrankvote
from pyrankvote import Candidate, Ballot

#import pyRankVoteTest
#from pyRankVoteTest import Candidate, Ballot

bush = Candidate("George W. Bush (Republican)")
gore = Candidate("Al Gore (Democratic)")
nader = Candidate("Ralph Nader (Green)")

candidates = [bush, gore, nader]

# Bush have most first choice votes, but because Ralph Nader-voters want
# Al Gore if Nader is not elected, the elected candidate is Al Gore
ballots = [
    Ballot(ranked_candidates=[bush, nader, gore]),
    Ballot(ranked_candidates=[bush, nader, gore]),
    Ballot(ranked_candidates=[bush, nader]),
    Ballot(ranked_candidates=[bush, nader]),
    Ballot(ranked_candidates=[nader, gore, bush]),
    Ballot(ranked_candidates=[nader, gore]),
    Ballot(ranked_candidates=[gore, nader, bush]),
    Ballot(ranked_candidates=[gore, nader]),
    Ballot(ranked_candidates=[gore, nader])
]

# You can use your own Candidate and Ballot objects as long as they implement the same properties and methods
election_result = pyrankvote.instant_runoff_voting(candidates, ballots)

winners = election_result.get_winners()
# Returns: [<Candidate('Al Gore (Democratic)')>]

print(election_result)