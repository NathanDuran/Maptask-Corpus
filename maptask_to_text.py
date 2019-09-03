import os
from maptask_utilities import *
import process_transcript as process

# Switchboard archive directory
archive_dir = 'maptask_archive'

# Processed data directory
data_dir = 'maptask_data/'

# Metadata directory
metadata_dir = os.path.join(data_dir, 'metadata')

# If flag is set will only write utterances and not speaker or DA label
utterance_only_flag = False

# Files for all the utterances in the corpus and data splits
full_set_file = "full_set"
train_set_file = "train_set"
test_set_file = "test_set"
val_set_file = "val_set"
dev_set_file = "dev_set"

# Remove old files if they exist, so we do not append to old data
remove_file(data_dir, full_set_file, utterance_only_flag)
remove_file(data_dir, train_set_file, utterance_only_flag)
remove_file(data_dir, test_set_file, utterance_only_flag)
remove_file(data_dir, val_set_file, utterance_only_flag)
remove_file(data_dir, dev_set_file, utterance_only_flag)

# Get a list of all the transcript files
transcripts_list = os.listdir(os.path.join(archive_dir, 'transcripts'))

# Split into training, validation, test  and development sets
train_split, val_split, test_split, dev_split = split_sets(metadata_dir, transcripts_list, train_set_split=0.8)
print(len(transcripts_list))
print(transcripts_list)
print(len(train_split))
print(len(val_split))
print(len(test_split))
print(len(dev_split))