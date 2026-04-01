from spellchecker import SpellChecker 

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word)

                
        return ' '.join(corrected_words)

    def run(self):
        print("\n __ Spell Checker__")

        while True:
            text = input('Enter text to check for type "exit" to quit):')

            if text.lower() == 'exit':
                print('Closing the programm...') 
                break

            correct_text = self.correct_text(text)
            print(f'Corrected Text : {correct_text}')


if __name__ == "__main__":
    SpellCheckerApp().run()



