from puzzle.step1_tokenize import hands_re
from puzzle.step2_normal_form import to_normal_form
from puzzle.step3_stop_words import no_stop
from puzzle.step4_freq_analyze import analize

def get_theme(text):
    words = hands_re(text)
    normals = to_normal_form(words)
    words_no = no_stop(normals)
    theme = analize(words_no)
    return theme

