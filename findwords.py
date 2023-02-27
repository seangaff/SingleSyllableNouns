# Required libraries:
import pandas as pd
import cmudict

# Import CMU Pronouncing Dictionary
d = cmudict.dict()

# Check if a word has one syllable
def if1syll(word):
  var = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]] 
  return max(var) if var else 0

# Import Frequency List
df = pd.read_excel("lemmas_60k.xlsx")
df = df.drop(["rank", "perMil", "%caps", "webPM", "TVMPM", "spokPM", "ficPM", "magPM", "newsPM", "acadPM", "%allC", "range", "disp", "blog", "web", "TVM", "spok", "fic", "mag", "news", "acad", "blogPM"], axis=1)

# Filter the dataframe to include only nouns
nouns_df = df[df["PoS"] == "n"]

# Sort the dataframe by frequency
nouns_sorted = nouns_df.sort_values("freq", ascending=False)

# Filter the dataframe to include only words with one syllable
nouns_1syll = nouns_sorted[nouns_sorted["lemma"].apply(lambda x: if1syll(x) == 1)]

# res = nouns_1syll.head(1000)

# Export the dataframe to an Excel file
nouns_1syll.to_excel("nouns1syll.xlsx", index=False)


