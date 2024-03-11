from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize # pip install git+https://github.com/csebuetnlp/normalizer
import re

model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_bn_en")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_bn_en", use_fast=False)


def translate(input_sentence):
    input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
    generated_tokens = model.generate(input_ids)
    decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]
    output_sentence = re.sub(r'<pad>|<\/s>', '', decoded_tokens)
    return output_sentence


if __name__ == "__main__":
    input_sentence = "চার শিরোপা জেতার পর প্রথমবার ফাইনাল হারলেও বিশেষ এক প্রাপ্তিতে বড় তৃপ্তির উপকরণ পাচ্ছেন কোচ"
    output_sentence = translate(input_sentence)

    print("input sentence: ", input_sentence)
    print("Output sentence: ", output_sentence)

