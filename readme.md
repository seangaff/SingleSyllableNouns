# Find Single Syllable Nouns

This is a simple script to find single syllable nouns in an Excel Spreadsheet. 

Data is sourced from [wordfreqency.info](https://www.wordfrequency.info/samples.asp) where you can download a list of the top 5000 most freqent used English words. Wordfrequency.info uses  uses the [COCA dataset](https://www.english-corpora.org/coca/).

The [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict?in=C+M+U+Dictionary) is used to check the number of syllables in a word.

## Usage

Python 3.x is required to run this script. (Tested with 3.11)

1. Clone or download this repository

2. Download the top 5000 most frequent English words from [wordfreqency.info](https://www.wordfrequency.info/samples.asp) in Excel format and add it to the root of this repository. If you want to use a different list of words/lemmas, you can change the file name in the script.

3. Install the required packages

```pip install pandas openpyxl cmudict```

4. Run the script

```python findwords.py```

5. The output will be save in a file titled ```nouns1syll.xlsx```