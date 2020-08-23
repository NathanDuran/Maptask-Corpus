import string


class Dialogue:
    def __init__(self, conversation_id, num_utterances, utterances):
        self.conversation_id = conversation_id
        self.num_utterances = num_utterances
        self.utterances = utterances

    def __str__(self):
        return str("Conversation: " + self.conversation_id + "\n"
                   + "Number of Utterances: " + str(self.num_utterances))


class Utterance:
    def __init__(self, speaker, text, da_label):
        self.speaker = speaker
        self.text = text
        self.da_label = da_label

    def __str__(self):
        return str(self.speaker + " " + self.text + " " + self.da_label)


def process_transcript(transcript, moves_g, moves_f, excluded_chars, excluded_tags):

    # Extract speakers DA's from the 'moves' files
    moves_g = get_da_list(moves_g)
    moves_f = get_da_list(moves_f)
    g_index, f_index = 0, 0

    # Process each utterance in the transcript and create list of Utterance objects
    utterances = []
    for line in range(3, len(transcript)):  # First 3 lines are not utterances

        # Get the speaker from the text
        speaker = transcript[line].split("\t")[0]

        # Get the utterance text
        text = transcript[line].split("\t")[1]

        # Check just in case excluded chars are in text
        if any(char in excluded_chars for char in text):
            # Tokenise text and remove incomplete words i.e. 'th--'
            tokens = text.split(' ')
            tokens = [token for token in tokens if '--' not in token]
            text = ' '.join(join_punctuation(tokens))

        # Get the appropriate speaker DA
        if speaker == 'g':
            da = moves_g[g_index]
            g_index += 1
        else:
            da = moves_f[f_index]
            f_index += 1

        # Create an utterance if its DA not an excluded one
        if da not in excluded_tags and len(text) >= 1:
            utterances.append(Utterance(speaker, text, da))

    # Get the conversation ID and number of utterances
    conversation_id = transcript[1].split(' ')[1].replace(';', '')
    num_utterances = len(utterances)

    dialogue = Dialogue(conversation_id, num_utterances, utterances)
    return dialogue


def get_da_list(moves):
    da_list = []
    for line in range(2, len(moves)):  # First two lines are metadata
        # Skip lines that have no DA labels
        if "label" in moves[line]:
            # Get DA from labels
            da = moves[line].split("label=")[1].split("\"")[1].split("\"")[0]
            da_list.append(da)

    return da_list


def join_punctuation(tokens, characters='.,;?!'):
    # characters = set(characters)

    try:
        tokens = iter(tokens)
        current = next(tokens)

        for char in tokens:
            if char in string.punctuation:
                current += char
            else:
                yield current
                current = char

        yield current
    except StopIteration:
        return