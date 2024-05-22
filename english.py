from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize # pip install git+https://github.com/csebuetnlp/normalizer
import re

model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_en_bn")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_en_bn", use_fast=False)


# def translate_en(input_sentence):
#     input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
#     generated_tokens = model.generate(input_ids)
#     decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]
#     output_sentence = re.sub(r'<pad>|<\/s>', '', decoded_tokens)
#     return output_sentence

def translate_en(input_sentence):
    result = ""
    words = input_sentence.split('.')
    for word in words:
        input_ids = tokenizer(normalize(word), return_tensors="pt").input_ids
        generated_tokens = model.generate(input_ids)
        decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]
        output_sentence = re.sub(r'<pad>|<\/s>', '', decoded_tokens)
        result += (output_sentence)
    return result


# if __name__ == "__main__":
#     input_sentence = "A section of unscrupulous Bangladesh Road Transport Authority (BRTA) officials and staffers, police, transport associations, staffers of city corporations and municipalities and people affiliated with political parties realise the bribe and ransom, it said."
#     output_sentence = translate(input_sentence)

#     print("input sentence: ", input_sentence)
#     print("Output sentence: ", output_sentence)

#  বাংলাদেশ সড়ক পরিবহন কর্তৃপক্ষের (বিআরটিএ) কর্মকর্তা-কর্মচারী, পুলিশ, পরিবহন সমিতি, সিটি কর্পোরেশন ও পৌরসভার কর্মকর্তা-কর্মচারী এবং রাজনৈতিক দলের সঙ্গে জড়িত ব্যক্তিরা ঘুষ ও মুক্তিপণ আদায় করে বলে জানিয়েছে।
