# Calculating textual similarity

Compares texts in the 9 corpora included in NLTK book, but could be adapted to operate on a directory of texts.

## About
Describing similarity between texts strictly numerically requires using various linguistic metrics. Intuitively, one may describe similarities based on outside information about the text, e.g., date of publication, or else by describing the content, e.g., a book of modern ghost stories may be similar to _The Fall of the House of Usher_. 

	But there is also a rough but roughly accurate way to describe textual similarity using more banal metrics. In my function, I compare word frequency distributions, average word length, and average sentence length.
	
	Word frequency distribution: how often is a word token distributed across a text? Or put another way, what proportion of a text is made up of a given word? Two books about coffee will have high frequencies of "bean" and "grind," which would mark them as similar texts. But stylometry literature tells us that counterintuitively, function words like 'of' and 'like' are also very revealing of authorial style.
	
	Average word length in vocabulary: texts are dissimilar if one uses brusque language ("I didn't go") and the other uses longer words ("I categorically refused to attend"). The average word length is taken from the total length of all of the keys in the frequency distribution divided by the number of keys. In this way, when counting up words, 'of' only appears once in the keys.
	
	Average sentence length: Hemingway's terse style and Dickens' paid-by-the-word writing feel very different to a reader, but for my function, they are also numerically distinct. The average sentence length here is in characters, not words. This number is derived from the total length of all sentences in the text (as parsed by the Punkt sentence tokenizer) divided by the number of all sentences in the text. 
	
	The function I wrote uses all of these metrics to come up with a similarity score. Texts that are the same have a score of zero. Texts that are very different can have scores in the teens or higher. The similarity score is somewhat arbitrarily weighted. The average difference between word frequencies is multiplied by 10,000 so that it carries more weight (i.e., 3.3 instead of 0.00033). The difference between average word length stays the same (e.g., 1.477). The difference between average sentence length (asl) is taken as log(base 10)(asl), so that the scores are less unwieldy (e.g., 1.738 instead of 54.743) and have a reasonable weight in the final score.

## Most & least similar corpora in NLTK book 
The most similar texts are _Moby Dick_ and _Sense and Sensibility_. 
The least similar are the Book of Genesis and the Personals Corpus.

## Function vs. intuition
At the two ends of the spectrum, with this small collection of texts, my similarity function is in line with my own intuition of the texts. As a reader, I know that _MB_ (1851) and _SS_ (1811) both use the same kind of overwrought 19th-c. language, particularly with long words and long sentences. _MB_, _SS_, and _The Man Who Was Thursday_ are all very similar to each other, being the only novels in the collection. I am also aware that the sacred text of Genesis is radically different from the Personals, in language style and especially in content.  

There are a few surprises. The Chat Corpus is more similar to _WSJ_ (6.66) than to the Personals (17.53). I would have thought that both use similarly short words and sentences, and in reading the first few hundred words of Chat and Personals, they seem to share similar lewd language. (Perhaps in other parts of the Chat Corpus, international business deals are discussed.) In fact, the Personals corpus is the least similar to any other texts; all 8 pairs that include Personals are in the last 8 slots in the table. Looking at the average word and sentence lengths in Personals, neither are especially low or high compared to the rest of the collection. The major factor in the dissimilarity of Personals to the rest of the collection must therefore be in word frequencies. Looking through the first hundred words, however, I can see that there is not much lexical diversity in this corpus. The ads are very short, meaning many authors are describing the same basics in a short line of text -- that's bound to limit the lexicon and dramatically increase the frequencies of some words ("man").
	
## Two ideas to improve the calculation of textual similarity:

a) Isolate words that appear very often in the two texts being compared relative to the rest of the text collection. Two documents about Venice will mention canals and gondolas far more often than in the rest of the texts, but that interesting and unusual comparison would be swallowed up and flattened out by my current algorithm. Picking out unusually high document term frequencies, compared to term frequencies across the whole collection, reveals more about the content of the text. 

b) I used average word and sentence lengths, but it may be more accurate to compare frequencies of word and sentence lengths. In texts as long as the ones in the collection, taking the average is passable, but does a very rough job of describing a whole text. 

*Robin Camille Davis
February 27, 2014
Created for Methods in Computational Linguistics II (Andrew Rosenberg), Homework I*


