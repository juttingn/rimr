# RIMR
automatic rhyme generator

## Installation
RIMR has been implemented and tested on Ubuntu 16.04 (Linux) with Python 3. Other environments may work but are untested.

There are three different libraries you need to download for RIMR to function. To install these you can do the following: 
```bash
sudo pip3 install -r requirements.txt
```
For voxpopuli there are some specific installation steps which are required and which you can all find here : https://github.com/hadware/voxpopuli
Make sure to install a French voice (required for the phonemization of French text).

## Usage 

## Potential Improvements
First of all, we would have liked RIMR to support languages other than French, such as English, German or Spanish for example. To do this, we should have found a lexicon with structure and information similar to the one we found for French. Then, we would have adapted the code to the new format of the lexicon, but a priori no problem with word phonemization because voxpopuli supports languages other than French.

The second idea that we would have liked to implement in RIMR is the option that the user can also enter an entire sentence as a query, instead of a single word. The rhyming engine would then have been configured such that the output of the rhyming engine would have displayed a structured sentence, rhyming entirely with the query.

One last idea that crossed our mind to further improve our project was to propose a "poet" option, where poetry enthusiasts could have found the verses of their favorite poets. This could have been achieved by downloading more files containing a large number of verses from the most famous poets. Then the user would have entered his request and the poet wanted for RIMR to display a rhyming verse with the query.

We encourage anyone using RIMR to implement these changes or make other suggestions to make RIMR better.
