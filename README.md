# Processing the HCRC Map Task Corpus
Utilities for Processing the [HCRC Map Task Corpus](http://groups.inf.ed.ac.uk/maptask/)
for the purpose of dialogue act (DA) classification.
The data has been randomly split, with the training set comprising 80% of the dialogues (102), and test and validation
sets 10% each (13). 50% of the training set is used as a development set (51).

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
Dialogue Act    |  Count
--- |  :---:
acknowledge | 5605
instruct    | 4267
reply_y     | 3230
explain     | 2160
check       | 2137
ready       | 2062
align       | 1778
query_yn    | 1758
clarify     | 1193
reply_w     | 916
reply_n     | 884
query_w     | 772

## Metadata
- Total number of utterances:  26762
- Max utterance length:  115
- Maximum dialogue length: 682
- Vocabulary size: 2189
- Number of labels: 12
- Number of dialogue in train set: 102
- Maximum length of dialogue in train set: 682
- Number of dialogue in test set: 13
- Maximum length of dialogue in test set: 292
- Number of dialogue in val set: 13
- Maximum length of dialogue in val set: 439
- Number of dialogue in dev set: 51
- Maximum length of dialogue in dev set: 682

### Keys and values for the metadata dictionary
- num_utterances = Total number of utterance in the full corpus.
- max_utterance_len = Number of words in the longest utterance in the corpus.
- max_dialogues_len = Number of utterances in the longest dialogue in the corpus.
- word_freq = Dictionary with {word : frequency} pairs.
- vocabulary = Full vocabulary - Gluon NLP [Vocabulary.](http://gluon-nlp.mxnet.io/api/modules/vocab.html#gluonnlp.Vocab)
- vocabulary_size = Number of words in the vocabulary.
- label_freq = Dictionary with {dialogue act label : frequency} pairs.
- labels = Full labels - Gluon NLP [Vocabulary.](http://gluon-nlp.mxnet.io/api/modules/vocab.html#gluonnlp.Vocab)
- num_labels = Number of labels used from the Maptask data.

Each data set also has:
- <*setname*>_num_dialogues = Number of dialogues in the set.
- <*setname*>_max_dialogues_len = Length of the longest dialogue in the set.