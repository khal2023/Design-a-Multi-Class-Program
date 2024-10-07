from lib.planner_helper_classes import*
class Planner:
    def __init__(self):
        self.entries = []
        self.tasks = []

    def add_diary_entry(self, entry):
        if isinstance(entry, DiaryEntry):
            self.entries.append(entry)
        else:
            raise Exception("DiaryEntry type only")

    def list_entries_by_name(self):
        return [entry.name for entry in self.entries]

    def select_entry_by_name(self, entry_name):
        for entry in self.entries:
            if entry.name == entry_name:
                return entry.contents
        return (f"Available entries: {", ".join([entry.name for entry in self.entries])}")
            
    def select_entry_by_read_time(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        best_entries = {entry: entry.calculate_length() for entry in self.entries if entry.calculate_length() <= words_user_can_read}
        return max(best_entries, key=best_entries.get)

    def list_stored_numbers(self):
        return {entry.contact.name: entry.contact.number for entry in self.entries if entry.contact != None}

    def add_task(self, task):
        self.tasks.append(task)

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if not task.complete]

    def list_complete_tasks(self):
        return [task for task in self.tasks if task.complete]

    def clear_all_tasks(self):
        for task in self.tasks:
            if not task.complete:
                task.mark_complete()