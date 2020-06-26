# Processing the HCRC Map Task Corpus
Utilities for Processing the [HCRC Map Task Corpus](http://groups.inf.ed.ac.uk/maptask/)
for the purpose of dialogue act (DA) classification.
The data has been randomly split, with the training set comprising 80% of the dialogues (102), and test and validation
sets 10% each (13).

## Scripts
The maptask_to_text.py script processes all dialogues into a plain text format.
Individual dialogues are saved into directories corresponding to the set they belong to (train, test, etc).
All utterances in a particular set are also saved to a text file.

The maptask_utilities.py script contains various helper functions for loading/saving the data.
 
The process_transcript.py includes functions for processing each dialogue.

The maptask_metadata.py generates various metadata from the processed dialogues and saves them as a dictionary to a pickle file.
The words, labels and frequencies are also saved as plain text files in the /metadata directory.

## Data Format
Utterance are tagged with the [Maptask Coding Scheme](http://groups.inf.ed.ac.uk/maptask/interface/expl.html) for DA.

By default:
- Utterances are written one per line in the format *Speaker* | *Utterance Text* | *Dialogue Act Tag*.
- Setting the utterance_only_flag == True, will change the default output to only one utterance per line i.e. no speaker or DA tags.
- Utterances marked as *Uncodable* ('uncodable' tag) are removed.

### Example Utterances
g|okay|ready

g|starting off we are above a caravan park|instruct

f|mmhmm|acknowledge

## Dialogue Acts
Dialogue Act                   |        Labels        |  Count   |    %     |   Train Count   | Train %  |   Test Count    |  Test %  |    Val Count    |  Val %  
--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
Acknowledge                    |     acknowledge      |   5605   |  20.94   |      4433       |  21.04   |       527       |  20.29   |       645       |  20.82  
Instruct                       |       instruct       |   4267   |  15.94   |      3390       |  16.09   |       417       |  16.06   |       460       |  14.85  
Yes-Reply                      |       reply_y        |   3230   |  12.07   |      2530       |  12.01   |       304       |  11.71   |       396       |  12.78  
Explain                        |       explain        |   2160   |   8.07   |      1669       |   7.92   |       219       |   8.43   |       272       |   8.78  
Check                          |        check         |   2137   |   7.99   |      1683       |   7.99   |       232       |   8.93   |       222       |   7.17  
Ready                          |        ready         |   2062   |   7.70   |      1559       |   7.40   |       222       |   8.55   |       281       |   9.07  
Check Attention                |        align         |   1778   |   6.64   |      1444       |   6.85   |       130       |   5.01   |       204       |   6.58  
Yes-No-Question                |       query_yn       |   1758   |   6.57   |      1350       |   6.41   |       191       |   7.35   |       217       |   7.00  
Clarify                        |       clarify        |   1193   |   4.46   |       970       |   4.60   |       116       |   4.47   |       107       |   3.45  
Non Yes-No-Reply               |       reply_w        |   916    |   3.42   |       729       |   3.46   |       83        |   3.20   |       104       |   3.36  
No-Reply                       |       reply_n        |   884    |   3.30   |       692       |   3.28   |       101       |   3.89   |       91        |   2.94  
Non Yes-No-Question            |       query_w        |   772    |   2.88   |       618       |   2.93   |       55        |   2.12   |       99        |   3.20  

![Label Frequencies](maptask_data/metadata/Maptask%20Label%20Frequency%20Distributions.png)

## Metadata
- Total number of utterances:  26762
- Maximum utterance length:  115
- Mean utterance length: 6.2
- Total number of dialogues: 128
- Maximum dialogue length: 682
- Mean dialogue length: 209
- Vocabulary size: 2189
- Number of labels: 12
- Number of dialogue in train set: 102
- Maximum length of dialogue in train set: 682
- Number of dialogue in test set: 13
- Maximum length of dialogue in test set: 292
- Number of dialogue in val set: 13
- Maximum length of dialogue in val set: 439

### Keys and values for the metadata dictionary
- num_utterances = Total number of utterance in the full corpus.
- max_utterance_len = Number of words in the longest utterance in the corpus.
- mean_utterance_len = Average number of words in utterances.
- num_dialogues = Total number of dialogues in the corpus.
- max_dialogues_len = Number of utterances in the longest dialogue in the corpus.
- mean_dialogues_len = Average number of utterances in dialogues.
- word_freq = Dictionary with {word : frequency} pairs.
- vocabulary = Full vocabulary - Gluon NLP [Vocabulary.](http://gluon-nlp.mxnet.io/api/modules/vocab.html#gluonnlp.Vocab)
- vocabulary_size = Number of words in the vocabulary.
- label_freq = [Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) containing all data in the Dialogue Acts table above.
- labels = Full labels - List of all DA labels.
- num_labels = Number of labels used from the Maptask data.

Each data set also has:
- <*setname*>_num_dialogues = Number of dialogues in the set.
- <*setname*>_max_dialogues_len = Length of the longest dialogue in the set.