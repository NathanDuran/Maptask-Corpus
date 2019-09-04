import os
import random
import pickle


def split_sets(output_dir, transcript_list, train_set_split=0.8):
    random.seed(42)

    # Calculate number of transcripts in each set
    num_train = int(len(transcript_list) * train_set_split)
    num_val = int((len(transcript_list) - num_train) / 2)
    num_test = len(transcript_list) - num_train - num_val
    num_dev = int(num_train / 2)

    # Randomise the transcripts
    random.shuffle(transcript_list)

    # Select the number of training and dev transcripts
    train_indices = random.sample(range(len(transcript_list)), num_train)
    train_split = [transcript_list[i].split('.')[0] for i in range(len(transcript_list)) if i in train_indices]
    dev_split = random.sample(train_split, num_dev)
    # Remove from transcript list so we don't select again
    for index in sorted(train_indices, reverse=True):
        del transcript_list[index]

    # Select the number of test and validation transcripts
    test_indices = random.sample(range(len(transcript_list)), num_test)
    test_split = [transcript_list[i].split('.')[0] for i in range(len(transcript_list)) if i in test_indices]
    val_split = [transcript_list[i].split('.')[0] for i in range(len(transcript_list)) if i not in test_indices]

    # Ensure no data is in more than one set
    if any(el in test_split for el in train_split):
        print("Train split has elements from test split!")
    if any(el in val_split for el in train_split):
        print("Train split has elements from validation split!")
    if any(el in test_split for el in val_split):
        print("Test split has elements from validation split!")

    # Save to file
    save_text_data(os.path.join(output_dir, 'train_split.txt'), train_split)
    save_text_data(os.path.join(output_dir, 'val_split.txt'), val_split)
    save_text_data(os.path.join(output_dir, 'test_split.txt'), test_split)
    save_text_data(os.path.join(output_dir, 'dev_split.txt'), dev_split)

    return train_split, val_split, test_split, dev_split


def save_text_data(path, data, verbose=False):
    with open(path, "w") as file:
        for i in range(len(data)):
            file.write(data[i] + "\n")
    if verbose:
        print("Saved data to file %s." % path)


def load_text_data(path, verbose=False):
    with open(path, "r") as file:
        # Read a line and strip newline char
        lines = [line.rstrip('\r\n') for line in file.readlines()]
    if verbose:
        print("Loaded data from file %s." % path)
    return lines


def save_data_pickle(path, data, verbose=True):
    with open(path, "wb") as file:
        pickle.dump(data, file, protocol=2)
    if verbose:
        print("Saved data to file %s." % path)


def dialogue_to_file(path, dialogue, utterance_only, write_type):
    if utterance_only:
        path = path + "_utt"
    with open(path + ".txt", write_type) as file:
        for utterance in dialogue.utterances:
            if utterance_only:
                file.write(utterance.text.strip() + "\n")
            else:
                file.write(utterance.speaker + "|" + utterance.text.strip() + "|" + utterance.da_label + "\n")


def remove_file(data_dir, file, utterance_only):
    # Remove either text or full versions
    if utterance_only:
        if os.path.exists(os.path.join(data_dir, file + '_utt.txt')):
            os.remove(os.path.join(data_dir, file + '_utt.txt'))
    else:
        if os.path.exists(os.path.join(data_dir, file + '.txt')):
            os.remove(os.path.join(data_dir, file + '.txt'))


