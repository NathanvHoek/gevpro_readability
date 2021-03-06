# gevpro_readability
As first-year students of the bachelor Information Science at the University of Groningen, we were commanded to create a project for the course Advanced Programming given by our lecturer Dr. Andreas van Cranenburgh.

Of the two given choices for project topics, we chose to create a Dutch writing assistant.

Thereby, our project implements the aspects of the topic of readability, which its main characteristics are based on the number of characters/tokens, words, syllables, and sentences.

# Information about this project
With our version of a Dutch writing assistant, we mainly give, among other things, the readability scores and textual statistics. The readability scores are based on pre-existing formulas which reflect on the difficulty of reading a given Dutch text. The textual statistics are calculated in order to issue warnings on what is thus complicating the readability of the text.

The supported language is Dutch as one would reason based on the topic 'Dutch writing assistant', therefore the text is checked on correct language.

We have made use of the code/module of our aforementioned lecturer. His code and corresponding repository is linked under references below.

For the division of tasks within our group, we tried to do this as equally as possible. We created the idea and thought out the necessary components together, then divided these over the four of us. We helped one another out when we encountered difficulties or even took over for one during calamities. In the end, Nathan put all together in one app.


# Install
For the installation of the required modules, please run the following command:

```$ pip install -r requirements.txt```

For launching the corresponding web-interface, please run the following command:

```$ streamlit run app.py```

# Usage
For the usage of our Dutch writing assistant, no necessary pre-processing is needed. 

First, choose the option to either:
1. Type the text manually, or;
2. Add a file containg text from your computer.

Then, for processing, choose the option to either:
1. View the textual statistics of the given text, or;
2. View the scores of the readability formulas of the given text.
3. View the warnings that apply to your text

You can change your text live and see the changes in statistics, scores, and warnings.

You may then download the text as a text-file.

# References
Gerard Koolstra (2008), Leesbaarheid gevangen in formules:
[Algebra en Tellen - Leesbaarheid.pdf](https://github.com/NathanvHoek/gevpro_readability/files/8475591/Algebra.en.Tellen.-.Leesbaarheid.pdf)

Readability Module:
https://github.com/andreasvc/readability/tree/master/readability![image](https://user-images.githubusercontent.com/99412336/163030366-624b2992-85aa-4d72-ab5c-e05f86bb02ba.png)

Writing assistant main source of inspiration:
https://readable.com/









