## Practical 01b: Segmentation & Tokenization
## Segmentation Questions
1. How should you segment sentences with semicolons? As a single sentence or as two sentences? Should it depend on context?  
Sentences with semicolons should be treated as two separate sentences. Semicolons conjoin two independent (yet related)
clauses. One might argue that since the thoughts are related, they should be treated as one, but the same
could be said for two consecutive related sentences. It just doesn't make sense.

2. Should sentences with ellipsis be treated as a single sentence or as several sentences?  
Ellipses can mean many things depending on the context. On the internet, they commonly denote a trailing thought
(e.g. "This practical sure was fun...") or a sense of wistfulness in the same context. In quotes or mathematical sets,
they can represent a purposeful omission or skip. Sentences with ellipses should be treated as one because the topic is
the same on both sides of the ellipses, or in the case of the first example, they're purely stylistic.

3. If there is an exclamation after the first word in the sentence should it be a separate sentence? How about if there is a comma?  
Single-word exclamations are sentences and should be counted as such. This is important in sentiment analysis; a single word
can carry strong positive or negative sentiment (i.e. "Argh!" or "Nice!").

4. Can you think of some hard tasks for the segmenter?  
"W. E. B. DuBois... he's all over the place; I saw him runnin' around town."  
Here, periods indicate both initials, ellipses (as a set of 3), and the end of the sentence. Apostrophes represent both
contractions and the reduction of [ŋɡ] to [n], the alveolar nasal consonant, in colloquial English. The semicolon links
two related sentences together; readers rely on the former to determine who 'him' is referring to in the latter.


## Tokenization Questions
1. Why should we split punctuation from the token it goes with?  
When looking at the tokens themselves, context isn't that important. Removing punctuation and splitting
apart contractions gives you the most tokens to work with. The manner in which they were pieced together is no
longer important.

2. Should abbreviations with space in them be written as a single token or two tokens? How about numerals like 134 000?   
I can't think of any abbreviations with spaces, but one with periods that comes to mind is **M.I.T**, a proper noun. It is
safe to remove the periods and count it as one token ("MIT"). The three letters have no meaning when they're separate.
Numbers should be combined with spaces and commas removed and counted as one token each.

3. If you have a case suffix following punctuation, how should it be tokenized?   
Probably as one token. I can't think of any suffixes that immediately follow punctuation, and neither can Google.

4. Should contractions and clitics be a single token or two (or more) tokens?  
For contractions, two or more, but unless the tokenizer can interpret clitics it should leave them as one token. Clitics
aren't understood on their own so separating them wouldn't be useful. A good tokenizer would be able to see
*couldn't* and rewrite it as *could not*.

