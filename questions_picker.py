import sys

def pick_questions(count):
  # TODO
  return list(map(str, range(0, count)))

if __name__ == '__main__':
  if len(sys.argv) <= 1 or not sys.argv[1].isdigit():
    print("Usage: python3 questions_picker.py <NUMBER OF QUESTIONS>")
    sys.exit()

  num_questions = int(sys.argv[1])
  questions_list = pick_questions(num_questions)
  print(','.join(questions_list))

