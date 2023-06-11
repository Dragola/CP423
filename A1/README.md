# Text Retrieval & Search Engine (CP423)

### Assignment 1 - Group 6 Submission

## Members:
- Gadd, Bryan

- Jain, Maheep

- Khamphavong, Osaka

- Simion, Alexandra

Due Date/Submission Date: June 11th, 2023, 11:59pm

## Summary:
The purpose of this assignment was to create a functioning program to run queries against a dataset in Python. This involved preprocessing the data, implementing an inverted index data structure, taking input from the user, implementing a combination of 'OR', 'AND', & 'NOT' operations for the queries, testing the code for errors, and running a set of queries that return data from the dataset. 

## Requirments:
To run this project you will need to run the following command to install the required modules/libraries:

pip install -r .\requirements.txt

## Summary of files:
### Q1.
Contains the tokenization code. The function take some text (aka string) as input, tokenizes it, and outputs a unique list of workds/tokens. We use this function to process the input sentence and text in the data documents in Q4.

### Q2.
Holds the InvertedIndex class. This class is used to store the tokens and their posting lists in a dictionary list. A dictionary list was used to provide speedy indexing + easier locating of index's. It contains a few methods to add/updated and index, and print the index list (for debugging).

### Q3.
Contains the query processing code. There are 2 functions:
- The first take a query (string) and checks the format. We use this in Q4 before running the query.
- The second takes a query (string), the inverted index, and the total number of documents to processes the query. Once complete, the function returns a new posting list and the total number of comparisons required to create the new posting list. We use this in Q4 to process the query(s) and output the results.

### Q4.
The main file that handles the input and output of the program. This file uses the methods in the other 3 files.

The video demo focuses on Q4 since this file handles both the input and output.

## How to run the program:
1. Install the required libraries/modules (refer to instruction above).
2. Run Q4.py.
3. You will be prompted to ender the number of quieries your want to run. Enter a number and press enter.
4. Next, you will be asked to enter the sentence for the query. Enter your sentence and press enter.
    - Example: lion stood thoughtfully for a moment.
    - Note: DO NOT ENTER "" around the sentence. Just enter the sentence only.
5. Finally, you will be asked to enter the operators. Make sure they are all uppercase and are seperated by comma's.
    - Example: OR, AND, OR NOT, AND NOT. 
    - Note: DO NOT ENTER brackets '[]'. Only enter the operators and seperate using comma's.
6. Wait for query output.
    - Note: Will take about 20 seconds or more to run the first query as the inverted index has to be generated. This process involves reading and processing all the data files so the more data you have the longer it will take to process and store.
7. Repeat Steps 4-6 if the number of queries is greater then 1.

## Example:

