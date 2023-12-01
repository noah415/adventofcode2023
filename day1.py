'''
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

'''
My approach

We only need to get the first and last numeric character of each line. 

To guarantee that the resulting numbers are in fact "first" and "last", we can run 2 searches.
The first search looks for the first numeric character in given order.
The second search looks for the last numeric character in reverse order.

ex.

search1
-->!
pqr3stu8vwx

search2
       !<--
pqr3stu8vwx

result: 38
'''

from utils.funcs import get_input_lines, PriorityQueue, QueueObject
import sys

translator = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

def main():
  if len(sys.argv) == 1:
    part = 'part1'
    input_file = "./inputs/input1.txt"
  elif len(sys.argv) == 2:
    part = sys.argv[1]
    input_file = "./inputs/input1.txt"
  elif len(sys.argv) == 3:
    part = sys.argv[1]
    input_file = sys.argv[2]
  else:
    print('\nusage: python3 day1.py [part1 | part2 [<input_file_path>]]\n')
    return

  input1 = get_input_lines(input_file)
  sum = 0

  if part == 'part2':
    input1 = tokenize(input1)

  for line in input1:
    first_num = search_forward(line)
    last_num = search_backward(line)

    calibration_value = int(first_num + last_num)

    sum += calibration_value

  print('Answer: ' + str(sum))

def search_forward(line: str) -> str:
  for letter in line:
    if letter.isdigit():
      return letter

def search_backward(line: str) -> str:
  for i in range(-1, -len(line)-1, -1):
    letter: str = line[i]
    if letter.isdigit():
      return letter

def tokenize(input: [str]) -> [[str]]:
  new_input: [[str]] = []

  for line in input:
    # create a priority queue of tokens for each line
    queue: PriorityQueue = PriorityQueue()
    
    while contains_token(line):
      valid_token: QueueObject = find_next_valid_token(line, queue)
      idx: int = valid_token.priority
      token: str = valid_token.value

      line = update_line_with_token(line, token, idx)

      # reset queue after each iteration
      queue.dequeue_all()

    new_input.append(line)

  return new_input

def update_line_with_token(line: str, token: str, idx: int):
  '''
  idx: the index of the line where the token begins
  '''
  if (idx + len(token)) < len(line):
    return line[:idx] + translator[token] + line[(idx+len(token)):]
  # reached end of line
  else:
    return line[:idx] + translator[token]


def find_next_valid_token(line: str, queue: PriorityQueue) -> QueueObject:
  for token in translator.keys():
    idx: int = line.find(token)

    # if token is found...
    if idx != -1:
      # create queue object for every valid index
      object: QueueObject = QueueObject(token, idx)
      # enqueue object
      queue.enqueue(object)
  
  return queue.dequeue()

def contains_token(line: str) -> bool:
  for token in translator.keys():
    idx: int = line.find(token)

    if idx != -1:
      return True

  return False

if __name__ == "__main__":
  main()
