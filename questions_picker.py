import csv
import sys

def load_taxonomy_from_csv(filename):
  strands = {}
  with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      strand_id = row['strand_id']
      strand_name = row['strand_name']
      standard_id = row['standard_id']
      standard_name = row['standard_name']
      question_id = row['question_id']
      difficulty = row['difficulty']

      if strand_id not in strands:
        strands[strand_id] = {
          'name': strand_name,
          'standards': {}
        }

      if standard_id not in strands[strand_id]['standards']:
        strands[strand_id]['standards'][standard_id] = {
          'name': standard_name,
          'questions': {}
        }

      strands[strand_id]['standards'][standard_id]['questions'][question_id] = {
        'difficulty': float(difficulty)
      }

  return strands


def pick_questions(count):
  # TODO
  return list(map(str, range(0, count)))

if __name__ == '__main__':
  if len(sys.argv) <= 1 or not sys.argv[1].isdigit():
    print("Usage: python3 questions_picker.py <NUMBER OF QUESTIONS>")
    sys.exit()

  taxonomy = load_taxonomy_from_csv('questions.csv')

  num_questions = int(sys.argv[1])
  questions_list = pick_questions(num_questions)
  print(','.join(questions_list))


"""
{'1': {'name': 'Nouns',
       'standards': {'1': {'name': 'Common Nouns',
                           'questions': {'1': {'difficulty': 0.7},
                                         '2': {'difficulty': 0.6}}},
                     '2': {'name': 'Abstract Nouns',
                           'questions': {'3': {'difficulty': 0.8}}},
                     '3': {'name': 'Proper Nouns',
                           'questions': {'4': {'difficulty': 0.2},
                                         '5': {'difficulty': 0.5},
                                         '6': {'difficulty': 0.4}}}}},
 '2': {'name': 'Verbs',
       'standards': {'4': {'name': 'Action Verbs',
                           'questions': {'7': {'difficulty': 0.9},
                                         '8': {'difficulty': 0.1}}},
                     '5': {'name': 'Transitive Verbs',
                           'questions': {'10': {'difficulty': 0.6},
                                         '11': {'difficulty': 0.4},
                                         '9': {'difficulty': 0.3}}},
                     '6': {'name': 'Reflexive Verbs',
                           'questions': {'12': {'difficulty': 0.2}}}}}}
"""
