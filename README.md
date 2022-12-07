# RankedChoiceVoting
1) Prepare an excel file with the votes (follow the format of `data/testData.xlxs`)
2) Run `python3 getWinners.py` and then select the voting data via file browser.

```
Usage: getWinners.py [-h] [-n NUMBEROFCAPTAINS]

Run STV vote for n captains

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBEROFCAPTAINS, --numberOfCaptains NUMBEROFCAPTAINS
                        The number of captains that you would like to elect.
```

## Dependencies:
- https://pypi.org/project/pyrankvote/ by Jon Tingvold
- tkinter
- pandas
- python3
