from PyPDF2 import PdfReader
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
import os

data_path = "./NLPPapersSpider/nlp"
meetings = ["ACL", "EMNLP"]
years = ["2018", "2019", "2020", "2021"]


def read_data_from_path():
    nlp = English()
    sentencizer = nlp.add_pipe("sentencizer")
    tokenizer = Tokenizer(nlp.vocab)
    papers = []
    for meeting in meetings:
        for year in years:
            filepath = os.path.join(data_path, meeting, year)
            if not os.path.exists(filepath):
                continue
            for path, _, file_list in os.walk(filepath):
                for file_name in file_list:
                    file = os.path.join(path, file_name)
                    print ("-------start tokenizer paper: {}".format(file))
                    reader = PdfReader(file)
                    for page in reader.pages:
                        text = page.extract_text()
                        for sent in list(nlp(text).sents):
                            sent_text = sent.text.strip()
                            if len(sent_text) < 1:
                                continue
                            sent_ls = [item.lower_ for item in nlp(sent_text) if item.lower_.strip() != ""]
                            if len(sent_ls) <= 10:
                                continue
                            papers.append(" ".join(sent_ls))

    return papers


def write_data(data, outpath):
    with open(os.path.join(outpath, "train.txt"), "w") as f:
        for sent in data:
            f.write(sent + "\n")


if __name__ == "__main__":
    print ("---------start read pdf-----------")
    data = read_data_from_path()
    write_data(data, data_path)
