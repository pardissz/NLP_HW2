"""
Crawled from https://shadima.com/%D8%A7%D8%B3%D9%85-%D9%BE%D8%B3%D8%B1/
Thanks!!
"""

# Open the file
with open('Girls.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove all spaces from the text while keeping the tabs
new_text = text.replace(' ', '')

# Write the new text back to the file
with open('Modified_Girls.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)
with open('Modified_Girls.txt', 'r', encoding='utf-8') as f:
    lines_women = f.readlines()
with open('Boys.txt', 'r', encoding='utf-8') as f:
    lines_men = f.readlines()

# Extract the first word from each line
words_men = [line.split("\t")[0] for line in lines_men]
words_women = [line.split("\t")[0] for line in lines_women]

import re


def extract_names(text, women_names, men_names):
    full_names = []
    words = text.split()
    women_prefixes = ['خانم','مهندس','دکتر','استاد']
    men_prefixes = ['آقای','آقا','دکتر','استاد','مهندس','جناب']
    all_prefixes = women_prefixes + men_prefixes
    i = 0
    while i < len(words):
        if words[i].lower() in women_prefixes:
            if i < len(words) - 1 and words[i+1].lower() not in all_prefixes:
                if words[i+1].lower() in women_names:
                    if i < len(words) - 2:
                        full_names.append(words[i] + ' ' + words[i+1] + ' ' + words[i+2])
                        i += 1
                    else:
                        full_names.append(words[i] + ' ' + words[i+1])
                else:
                    full_names.append(words[i] + ' ' + words[i+1])
        elif words[i].lower() in men_prefixes:
            if i < len(words) - 1 and words[i+1].lower() not in all_prefixes:
                if words[i+1].lower() in men_names:
                    if i < len(words) - 2:
                        full_names.append(words[i] + ' ' + words[i+1] + ' ' + words[i+2])
                        i += 1
                    else:
                        full_names.append(words[i] + ' ' + words[i+1])
                else:
                    full_names.append(words[i] + ' ' + words[i+1])
        elif words[i].lower() in women_names or words[i].lower() in men_names:
            full_names.append(words[i])
        i += 1

    return full_names
text = "به المیرا و سوسن بگو آقای علی مردانی و دکتر پردیس مومنی و آقای مهندس فراهانی هم هست مهندس نیکبخت دوستش دارم و آقای مهدی علیزاده چون خانم لوزیانی هم زنگ زده است و خانم دکتر زهرایی هم خوب اند"
full_names=extract_names(text, words_women, words_men)
me_prounoun=['من','می کنم','می‌کنم','می دهم','میدهم']
you_prounoun=['تو','برو','بکن','بخر','بده']
words = text.split()
if not full_names:
    for word in words:
        if word.lower() in me_prounoun:
            full_names.append("گوینده")
            break
        if word.lower() in you_prounoun:
            full_names.append("شنونده")
            break
if not full_names:
    full_names.append("نامعلوم")
print(full_names)