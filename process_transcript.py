class Dialogue:
    def __init__(self, conversation_id, num_utterances, utterances):
        self.conversation_id = conversation_id
        self.num_utterances = num_utterances
        self.utterances = utterances

    def to_string(self):
        return str("Conversation: " + self.conversation_id + "\n"
                   + "Number of Utterances: " + str(self.num_utterances))


class Utterance:
    def __init__(self, speaker, text, da_label):
        self.speaker = speaker
        self.text = text
        self.da_label = da_label

    def to_string(self):
        return str(self.speaker + " " + self.text + " " + self.da_label)

# def process_transcript(transcript):