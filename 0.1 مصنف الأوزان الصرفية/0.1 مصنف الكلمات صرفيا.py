import re
import ast

class ArabicProcessor:
    def __init__(self, symbols_path):
        self.arabic_symbols = self.load_arabic_symbols(symbols_path)
        self.compiled_patterns = {}

    def load_arabic_symbols(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return ast.literal_eval(file.read())

    def compile_weights_to_regex(self, weights):
        for weight in weights:
            pattern = ""
            for letter in weight:
                if letter in self.arabic_symbols:
                    pattern += self.arabic_symbols[letter]
                else:
                    pattern += letter
            self.compiled_patterns[weight] = re.compile(pattern)

class FileManager:
    def __init__(self, processor):
        self.processor = processor

    def read_sarf_weights(self, file_path):
        special_chars = {'أ', 'إ', 'أ', 'آ', 'ؤ', 'ئ', 'س', 'ت', 'م', 'ن', 'ه', 'ي', 'ء', 'و', 'ج'}
        with open(file_path, 'r', encoding='utf-8') as file:
            weights = [line.strip() for line in file.readlines()]
        
        priority_weights = []
        secondary_weights = []

        for weight in weights:
            if any(char in weight for char in special_chars):
                priority_weights.append(weight)
            else:
                secondary_weights.append(weight)

        return priority_weights, secondary_weights


    def process_words(self, words_file_path, priority_weights, secondary_weights, results_file_path):
        self.processor.compile_weights_to_regex(priority_weights + secondary_weights)
        with open(words_file_path, 'r', encoding='utf-8') as words_file, \
             open(results_file_path, 'w', encoding='utf-8') as results_file:
            for word in words_file:
                word = word.strip()
                matched = False
                for weight in priority_weights + secondary_weights:
                    pattern = self.processor.compiled_patterns[weight]
                    if pattern.fullmatch(word):
                        results_file.write(f"{word} = {weight}\n")
                        matched = True
                        break
                if not matched:
                    results_file.write(f"{word} = ***\n")

def main():
    arabic_processor = ArabicProcessor("الخريطة.txt")
    file_manager = FileManager(arabic_processor)
    
    priority_weights, secondary_weights = file_manager.read_sarf_weights("الأوزان++.txt")
    file_manager.process_words("الألفاظ.txt", priority_weights, secondary_weights, "النتائج.txt")

if __name__ == "__main__":
    main()
