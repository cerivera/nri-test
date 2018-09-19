import csv
import math
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
          'standards': {},
          'questions': {}
        }

      if standard_id not in strands[strand_id]['standards']:
        strands[strand_id]['standards'][standard_id] = {
          'name': standard_name,
          'questions': {}
        }

      question = {'difficulty': float(difficulty)}
      strands[strand_id]['questions'][question_id] = question
      strands[strand_id]['standards'][standard_id]['questions'][question_id] = question
  return strands

def sort_strand_ids_by_questions_count(taxonomy):
  num_questions_by_strand = {}
  for strand_id in taxonomy.keys():
    num_questions_by_strand[strand_id] = len(taxonomy[strand_id]['questions'])

  return sorted(num_questions_by_strand, key=num_questions_by_strand.__getitem__)

def find_questions_in_strand(taxonomy, strand_id, count):
  return list(taxonomy[strand_id]['questions'])[:count]

def pick_questions(taxonomy, count):
  num_strands = len(taxonomy.keys())
  results_per_strand = math.floor(count/num_strands)

  results = []
  strand_iteration = 0
  for strand_id in sort_strand_ids_by_questions_count(taxonomy):
    strand_iteration += 1
    results = results + list(taxonomy[strand_id]['questions'])[:results_per_strand]
    if len(results) != count:
      results_per_strand = math.floor((count-len(results))/(num_strands-strand_iteration))

  return results

if __name__ == '__main__':
  if len(sys.argv) <= 1 or not sys.argv[1].isdigit():
    print("Usage: python3 questions_picker.py <NUMBER OF QUESTIONS>")
    sys.exit()

  num_questions = int(sys.argv[1])

  taxonomy = load_taxonomy_from_csv('questions.csv')

  questions = pick_questions(taxonomy, num_questions)

  print(','.join(questions))
