# UK Political Party Manifesto Analysis

This Python script analyzes the manifestos of various UK political parties, focusing on the frequency of words related to specific topics such as Immigration, Ukraine-Russia, Brexit, Israel-Palestine, Housing, and Environment. The results are visualized in a bar plot.

## Prerequisites

Ensure you have the following Python packages installed:

- `re`
- `nltk`
- `matplotlib`
- `pandas`
- `numpy`

You can install the necessary packages using pip:

```bash
pip install nltk matplotlib pandas numpy
```

## Setup

Before running the script, ensure you have the NLTK stopwords corpus downloaded. You can download it by running the following command:

```python
import nltk
nltk.download('stopwords')
```

## Usage

1. **Prepare Text Files**: Ensure you have text files for each political party's manifesto. The filenames should be in the format: `[party].txt`, where `[party]` can be `Tory`, `Labour`, `Reform`, `Libdems`, `Greens`, or `SNP`.

2. **Run the Script**: Execute the script to analyze the manifestos and generate a bar plot.

```bash
python manifesto_analysis.py
```

3. **Output**: The script will save a figure named `Manifestos.png` that visualizes the frequency of topic-specific words used in each party's manifesto.

## Script Details

- **`clean_text(text)`**: Removes special characters and digits from the text and converts it to lowercase.
- **`read_file(file_path)`**: Reads the content of a text file and returns it as a string.
- **`main(file_path, min_length=1)`**: Cleans the text from a file and filters words by minimum length.
- **`get_occurrences(words, topic)`**: Counts the occurrences of topic-related words in the given list of words.
- **`add_row(txt_file, dataframe)`**: Adds a row to the dataframe with word counts and topic-related word frequencies for a given text file.

### Topics and Related Words

The script defines specific words related to various topics:
- **Immigration**: ["immigration", "immigrant", "immigrants", "migrants", "migrant", "border", "asylum", "refugees", "refugee", "visa", "deportation", "boat", "boats", "rwanda"]
- **Ukraine-Russia**: ["ukraine", "ukranian", "russia", "putin", "putin's"]
- **Brexit**: ["brexit", "eu"]
- **Israel-Palestine**: ["israel", "israeli", "israelis", "israel's", "palestine", "palestinian", "palestine's", "gaza", "two-state"]
- **Housing**: ["home", "homes", "house", "housing", "homeownership", "rent", "renter", "renting", "renters", "mortgage", "mortgages"]
- **Environment**: ["decarbonise", "emissions", "environmental", "environmentally", "climate", "warming", "carbon", "greenhouse", "renewable", "gases"]

### Plot Settings

- The script generates a bar plot with each bar representing the frequency of topic-specific words used per 1000 words in the party manifestos.
- The legend at the top of the plot indicates the political parties, with their respective colors.
- The x-axis shows the different topics, and the y-axis shows the number of topic-specific words used per 1000 words in the party manifesto.

