# Description
In this assignment, you will conduct an analysis of tweets produced by Russian trolls during the 2016 US election. These tweets were published by 538. We’ll be assessing the frequency with which troll tweets mention “Trump” by name.

1.	Data Collection
    a.	Download the raw tweet data.
    b.  Looking at only the first 10,000 tweets in the file, keep those that (1) are in English and (2) don’t contain a question. This will be our dataset. To filter the right tweets out, take a look at the columns.  
        i.	There are specific columns that call our language.  You can trust these.
        ii.	Assume that a tweet which contains a question contains a “?” character.
    c.	Create a new file (TSV format) containing these tweets.
2.	Data Annotation
    a.	To do our analysis, we need to add one new feature: whether or not the tweet mentioned Trump. This feature “trump_mention” is Boolean (=”T”/”F”).  A tweet mentions Trump if and only if it contains the word “Trump” (case-sensitive) as a word.  This means that it is separated from other alphanumeric letters by either whitespace OR non-alphanumeric characters (e.g., “anti-Trump protesters” contains “trump”, but “I got trumped” does not).
    b.	Create a new version of your dataset that contains this additional feature.
3.	Analysis
    a.	Using your newly annotated dataset, compute the statistic: % of tweets that mention Trump.
    b.	It turns out that our approach isn’t counting tweets properly … meaning that some tweets are getting counted more than once.  Go through and look at your annotated data.  Identify where the counting problem is coming from.
