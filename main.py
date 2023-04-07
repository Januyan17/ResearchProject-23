import IPython
import matplotlib
import matplotlib.pyplot as plt
import torch
import torchaudio

matplotlib.rcParams["figure.figsize"] = [16.0, 4.8]

torch.random.manual_seed(0)
device = "cuda" if torch.cuda.is_available() else "cpu"

print(torch.__version__)
print(torchaudio.__version__)
print(device)

symbols = "_-!'(),.:;? abcdefghijklmnopqrstuvwxyz"
look_up = {s: i for i, s in enumerate(symbols)}
symbols = set(symbols)


def text_to_sequence(text):
    text = text.lower()
    return [look_up[s] for s in text if s in symbols]


text = "Hello My Name Is Januyan . Iam Voice Artificial Intelligence"
print(text_to_sequence(text))

processor = torchaudio.pipelines.TACOTRON2_WAVERNN_CHAR_LJSPEECH.get_text_processor()

# text = "Hello My Name Is Januyan . Iam Voice Artificial Intelligence"
processed, lengths = processor(text)

print(processed)
print(lengths)
print([processor.tokens[i] for i in processed[0, : lengths[0]]])

