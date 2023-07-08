# Text Retrieval & Search Engine (CP423)

### Assignment 2 - Group 6 Submission

## Members:
- Gadd, Bryan

- Jain, Maheep

- Khamphavong, Osaka

- Simion, Alexandra

Due Date/Submission Date: July 9th, 2023, 11:59pm

## Summary:
To-Do

## Requirments:
To run this project you will need to run the following command to install the required modules/libraries:

pip install -r .\requirements.txt

## Summary of files:
### Q1.
Contains the positional index data structure along with preprocessing function and phrase queries functions.

In phrase queries function we made an assumption that the user want to search for phrase that exist within the documents so the input would take a phrase and then the output would show in format: (docID, {docID: [position of the word]}) (the position would be in an order because each word needs to be next to each other). If user enter phrase that does not exist in the document it will return empty result. 

### Q2.
Contains the TF, TF-IDF, and Cosine similarity functions.

Any assumptions?

## How to run the program:
1. Refer to Requirements to install the required libraries.
2. Run Main.py.
3. You will be prompted to enter which function you want to run (or exit the program):
    - 0 = Exit
    - 1 = Phrase query
    - 2 = TF-IDF
    - 3 = Cosine Similatiry
    - Enter a number and press enter to select the function (or exit the program).
4. After picking the function you will be prompted to enter the query. Enter the query and press enter.
5. At this point phrase query will process and output the result. If TF-IDF or Cosine Similatiry was picked then you will be asked to pick which weight scheme to use.
    - 1 = Binary
    - 2 = Raw Count
    - 3 = Term Frequency
    - 4 = Log Normalization
    - 5 = Double Normalization
    - Enter a number and press enter to select the weight schemna. Once processed the results are outputed.
6. Once the selected function outputs its results you will return to step 3 where you can pick another function to run or exit the program.

## Program Example:
To-Do
