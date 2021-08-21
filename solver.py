import fileinput
import os
import itertools
import time

def get_words():
    valid_words = set()
    with open(resource_path("words.txt")) as dict_words:
      for dict_word in dict_words:
        dict_word = dict_word.strip()
        if(len(dict_word) <= 7 and len(dict_word) >= 3):
          valid_words.add(dict_word)

    print ("Enter the available letters (q to quit):")
    for line in fileinput.input():
        line = line.strip()
        if(line == "q"):
          os.sys.exit()
        
        for word_length in range(3, len(line) + 1):
            # t0 = time.time()
            words = set()
            for word_tuple in itertools.permutations(line, word_length):
                word_string = ''.join(word_tuple)

                if (word_string in valid_words):
                    words.add(word_string)

            print("Matching {} letter words:".format(word_length))
            for word in words:
                print("\t {}".format(word))
            # print("time elapsed: " + str(time.time() - t0) + "\n")
        print ("\nEnter more available letters (q to quit):")

def resource_path(relative):
  bundle_dir = getattr(os.sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
  return os.path.abspath(os.path.join(bundle_dir, relative))

if __name__ == "__main__":
    get_words()
