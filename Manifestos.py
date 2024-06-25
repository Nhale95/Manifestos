import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
import numpy as np
from matplotlib.lines import Line2D

# Download the stopwords corpus if not already done
nltk.download('stopwords')

def clean_text(text):
    """
    Remove special characters and digits from text, and convert to lowercase.
    """
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove special characters and digits
    text = text.lower()  # Convert to lowercase
    return text

def read_file(file_path):
    """
    Read the content of a text file and return as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main(file_path, min_length=1):
    """
    Read and clean the text from a file, and filter words by minimum length.
    """
    text = read_file(file_path)
    cleaned_text = clean_text(text).split()
    filtered_words = [word for word in cleaned_text if len(word) >= min_length]
    return filtered_words

def get_occurrences(words, topic):
    """
    Count the occurrences of topic-related words in the given list of words.
    """
    occurrences = 0
    for word in topics[topic]:
        occurrences += words.count(word)
    return occurrences

def add_row(txt_file, dataframe):
    """
    Add a row to the dataframe with word counts and topic-related word frequencies for a given text file.
    """
    words = main(txt_file)
   
    occurrences_immigration = get_occurrences(words, "Immigration")
    occurrences_ukraine = get_occurrences(words, "Ukraine-Russia")
    occurrences_brexit = get_occurrences(words, "Brexit")
    occurrences_israel = get_occurrences(words, "Israel-Palestine")
    occurrences_homes = get_occurrences(words, "Housing")
    occurrences_environment = get_occurrences(words, "Environment")
    
    # Create a new row as a dictionary
    new_row = {
        "party": txt_file.replace(".txt", ""),
        "Total words": len(words),
        "Immigration": occurrences_immigration * 1000 / len(words),
        "Ukraine-Russia": occurrences_ukraine * 1000 / len(words),
        "Brexit": occurrences_brexit * 1000 / len(words),
        "Israel-Palestine": occurrences_israel * 1000 / len(words),
        "Housing": occurrences_homes * 1000 / len(words),
        "Environment": occurrences_environment * 1000 / len(words)
    }
    df_template = dataframe.append(new_row, ignore_index=True)
    return df_template

# Define topics and related words
topics = {
    "Immigration": ["immigration","immigrant","immigrants", "migrants","migrant", "border", "asylum","refugees","refugee", "visa", "deportation", "boat","boats","rwanda"],
    "Ukraine-Russia": ["ukraine","ukranian","russia","putin","putin's"],
    "Brexit": ["brexit","eu"],
    "Israel-Palestine": ["israel","israeli","israelis","israel's","palestine","palestinian","palestine's","gaza","two-state"],
    "Housing": ["home","homes","house","housing","homeownership","rent","renter","renting","renters","mortgage","mortgages"],
    "Environment": ["decarbonise","emissions","environmental","environmentally","climate","warming","carbon","greenhouse","renewable","gases"]
}

# Define party colors
colors = {
    "Tory": "#013775",
    "Labour": "#ed1747",
    "Reform": "#2596be",
    "Libdems": "#f9a431",
    "Greens": "#00a85a",
    "SNP": "#fff482"
}

# Define the columns for the dataframe
columns = ["party", "Total words", "Immigration", "Ukraine-Russia", "Brexit", "Israel-Palestine", "Housing", "Environment"]

# Initialize an empty DataFrame with the defined columns
df_template = pd.DataFrame(columns=columns)
parties = ["Tory", "Labour", "Reform", "Libdems", "Greens", "SNP"]

# Add rows to the dataframe for each party
for party in parties:
    df_template = add_row(party + ".txt", df_template)

# Plot settings
fig1, ax1 = plt.subplots(1, figsize=(25, 12), dpi=300, facecolor='#2e2e2e')
fontsize = 20

# Set bar plot parameters
x = np.arange(len(parties))  # the label locations
width = 1  # the width of the bars

# Initialize the offset for bar positions
offset = 0
for topic in list(topics.keys()):
    x = np.arange(len(parties)) + (len(parties) + 2) * offset
    rects = ax1.bar(x, df_template[topic], width, label=topic, color=[colors[party] for party in df_template["party"]])
    offset += 1

# Create a list of Line2D objects for the legend
legend_elements = [Line2D([0], [0], color=colors[party], lw=12, label=party) for party in parties]

# Add legend to the plot
legend = ax1.legend(handles=legend_elements, 
                    framealpha=0.0,
                    fontsize=fontsize + 9,
                    bbox_to_anchor=(0.504, 1.07), 
                    loc='center', 
                    ncol=len(parties), 
                    handletextpad=0.85,   # Increase spacing between the legend symbol and text
                    columnspacing=3.6) 

# Set the legend text color to white
for text in legend.get_texts():
    text.set_color("white")

# Calculate x-ticks positions
start_value = 3
spacing = 8
num_values = 6
values = np.arange(start_value, start_value + num_values * spacing, spacing)

# Set x-ticks and labels
ax1.set_xticks(values)
ax1.set_xticklabels(list(topics.keys()), fontsize=fontsize + 15, color='white')
ax1.set_facecolor('#2e2e2e')

# Customize the ticks and labels
ax1.tick_params(axis='x', which='major', labelsize=fontsize + 15, colors='white')
ax1.tick_params(axis='y', which='major', labelsize=fontsize + 15, colors='white')

# Set axis labels and title
ax1.set_ylabel("Number of topic-specific words used\n per 1000 words in party manifesto", fontsize=fontsize + 17, labelpad=35, color='white')
ax1.set_xlabel("Topics", fontsize=fontsize + 17, labelpad=25, color='white')

#make figure title
ax1.text(0.02,1.17,"What UK Political Parties Emphasise in Their Manifestos?",  color = "white",  transform=ax1.transAxes,fontsize =fontsize+31)

# Customize the plot aesthetics
ax1.spines['top'].set_color('#444444')
ax1.spines['bottom'].set_color('#444444')
ax1.spines['left'].set_color('#444444')
ax1.spines['right'].set_color('#444444')

# Set the color of the plot background and figure background
ax1.patch.set_alpha(0.7)
fig1.patch.set_alpha(0.7)

#set source text
ax1.text(-0.09,-0.18,"Source: UK party manifestos taken from party websites", transform=ax1.transAxes,fontsize =fontsize  -3, color='white')

ax1.set_xlim(-1, num_values * spacing-2)
# Adjust the layout of the plot
fig1.subplots_adjust(left=0.095, bottom=0.14, right=0.97, top=0.8)

# Save the figure
fig1.savefig("Manifestos.png", dpi=300, facecolor=fig1.get_facecolor())
