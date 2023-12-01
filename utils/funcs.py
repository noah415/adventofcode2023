def get_input_lines(input_file: str) -> [str]:
  file: any = open(input_file, 'r')

  content: [str] = file.readlines()

  file.close()

  return content

class QueueObject:
  # lower number higher priority
  def __init__(self, priority: int, value: any):
    self.priority: int = priority
    self.value: any = value

class PriorityQueue:
  def __init__(self):
    self.objects: [QueueObject] = []

  def is_empty(self):
    return len(self.objects) == 0

  def dequeue_all(self):
    old_queue: [QueueObject] = self.objects
    self.objects = []

    return old_queue

  def enqueue(self, new_object: QueueObject) -> None:
    for i in range(len(self.objects)):
      object: QueueObject = self.objects[i]

      if object.priority > new_object.priority:
        self.objects = self.objects[:i] + [new_object] + self.objects[i:]
        break

      if object.priority == new_object.priority and i != (len(self.objects) - 1):
        self.objects = self.objects[:i+1] + [new_object] + self.objects[i+1:]
        break

      if i == (len(self.objects) - 1):
        self.objects.append(new_object)

  def dequeue(self) -> QueueObject:
    if self.is_empty():
      raise Exception('PriorityQueue error: nothing to dequeue. Queue is empty.')

    ret_val = self.objects[0]
    self.objects = self.objects[1:]

    return ret_val