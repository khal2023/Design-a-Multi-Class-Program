class DiaryEntry:
    def __init__(self, name, contents):
        if type(name) == str and type(contents) == str:
            self.name = name
            self.contents = contents
            self.contact = None
        else:
            raise Exception("Names and contents of entries must be in string format.")

    def calculate_length(self):
        return len(self.contents.split())
    
    def add_contact(self, contact):
        self.contact = contact

class Task:
    def __init__(self, task):
        self.task = task
        self.complete = False

    def mark_complete(self):
        if not self.complete:
            self.complete = True
        else:
            raise Exception("This task has already been completed.")

    def mark_incomplete(self):
        if self.complete:
            self.complete = False
        else:
            raise Exception("This task is already marked as incomplete.")

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

