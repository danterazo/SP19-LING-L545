# Practical 04: Parsing / Dependency
## Bash
```bash
> cd /04_Parsing/data/UD_Japanese-GSD/
> udpipe --tokenizer none --tagger none --train ja.udpipe < ja_gsd-ud-train.conllu
> udpipe --parse ja.udpipe < ja_gsd-ud-test.conllu > ja_gsd-test-out.conllu
> cat ja_gsd-ud-train.conllu | python3 ../../../03_Disambiguation/tools/conllu-perceptron-tagger/tagger.py -t ja-ud.dat
> cat ja_gsd-ud-test.conllu | python3 ../../../03_Disambiguation/tools/conllu-perceptron-tagger/tagger.py ja-ud.dat > ja-ud-test.out
> python3 ../../../03_Disambiguation/tools/coNLL17/conll17_ud_eval.py --verbose ja_gsd-ud-test.conllu ja-ud-test.out
```

## CoNLL17 Evaluation
My Japanese model received a **UPOS** score of 95.57, which is only slightly below the CoNLL17 score of the Portuguse
model from the last practical

## Plotting
changed y[] assignment

![rwo](./report_assets/rwo.png)

OV = word index is lower than it's head index
VO = word index is higher than it's head index
