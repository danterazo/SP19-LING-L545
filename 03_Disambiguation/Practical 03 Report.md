# Practical 3: Disambiguation
udpipe output in Finnish treebank folder
conllu-perceptron-tagger output in /03_Disambiguation/

## Bash
```bash
...
> cat ../../data/UD_Portuguese-GSD/pt_gsd-ud-dev.conllu | python3 tagger.py pt-ud.dat > pt-ud-dev.out && python3 ../coNLL17/conll17_ud_eval.py --verbose ../../data/UD_Portuguese-GSD/pt_gsd-ud-dev.conllu pt-ud-dev.out
```

## Feature Extraction Updates
new features marked as #new; no improvements when commenting out features; no improvements with new features

modest improvement over example (~1) without changing anything for some reason