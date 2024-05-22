from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize # pip install git+https://github.com/csebuetnlp/normalizer
import re

model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_bn_en")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_bn_en", use_fast=False)


# def translate_bn(input_sentence):
#     input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
#     generated_tokens = model.generate(input_ids)
#     decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]
#     output_sentence = re.sub(r'<pad>|<\/s>', '', decoded_tokens)
#     return output_sentence

def translate_bn(input_sentence):
    result = ""
    words = input_sentence.split('।')
    for word in words:
        input_ids = tokenizer(normalize(word), return_tensors="pt").input_ids
        generated_tokens = model.generate(input_ids)
        decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]
        output_sentence = re.sub(r'<pad>|<\/s>', '', decoded_tokens)
        result += (output_sentence)
    return result

if __name__ == "__main__":
    # input_sentence = "চার শিরোপা জেতার পর প্রথমবার ফাইনাল হারলেও বিশেষ এক প্রাপ্তিতে বড় তৃপ্তির উপকরণ পাচ্ছেন কোচ"
    # output_sentence = translate_bn(input_sentence)

    # print("input sentence: ", input_sentence)
    # print("Output sentence: ", output_sentence)
    
    input_text = "এ সময় চট্টগ্রাম নগর থেকে বিভিন্ন উপজেলা, কক্সবাজার, রাঙামাটি, বান্দরবান ও খাগড়াছড়ির উদ্দেশে ছেড়ে যায়নি কোনো বাস। এতে চরম ভোগান্তিতে পড়েন নগরের সাধারণ যাত্রীরা।  এ সময় চট্টগ্রাম নগর থেকে বিভিন্ন উপজেলা, কক্সবাজার, রাঙামাটি, বান্দরবান ও খাগড়াছড়ির উদ্দেশে ছেড়ে যায়নি কোনো বাস। এতে চরম ভোগান্তিতে পড়েন নগরের সাধারণ যাত্রীরা।"

    # Split the input text at the character '।'
    sentences = input_text.split('।')

    # Print the sentences
    for i, sentence in enumerate(sentences):
        print(f"Sentence {i+1}: {sentence.strip()}")

