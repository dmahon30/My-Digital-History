# Oral History Sonic Soundcloud: Experimentation

## DevLog 2: The Struggle to Sonify Transcript Data is Real.

## The Initial Plans (Spoiler: There are 2)

+ Plan number one: I wanted to take workforce data from the Africville Relocation Report and sonify that to interpret a conversation about labour data between genders. 

+ Plan number two: The first plan was simply to challenge myself to work with quantitative data to make an argument through sonal interpretation (rather than the usual essay format of historical argumentation). 

	- Plan number two involved 
	A. Analyzing qualitative data (interview transcripts with former residents) using TF-IDF (via Voyant or R-language)
	B. Creating a visual and audible interpretation of the 25 most frequent/significant terms in the transcript data.

## Challenges & Change in Plans

+ OK, so things did not go according to plan. 

+ Re: PLAN 1: 
	+ The MIDIscript detailed in [Programming Historian on Sonification](https://programminghistorian.org/en/lessons/sonification) really relies on change over time. The issues with my data was that the information was drawn from the same year, plus the interpretation on workforce data was limited in scope and quantity. I didn't feel comfortable manipulating the time variables, so I had to abandon that dataset. Instead, I'll be experimenting with statscan census data on ethnicity in Canada from the late 19th-century to the mid-20th century. 
	+ What stood out to me about this data (compiled in the early 1970s) was the conception of ethnicity measured across the years. What sort of conversation can we glean from how ethnicity was categorized, measured, and silenced - how can we sonify [this data] (https://docs.google.com/spreadsheets/d/1PEKXc-f0oEbr5uTKmYaYvoL4BSn8zBORAMbI0Yspqgs/edit?usp=sharing)?
	+ So I'll try again with the python script using the above data and see what I can come up with!

+ Re: PLAN 2:
	+ DeepSpeech is not picking up the words effectively in it's speech-to-text function (no matter how small of a segment I make the interviews). So, moving forward, I think it would be faster for me to transcribe each interview by hand. I'll transcribe 2-3 one hour interviews in order to have a corpus of texts for the TF-IDF function to work
			+ [This StackOverFlow thread] (https://stackoverflow.com/questions/22790974/how-to-calculate-tfidf-for-a-single-new-document-to-be-classified) notes that the text function would work fine for one text, but the inverse-document-frequency function wouldn't apply as easily.
	+ Since I had to switch gears with DeepSpeech, I only have one transcript to work with at this time. So then I ran it through Voyant to get some text frequency data to create a prototype, but I like the customization option of using R so that will be the tool I use for the corpus.

## Why use TF-IDF for Oral History Transcripts?

+ I know there are limitations in both the tool and using transcripts to identify textual patterns. Computational analysis tools can be a great way to help users get a feel for the content of an OH collection. It can present a powerful means of understanding document similarity by identifying key terms across multiple transcripts. Unfortunately I don't have a prototype resulting from the IDF application, but I do have one showing TF patterns in one interview.

## Plan 2: Prototype Process

+ After running the transcript through Voyant, I edited the stopwords to remove verbal pauses, and other non-descript terms. This generated a list of the 25 most frequent terms in the text, as well as a wordcloud representation of the ascending data. 
+ If you'd like to see my list of stopwords and the frequency list, [click here](https://docs.google.com/spreadsheets/d/1ABT2dhzQNmu6CMsxs7JfuKs9PPKirIaME9gAUebSfG4/edit?usp=sharing)

### Here is the visualized data (the wordcloud)	

![](/images/Wordcloud.png)	


### Now, the audio prototype

+ I decided I wanted to create an audiofile that reflected the frequency data, which I made using only the 5 most frequent terms.
+ I then pulled samples from my interview where the participants were saying these words to add another dimension to the data.
+ I also thought it would be quite powerful to loop these words, and increase the volume for each word depending on their TF. For example, the more often the word appeared in the text, the louder the word would be. The audio was then ordered from the quietest sample to the loudest.

+ This is a very basic prototype, but here is an example of the sonal interpretation:

{{<audio src="/posts/Transcript-Soundcloud.mp3" >}}
	
