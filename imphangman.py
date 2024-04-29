import random
from collections import Counter, defaultdict
word_list = words = [
    "Abjunct",
    "Acaroid",
    "Achillea",
    "Aigrette",
    "Alcaid",
    "Aleatory",
    "Alidade",
    "Allodium",
    "Amadou",
    "Amulet",
    "Anhinga",
    "Anisopod",
    "Antilogy",
    "Aperitif",
    "Aphelion",
    "Apopyle",
    "Arbuscle",
    "Arcturus",
    "Arete",
    "Arhat",
    "Arnica",
    "Arsinoe",
    "Ascesis",
    "Ashram",
    "Astilbe",
    "Atoll",
    "Augury",
    "Avowal",
    "Axil",
    "Backstay",
    "Bambino",
    "Barnacle",
    "Basilisk",
    "Bastide",
    "Beadwork",
    "Belay",
    "Beldame",
    "Bespoke",
    "Bijoutery",
    "Bireme",
    "Bladdery",
    "Brabble",
    "Brachium",
    "Bramble",
    "Bromide",
    "Brummell",
    "Buffoon",
    "Bulwark",
    "Burdock",
    "Cachalot",
    "Cachucha",
    "Calabash",
    "Calathus",
    "Camelia",
    "Canoodle",
    "Canticle",
    "Capybara",
    "Caracole",
    "Carbuncle",
    "Carboy",
    "Carillon",
    "Castanet",
    "Cavicorn",
    "Celadon",
    "Cellarer",
    "Ceorl",
    "Chivvy",
    "Clastic",
    "Clinquant",
    "Codpiece",
    "Colinear",
    "Comestor",
    "Conurbia",
    "Cormlet",
    "Crabbily",
    "Crenulate",
    "Crevasse",
    "Croft",
    "Cumbrous",
    "Cynosure",
    "Dander",
    "Debility",
    "Decipher",
    "Dedendum",
    "Dehort",
    "Demulcent",
    "Desiccate",
    "Diamante",
    "Diapason",
    "Dibber",
    "Dickey",
    "Diddle",
    "Dicker",
    "Diphtheria",
    "Discomfit",
    "Drachma",
    "Dragoon",
    "Dromedary",
    "Ducatoon",
    "Efferent",
    "Effleurage",
    "Effluvium",
    "Emaciate",
    "Encomia",
    "Enclave",
    "Engram",
    "Ennui",
    "Epaulet",
    "Epiphyte",
    "Eremite",
    "Eristic",
    "Estray",
    "Eulogist",
    "Fain",
    "Fenestral",
    "Fetlock",
    "Fissure",
    "Flan",
    "Flense",
    "Flummery",
    "Forage",
    "Foppery",
    "Fray",
    "Fustian",
    "Gabardine",
    "Galilee",
    "Garotte",
    "Gendarme",
    "Gibber",
    "Gossan",
    "Grovel",
    "Hake",
    "Halation",
    "Halophile",
    "Hanaper",
    "Hebdomad",
    "Hectogon",
    "Hedgehog",
    "Hematic",
    "Hemophiliac",
    "Heraldry",
    "Hoarfrost",
    "Hoax",
    "Homuncle",
    "Honcho",
    "Huzzah",
    "Hypogene",
    "Ichor",
    "Immure",
    "Imprimis",
    "Infector",
    "Inure",
    "Isolette",
    "Janissary",
    "Jalousie",
    "Jilt",
    "Joggle",
    "Jouster",
    "Kurgan",
    "Kvetch",
    "Labium",
    "Lampion",
    "Lanterne",
    "Lapwing",
    "Leman",
    "Limpid",
    "Littoral",
    "Logomachy",
    "Loquitur",
    "Lustrum",
    "Machinator",
    "Macra",
    "Madrigal",
    "Mangonel",
    "Mantrap",
    "Marabout",
    "Mariposa",
    "Melanoid",
    "Mete",
    "Middy",
    "Monodon",
    "Morglay",
    "Moue",
    "Nebula",
    "Nobbler",
    "Nocturne",
    "Nostrum",
    "Obelisk",
    "Octave",
    "Oeuvre",
    "Officiant",
    "Ohmmeter",
    "Olinary",
    "Omnibus",
    "Omphal",
    "Ophicleide",
    "Ossiferous",
    "Pabulum",
    "Paduasoy",
    "Parterre"]
def get_words_of_length(word_list, length):
    return [word for word in word_list if len(word) == length]
def get_matching_words(word_list, pattern):
    matching_words = []
    for word in word_list:
        matches = True
        for i, char in enumerate(pattern):
            if char != '_' and char != word[i]:
                matches = False
                break
        if matches:
            matching_words.append(word)
    return matching_words
def get_new_pattern(pattern, guessed_char, candidate_word):
    new_pattern = []
    for i in range(len(pattern)):
        if candidate_word[i] == guessed_char:
            new_pattern.append(guessed_char)
        else:
            new_pattern.append(pattern[i])
    return "".join(new_pattern)
def play_impossible_hangman(word_list):
    print("Welcome to Impossible Hangman! You get 10 tries to guess our unguessable word!(Created By Jalen Reid and Jaqueline Assiri)")
    word_length = random.choice([len(word) for word in word_list])
    possible_words = get_words_of_length(word_list, word_length)
    pattern = "_" * word_length
    guessed_chars = []
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and "_" in pattern:
        print("\nPattern:", " ".join(pattern))
        guess = input("Guess a Letter: ").lower()
        if guess in guessed_chars:
            print("YOU ALREADY GUESSED THAT, TRY AGAIN.")
            continue
        guessed_chars.append(guess)
        pattern_groups = defaultdict(list)
        for word in possible_words:
            new_pattern = get_new_pattern(pattern, guess, word)
            pattern_groups[new_pattern].append(word)
        largest_group_pattern = max(pattern_groups, key=lambda k: len(pattern_groups[k]))
        possible_words = pattern_groups[largest_group_pattern]
        if pattern == largest_group_pattern:
            print(f"AHHH HHAAAAAA WRONG LETTER TRY AGAIN")
            attempts += 1
        else:
            pattern = largest_group_pattern

        print("Guessed chars:", ", ".join(guessed_chars))
        print("Attempts left:", max_attempts - attempts)

    if "_" not in pattern:
        print("\nShocker, you guessed our word. Congratulations!:", pattern)
    else:
        print("\nWOMPPP WOMPPP WOMPPP WOMPPP YOU LOST >:) Your word could have been", possible_words, "But I guess we'll never know. TRY AGAIN IF YOU DARE.")
play_impossible_hangman(word_list)
