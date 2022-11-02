# NER_BERT_distill

### Usage
There are two models explored. The first one is BERT-CRF. To run it, use `sh scripts/run_ner_crf.sh`, and its results would be saved in `outputs/conll_output/bert`.

The second model is BILSTM-CRF as student and do knowledge distillation on the first model BERT-CRF as teacher.
We can also use the unlabeled samples as test.txt to let the teacher predict, and then use the output as the hard label as the training set of the student.
To run it, use `sh scripts/run_ner_crf_for_student.sh`, and `BERT_BASE_DIR` should be the path of saved teacher model.

To test model performance, run `scripts/run_ner_crf_for_test.sh` for both models. You can modify the configurations either in `run_ner_xxx.py` or `run_ner_xxx.sh`.

Note that we need to put pretrain model [bert-base-uncased](https://huggingface.co/bert-base-uncased?text=Paris+is+the+%5BMASK%5D+of+France.)
in `prev_trained_model/bert-base-uncased`. And its files level is as follow:
```
├── prev_trained_model
|  └── bert-base-uncased
|  |  └── config.json
|  |  └── pytorch_model.bin
|  |  └── tokenizer_config.json
|  |  └── tokenizer.json
|  |  └── vocab.txt
```