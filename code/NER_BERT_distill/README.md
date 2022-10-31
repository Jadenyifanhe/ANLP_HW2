### dataset list

1. conll: 人工标注数据

### model list

2. BERT+CRF (teacher)
3. IDCNN+CRF (student)
4. BILSTM+CRF (student)

### requirement

1. PyTorch == 1.8.0
2. transformers==4.18.0
4. python3.6+

### 运行代码
1. teacher在scripts/run_ner_xxx.sh
2. student模型配置文件在scripts/run_ner_xxx_for_student.sh, student配置中BERT_BASE_DIR要写teacher模型路径
3. Modify the configuration information in `run_ner_xxx.py` or `run_ner_xxx.sh` .
4. `sh scripts/run_ner_xxx.sh`

### 蒸馏方式-2 (比运行run_ner_xxx_for_student.sh方式效果要好)
1. 可以用大量无监爬取数据直接作为test.txt让teacher预测hard label
2. 将1得到的数据直接作为student的训练集, 采用teacher方式继续训练, student继承teacher的某些层like BERT_BASE_DIR要写teacher模型路径
4. Modify the configuration information in `run_ner_xxx.py` or `run_ner_xxx.sh` .
5. `sh scripts/run_ner_xxx.sh`

### 更改配置
1. TRAIN_TYPE  -- teacher or student
2. OUTPUR_DIR -- 输出路径
3. TASK_NAME -- 数据集名称

**note**: file structure of the model

```text
├── prev_trained_model
|  └── bert_base
|  |  └── pytorch_model.bin
|  |  └── config.json
|  |  └── vocab.txt
|  |  └── ......
```