import os
import re

labels_by_episode = {}
script_loc = os.getcwd()

os.chdir(script_loc + "/abgt_201")  # before: abgt_tracklists

all_txt_files = os.listdir(os.getcwd())

# Generate a list of ABGT episodes so we can use it later to open files
base = "abgt"
episodes = []
for ep in range(201, 221):  # before: 163, 197
    episodes.append(base + str(ep))

def find_labels_in_text(text):
    pattern = r"\(.+\)"
    labels = re.findall(pattern, text)
    return labels


for item in episodes:
    filename = item + ".txt"
    f = open(filename)
    txt = f.read()
    f.close()

    music_labels = find_labels_in_text(txt)
    labels_by_episode[item] = music_labels

total_mentions = {}

for episode in labels_by_episode:
    for i in labels_by_episode[episode]:
        if i not in total_mentions:
            total_mentions[i] = 1
        else:
            total_mentions[i] += 1

labels_by_rank = sorted(total_mentions.items(), key=lambda x: x[1])


f = open("MOST_PLAYED_LABELS_201_219.txt", "w")
for label, totals in labels_by_rank:
    f.write(label + " " + str(totals) + "\n")
f.close()