```
How many queries are you running? 1
Query #1:
Input Sentence: lion stood thoughtfully for a moment
Input operation sequence: OR, OR, OR

Expected preprocessed query: lion OR stood OR thoughtfully OR moment

Output:
Number of matched documents: 239
Minimum number of comparisons required: 475
List of retrieved document names
13chil.txt | ID= 2
3gables.txt | ID= 3
3gables.txt | ID= 3
3lpigs.txt | ID= 4
3student.txt | ID= 5
3student.txt | ID= 5
4moons.txt | ID= 7
5orange.txt | ID= 8
5orange.txt | ID= 8
6napolen.txt | ID= 10
6napolen.txt | ID= 10
6napolen.txt | ID= 10
7voysinb.txt | ID= 12
7voysinb.txt | ID= 12
ab40thv.txt | ID= 13
abbey.txt | ID= 14
abbey.txt | ID= 14
abbey.txt | ID= 14
advsayed.txt | ID= 17
adv_alad.txt | ID= 19
aesop11.txt | ID= 20
aesop11.txt | ID= 20
aesop11.txt | ID= 20
aesopa10.txt | ID= 21
aesopa10.txt | ID= 21
aesopa10.txt | ID= 21
aislesix.txt | ID= 23
alad10.txt | ID= 24
angry_ca.txt | ID= 27
aquith.txt | ID= 29
aquith.txt | ID= 29
arctic.txt | ID= 30
arctic.txt | ID= 30
beautbst.txt | ID= 34
beggars.txt | ID= 35
bgcspoof.txt | ID= 38
bishop00.txt | ID= 39
bishop00.txt | ID= 39
blabnove.txt | ID= 40
blackp.txt | ID= 41
blackp.txt | ID= 41
blh.txt | ID= 42
blh.txt | ID= 42
blind.txt | ID= 43
blind.txt | ID= 43
bluebrd.txt | ID= 44
bruce-p.txt | ID= 45
bruce-p.txt | ID= 45
bruce-p.txt | ID= 45
buggy.txt | ID= 46
buldream.txt | ID= 48
buldream.txt | ID= 48
bulfelis.txt | ID= 49
bulmrx.txt | ID= 53
bulolli1.txt | ID= 56
bulolli2.txt | ID= 57
bulphrek.txt | ID= 58
bulphrek.txt | ID= 58
bulprint.txt | ID= 59
bulzork1.txt | ID= 60
bulzork1.txt | ID= 60
bureau.txt | ID= 61
bureau.txt | ID= 61
cardcnt.txt | ID= 64
cardcnt.txt | ID= 64
cmoutmou.txt | ID= 68
cooldark.txt | ID= 69
cooldark.txt | ID= 69
cybersla.txt | ID= 71
cybersla.txt | ID= 71
cybersla.txt | ID= 71
darkness.txt | ID= 73
darkness.txt | ID= 73
deer.txt | ID= 74
diaryflf.txt | ID= 75
diaryflf.txt | ID= 75
dopedenn.txt | ID= 79
dskool.txt | ID= 80
dskool.txt | ID= 80
dtruck.txt | ID= 81
emperor3.txt | ID= 83
emperor3.txt | ID= 83
empnclot.txt | ID= 84
empty.txt | ID= 86
empty.txt | ID= 86
enginer.txt | ID= 88
enginer.txt | ID= 88
enginer.txt | ID= 88
enya_trn.txt | ID= 89
fantasy.txt | ID= 92
fantasy.txt | ID= 92
fgoose.txt | ID= 93
fgoose.txt | ID= 93
fish.txt | ID= 94
floobs.txt | ID= 97
flytrunk.txt | ID= 99
foxncrow.txt | ID= 100
foxngrap.txt | ID= 101
fred.txt | ID= 103
fred.txt | ID= 103
friends.txt | ID= 104
friends.txt | ID= 104
game.txt | ID= 106
game.txt | ID= 106
girlclub.txt | ID= 109
girlclub.txt | ID= 109
gold3ber.txt | ID= 112
goldenp.txt | ID= 113
goldenp.txt | ID= 113
goldfish.txt | ID= 114
goldgoos.txt | ID= 115
graymare.txt | ID= 116
graymare.txt | ID= 116
greedog.txt | ID= 117
gulliver.txt | ID= 118
gulliver.txt | ID= 118
hareporc.txt | ID= 121
hareporc.txt | ID= 121
haretort.txt | ID= 122
healer.txt | ID= 123
healer.txt | ID= 123
hellmach.txt | ID= 125
hellmach.txt | ID= 125
hellmach.txt | ID= 125
history5.txt | ID= 127
history5.txt | ID= 127
hitch2.txt | ID= 128
hitch2.txt | ID= 128
hitch3.txt | ID= 129
hitch3.txt | ID= 129
hitch3.txt | ID= 129
holmesbk.txt | ID= 131
horswolf.txt | ID= 133
hotline1.txt | ID= 134
hotline3.txt | ID= 135
hound-b.txt | ID= 137
hound-b.txt | ID= 137
hound-b.txt | ID= 137
jackbstl.txt | ID= 139
keepmodu.txt | ID= 140
keepmodu.txt | ID= 140
knuckle.txt | ID= 143
knuckle.txt | ID= 143
lament.txt | ID= 145
lament.txt | ID= 145
lgoldbrd.txt | ID= 146
lionmane.txt | ID= 148
lionmane.txt | ID= 148
lionmane.txt | ID= 148
lionmosq.txt | ID= 149
lionmosq.txt | ID= 149
lionwar.txt | ID= 150
lionwar.txt | ID= 150
lionwar.txt | ID= 150
lionwar.txt | ID= 150
lmtchgrl.txt | ID= 152
long1-3.txt | ID= 153
long1-3.txt | ID= 153
lrrhood.txt | ID= 155
lure.txt | ID= 156
mattress.txt | ID= 158
mazarin.txt | ID= 159
mazarin.txt | ID= 159
mazarin.txt | ID= 159
mcdonaldl.txt | ID= 160
missing.txt | ID= 164
missing.txt | ID= 164
monkking.txt | ID= 166
monkking.txt | ID= 166
mouslion.txt | ID= 168
mtinder.txt | ID= 169
musgrave.txt | ID= 170
musgrave.txt | ID= 170
paink-ws.txt | ID= 177
paink-ws.txt | ID= 177
pepdegener.txt | ID= 181
pinocch.txt | ID= 182
plescopm.txt | ID= 183
poplstrm.txt | ID= 187
poplstrm.txt | ID= 187
pphamlin.txt | ID= 188
pregn.txt | ID= 189
psf.txt | ID= 190
pussboot.txt | ID= 191
radar_ra.txt | ID= 192
radar_ra.txt | ID= 192
rainda.txt | ID= 193
redragon.txt | ID= 195
retrib.txt | ID= 196
roger1.txt | ID= 198
roger1.txt | ID= 198
roger1.txt | ID= 198
running.txt | ID= 199
running.txt | ID= 199
running.txt | ID= 199
shoscomb.txt | ID= 201
shoscomb.txt | ID= 201
shulk.txt | ID= 203
sick-kid.txt | ID= 204
sick-kid.txt | ID= 204
sick-kid.txt | ID= 204
sight.txt | ID= 205
silverb.txt | ID= 206
silverb.txt | ID= 206
sleprncs.txt | ID= 207
sleprncs.txt | ID= 207
snowmaid.txt | ID= 208
snowqn1.txt | ID= 209
socialvikings.txt | ID= 210
solitary.txt | ID= 211
solitary.txt | ID= 211
solitary.txt | ID= 211
space.txt | ID= 212
spiders.txt | ID= 214
sqzply.txt | ID= 215
sre-dark.txt | ID= 216
taxnovel.txt | ID= 222
tcoa.txt | ID= 223
tcoa.txt | ID= 223
tearglas.txt | ID= 225
tearglas.txt | ID= 225
timetrav.txt | ID= 229
tree.txt | ID= 232
unluckwr.txt | ID= 234
vainsong.txt | ID= 236
veiledl.txt | ID= 238
veiledl.txt | ID= 238
veiledl.txt | ID= 238
vgilante.txt | ID= 239
vgilante.txt | ID= 239
vgilante.txt | ID= 239
wisteria.txt | ID= 242
wisteria.txt | ID= 242
wlgirl.txt | ID= 243
wlgirl.txt | ID= 243
yukon.txt | ID= 247
yukon.txt | ID= 247
zombies.txt | ID= 248
zombies.txt | ID= 248
```