import streamlit as st
from statistics import *
from issues import *
from formulas import *

st.set_page_config(page_title='Leesbaarheidsmeter', page_icon='outline_book_black_24dp.png', layout='wide', menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     })

# Header of the page
st.markdown("""
<style>
.big-font {
    font-size:42pt !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="big-font">Controleer je tekst op leesbaarheid</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)



# The left column where the users can input their text
col1.header('Uw tekst:')
text_input = col1.text_area(label="", height=200)
text_input = text_input.upper()

col1.write('')
uploaded_file = st.file_uploader("Add text file!")




# The right column where the user can find the results
col2.header('Resultaat:')
stats = col2.radio('', ['Statistics', 'Scores', 'Issues', 'Text composition'])
col2.write('<style>div.row-widget.stRadio > div{flex-direction:row;}'
           'div.row-widget.stRadio > div > label{margin-right: auto;}</style>', unsafe_allow_html=True)


if stats == 'Statistics':
    col2.markdown(
        f'Woorden:  \n'
        f'Totaal aantal woorden: {len(text_input.split())}  \n'
        f'Gemiddelde woordlengte: {average_word_length(text_input):.2f}  \n'
        f'Aantal unieke woorden: {unique_words(text_input)}')


    col2.markdown(
        f'Zinnen:  \n'
        f'Aantal zinnen: 12  \n'
        f'Langste zin (aantal woorden): 12  \n'
        f'Kortste zin (aantal woorden): 2  \n')

    col2.markdown(f'Reading time: {reading_time_minutes(text_input)} minutes')


elif stats == 'Scores':
    SMOG = col2.expander(f'SMOG: {len(text_input)}')
    with SMOG:
        st.write("""
        Methode die schat hoeveel jaar onderwijs nodig is om een 
        stuk tekst te begrijpen. "SMOG" is een afkorting voor 
        "Simple Measure of Gobbledygook". [1969]""")

    Brouwer = col2.expander(f'Brouwer: {len(text_input) + 1}')
    with Brouwer:
        st.write("""
        De index van Brouwer is zo opgezet dat eenvoudige leesboekjes voor kinderen een score krijgen van meer dan 100. 
        Normale, goed leesbare teksten hebben een score van zo tussen de 50 en 75, 
        teksten met een score onder de 30 worden over het algemeen als (zeer) moeilijk ervaren. [1963]""")
    ARI = col2.expander(f'ARI: {len(text_input) + 2}')
    with ARI:
        st.write("""
        Formule die werkt met het gemiddeld aantal karakters per woord.
        "ARI" is een afkorting voor "Automated Readability Index". [1967]""")
    Flesch_Douma = col2.expander(f'Flesch_Douma: {len(text_input) + 3}')
    with Flesch_Douma:
        st.write("""
        De score die uit de formule komt, verwijst naar verschillende opleidingsniveaus. 
        Hoe lager de score, hoe geschikter de tekst is voor academici. Hoe hoger de score, 
        hoe makkelijker de tekst is voor leerlingen van de basisschool (groep 6).  (""")


else:
    errors = warning_long_word(text_input)
    # warnings = ['too long a sentence', 'too long a ord']
    col2.write('This is way too long')
    for error in errors:
        col2.error(error)
    warnings = warning_sentences()
    for warning in warnings:
        col2.warning(warning)
    col2.write(annotated_text(
        "This ",
        ("is", "", "#8ef"),
        " some ",
        ("annotated", "adj", "#faa"),
        ("text", "noun", "#afa"),
        " for those of ",
        ("you", "pronoun", "#fea"),
        " who ",
        ("like", "verb", "#8ef"),
        " this sort of ",
        ("thing", "noun", "#afa"),
    ))
