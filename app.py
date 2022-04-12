import streamlit as st
from statistics import *
from issues import *
import formulas
from io import StringIO


# ------------- PAGE CONFIGURATION ----------------------
def main():
    st.set_page_config(page_title='Leesbaarheidsmeter', layout='wide')

    # Hide the menu (burger icon)
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)

    # Overwrite default page padding
    st.markdown("""
    <style>
    .block-container {
        padding: 30px 80px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Change size of header title
    st.markdown("""
    <style>
    .big-font {
        font-size:39pt !important;
        padding-top: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="big-font">'
                'Controleer uw tekst op leesbaarheid'
                '</h1>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # ---------------------- TEXT INPUT ----------------------
    # --------------------------------------------------------

    con1 = st.container()
    con1.header('Uw tekst:')
    input_choice = con1.radio('', ['Tekst typen', 'Bestand toevoegen'])

    # Customize radio button
    con1.write('<style>div.row-widget.stRadio > div{flex-direction:row;}'
               'div.row-widget.stRadio > div > label {'
               'background-color:darkgreen;'
               'margin: 0px auto;'
               'padding: 10px;'
               'display: flex;'
               'align-items: center; '
               'justify-content: center; '
               'height:fit-content !important; '
               'width: 30%;}</style>', unsafe_allow_html=True)

    con2 = st.container()
    if input_choice == 'Tekst typen':
        con2.write('WAARSCHUWING! De ingegeven tekst wordt niet opgeslagen. '
                   'Wanneer je op de \'Bestand invoegen\' knop drukt, '
                   'zal de tekst verwijderd worden!')
        text_input = con2.text_area(label="", height=200)
        con2.download_button('Download deze tekst als .txt file', text_input)

    else:
        uploaded_file = con2.file_uploader("Add text file: ")
        if uploaded_file is not None:
            stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
            text_input = stringio.read()
            con2.header('Text')
            text_input = st.text_area(label="", value=text_input, height=400)
            con2.download_button('Download deze tekst als .txt bestand',
                                 text_input)
        else:
            text_input = ""

    if language_is_dutch(text_input) and len(words(text_input)) > 50:
        pass
    elif not language_is_dutch(text_input) and len(words(text_input)) > 50:
        con2.warning('Deze taal ken ik niet! '
                     'Deze leesbaarheidstest is speciaal voor '
                     'Nederlandse teksten ontworpen!')

    # --------------------------------------------------------
    # -------------------- TEXT ANALYSIS ---------------------
    # --------------------------------------------------------

    if len(text_input.split()) != 0:
        # ---------------------- OPTIONS -------------------------

        with st.container():
            options = st.radio('',
                               ['Statistieken', 'Formules', 'Waarschuwingen'])
            st.write(
                '<style>'
                'div.row-widget.stRadio > div {flex-direction:row;}'
                'div.row-widget.stRadio > div > label '
                '{margin-right: auto;'
                'padding: 0px auto;}'
                '</style>', unsafe_allow_html=True)

        # -------------------- TEXT STATISTICS -------------------
        if options == 'Statistieken':
            col1, col2, col3 = st.columns(3)

            col1.header('Woorden')

            col1.markdown(
                f'Totaal aantal woorden:  '
                f'{total_word_count(text_input):>10}  \n\n'
                f'Aantal unieke woorden:  '
                f'{unique_words_count(text_input):>10}  \n\n'
                f'Gemiddeld aantal letters: '
                f'{average_word_length_char(text_input):.2f} \n\n'
                f'Gemiddeld aantal lettergrepen: '
                f'{avg_syll_per_word(text_input):.2f} \n\n'
                f'Aantal woorden die langer zijn dan gemiddelde woord: '
                f'{words_chars_over_avg(text_input):.2f} \n\n'
                f'Langste woord: {longest_word(text_input)}  \n\n'
            )

            col2.header('Zinnen')
            col2.markdown(

                f'Aantal zinnen: {total_count_sentences(text_input)}  \n\n'
                f'Gemiddeld aantal woorden per zin: '
                f'{avg_word_count_per_sent(text_input): .2f}  \n\n'
                f'Gemiddeld aantal lettergrepen per zin: '
                f'{avg_syll_count_per_sent(text_input):.2f}  \n\n'
                f'Gemiddeld aantal karakter per zin: '
                f'{avg_char_count_per_sent(text_input):.2f}  \n\n'
                f'Langste zin heeft '
                f'{len(longest_sentence(text_input).split())} woorden:  \n'
                f' {longest_sentence(text_input)} ')

            col3.header('Overig')
            col3.markdown(f'Total paragraphs : {len(paragraphs(text_input))}')
            col3.markdown('Top ten most used keywords:')
            count = 1
            for word in n_most_used_words(text_input, 10):
                col3.markdown(f' {count}. {word[0]}: {word[1]} keer')
                count += 1

        # -------------- READABILITY FORMULAS ------------
        elif options == 'Formules':
            brouwer_score, brouwer_status = \
                formulas.Brouwer(avg_syll_per_word(text_input),
                                 avg_word_count_per_sent(text_input))
            Brouwer = st.expander(f'FORMULE VAN BROUWER  |  '
                                  f'Score:  {brouwer_score: .2f}  |  '
                                  f'{brouwer_status}')
            with Brouwer:
                st.write("""
                De index van Brouwer is zo opgezet dat eenvoudige leesboekjes
                 voor kinderen een score krijgen van meer dan 100.
                 Normale, goed leesbare teksten hebben een score van zo tussen
                 de 50 en 75, teksten met een score onder de 30 worden over
                 het algemeen als (zeer) moeilijk ervaren. [1963]""")

            flesch_douma_score, flesch_douma_status = \
                formulas.Flesch_Douma(avg_syll_per_word(text_input),
                                      avg_word_count_per_sent(text_input))

            Flesch_Douma = st.expander(f'FORMULE VAN FLESCH-DOUMA  | '
                                       f'Score: {flesch_douma_score:.2f}  | '
                                       f'{flesch_douma_status}')
            with Flesch_Douma:
                st.write("""
                De score die uit de formule komt, verwijst naar
                 verschillende opleidingsniveaus. Hoe lager de score,
                 hoe geschikter de tekst is voor academici. Hoe hoger de score,
                 hoe makkelijker de tekst is voor leerlingen van de basisschool
                 (groep 6).""")

            SMOG_score, SMOG_status = formulas.SMOG(
                formulas.long_words_SMOG(text_input),
                total_count_sentences(text_input))

            SMOG = st.expander(f'SMOG  |  '
                               f'Score: {SMOG_score:.2f} |  '
                               f'{SMOG_status}')
            with SMOG:
                st.write("""
                    Methode die schat hoeveel jaar onderwijs nodig is om een
                     stuk tekst te begrijpen. "SMOG" is een afkorting voor
                     "Simple Measure of Gobbledygook". [1969]""")

        # -------------------------- WARNINGS --------------------------
        elif options == 'Waarschuwingen':
            long_words = st.expander(
                label=f"Deze woorden "
                      f"({len(warning_long_word(words(text_input)))}"
                      f" in totaal) zijn wat aan de lange kant "
                      f"(3 of meer lettergrepen)!")
            with long_words:
                for long_word in warning_long_word(words(text_input)):
                    st.error(long_word)

            long_sentences = st.expander(
                label=f"Deze zinnen "
                      f"({len(warning_long_sentences(text_input))} "
                      f"in totaal) zijn wat aan de lange kant!")
            with long_sentences:
                for long_sentence in warning_long_sentences(text_input):
                    st.error(long_sentence)

            rare_word = st.expander(
                label=f"Deze {len(warning_rare_word(text_input))} "
                      f"woorden komen minder dan 1 op de 100.000.000 "
                      f"keer voor in teksten. Een zeldzaam woord dus!"
                      f"Ken je een woord dat vaker gebruikt wordt?")
            with rare_word:
                for word in warning_rare_word(text_input):
                    st.error(word)

            warning_passive = st.expander(
                label=f"In deze zinnen "
                      f"({len(warning_passive_voice(text_input))}"
                      f" in totaal) gebruik je mogelijk een passieve"
                      f" zinsconstructie. Gebruik liever actieve zinnen,"
                      f" deze lezen fijner!")
            with warning_passive:
                for sentence in warning_passive_voice(text_input):
                    st.error(sentence)

            warning_first_word_repeat = st.expander(
                label=f"Deze zinnen "
                      f"({len(warning_first_word_of_sent_repeat(text_input))} "
                      f"in totaal) beginnen met precies hetzelfde woord "
                      f"als de vorige zin. Beetje veel herhaling of niet?")
            with warning_first_word_repeat:
                for sentence in warning_first_word_of_sent_repeat(text_input):
                    st.error(sentence)


if __name__ == '__main__':
    main()
