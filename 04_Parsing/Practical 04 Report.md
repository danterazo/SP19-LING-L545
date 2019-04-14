# Practical 04: Parsing
## Bash
```bash
> cd /04_Parsing/data/UD_Japanese-GSD/
> udpipe --tokenizer none --tagger none --train ja.udpipe < ja_gsd-ud-train.conllu
> udpipe --parse ja.udpipe < ja_gsd-ud-test.conllu > ja_gsd-test-out.conllu
> cd ../../../03_Disambiguation/tools/conllu-perceptron-tagger
> cat ja_gsd-ud-test.conllu | python3 ../../../03_Disambiguation/tools/conllu-perceptron-tagger/tagger.py ja-ud.dat > ja-ud-test.out && python3 ../../../03_Disambiguation/tools/coNLL17/conll17_ud_eval.py --verbose ja_gsd-ud-test.conllu ja-ud-test.out
```

## CoNLL17 Evaluation


## 