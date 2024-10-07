import pytest
from lib.planner import *
from lib.planner_helper_classes import*


# Word blocks
_10_words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a."    
_50_words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Pellentesque leo enim, egestas aliquam vehicula rhoncus, tempor vitae justo. Sed 
tincidunt dui commodo, molestie orci sed, ullamcorper eros. Etiam nibh eros, consequat 
sit amet pulvinar non, faucibus non felis. Praesent faucibus a nibh ultricies consectetur. 
Nulla fringilla, elit non accumsan condimentum."""
_100_words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean efficitur 
iaculis mauris, in suscipit sapien rhoncus nec. Sed sodales elit in lectus 
bibendum, a vestibulum mauris porttitor. Sed malesuada, ex eget elementum 
sollicitudin, erat eros ultricies velit, id varius orci ex a lacus. Vivamus 
a lectus metus. Donec eu commodo velit, non sodales tortor. Vestibulum ante 
ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris 
et nunc pretium libero pharetra ultricies sit amet a felis. Mauris pretium 
ipsum eget mi posuere ultricies. Etiam vel sapien dolor. Integer dapibus mi 
vel erat bibendum consequat. In laoreet est dui."""
_200_words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In id arcu odio. Nullam 
consectetur, turpis sed condimentum tempus, ex tellus feugiat felis, vel eleifend ex ex eu ante. 
Curabitur rutrum, neque non sollicitudin elementum, nulla augue scelerisque erat, eget mattis 
magna mi non lectus. Nulla non tortor in velit vulputate porttitor. Nam pellentesque ac odio a 
pretium. Aliquam a odio facilisis, vehicula sapien non, dignissim enim. Nunc tempor imperdiet lacinia. 
Vestibulum vel sem at ex placerat vulputate. Suspendisse iaculis, mi et varius condimentum, leo lorem 
pretium felis, eu tincidunt lectus risus in neque. In turpis tortor, pulvinar vel pellentesque vel, 
molestie a ligula. Donec non ligula vestibulum, hendrerit purus ac, maximus mi. Praesent dictum tellus 
et erat scelerisque  sollicitudin vitae eu diam. Curabitur vulputate arcu et ipsum malesuada, ut ornare 
sem sodales. Fusce eu efficitur lectus. Vestibulum semper cursus turpis, sit amet finibus metus consequat 
rutrum. Etiam volutpat imperdiet velit, eu maximus ante volutpat vitae. Ut vehicula lacus non nulla 
mattis molestie. Aliquam non dictum nulla. Phasellus commodo massa non justo faucibus, vitae malesuada 
felis vestibulum. Mauris rhoncus bibendum semper. Praesent feugiat, nibh sit amet pretium tempor, odio 
magna finibus ex, sit amet aliquam dui mauris in turpis. Nulla blandit."""

def test_add_diary_entry():
    planner = Planner()
    entry1 = DiaryEntry("Monday", _10_words)
    planner.add_diary_entry(entry1)
    assert planner.entries == [entry1]

def test_adds_multiple_entries():
    planner = Planner()
    entry1 = DiaryEntry("Monday", _10_words)
    entry2 = DiaryEntry("Tuesday", _50_words)
    entry3 = DiaryEntry("Wednesday", _100_words)
    planner.add_diary_entry(entry1)
    planner.add_diary_entry(entry2)
    planner.add_diary_entry(entry3)
    assert planner.entries == [entry1, entry2, entry3]

def test_only_adds_diary_entry_objects():
    planner = Planner()
    with pytest.raises(Exception) as e:
        planner.add_diary_entry(7)
    assert str(e.value) == "DiaryEntry type only"

def test_diary_returns_a_list_of_names_of_added_entries():
    planner = Planner()
    entry1 = DiaryEntry("Monday", _10_words)
    entry2 = DiaryEntry("Tuesday", _50_words)
    entry3 = DiaryEntry("Wednesday", _100_words)
    planner.add_diary_entry(entry1)
    planner.add_diary_entry(entry2)
    planner.add_diary_entry(entry3)
    assert planner.list_entries_by_name() == ["Monday", "Tuesday", "Wednesday"] 
    
def test_diary_returns_entry_based_on_name():
    planner = Planner()
    entry1 = DiaryEntry("Monday", _10_words)
    entry2 = DiaryEntry("Tuesday", _50_words)
    entry3 = DiaryEntry("Wednesday", _100_words)
    planner.add_diary_entry(entry1)
    planner.add_diary_entry(entry2)
    planner.add_diary_entry(entry3)
    assert planner.select_entry_by_name("Monday") == _10_words

def test_diary_returns_list_of_available_entries_if_name_not_found():
    planner = Planner()
    entry1 = DiaryEntry("Monday", _10_words)
    entry2 = DiaryEntry("Tuesday", _50_words)
    entry3 = DiaryEntry("Wednesday", _100_words)
    planner.add_diary_entry(entry1)
    planner.add_diary_entry(entry2)
    planner.add_diary_entry(entry3)
    assert planner.select_entry_by_name("Thursday") == "Available entries: Monday, Tuesday, Wednesday"
    
def test_diary_returns_entries_by_closest_read_time():
    planner = Planner()
    entry1 = DiaryEntry("Monday", _10_words)
    entry2 = DiaryEntry("Tuesday", _50_words)
    entry3 = DiaryEntry("Wednesday", _100_words)
    planner.add_diary_entry(entry1)
    planner.add_diary_entry(entry2)
    planner.add_diary_entry(entry3)
    assert planner.select_entry_by_read_time(45, 2) == entry2
    
def test_planner_returns_list_of_contacts_and_numbers():
    planner = Planner()
    John = Contact("John", "1234-123-123")
    Hakim = Contact("Hakim", "1435-555-555")
    entry1 = DiaryEntry("Monday", _10_words)
    entry2 = DiaryEntry("Tuesday", _50_words)
    entry3 = DiaryEntry("Wednesday", _100_words)
    planner.add_diary_entry(entry1)
    planner.add_diary_entry(entry2)
    planner.add_diary_entry(entry3)
    entry1.add_contact(John)
    entry2.add_contact(Hakim)
    assert planner.list_stored_numbers() == {"John": "1234-123-123", "Hakim": "1435-555-555"}

def test_adds_tasks_to_task_list():
    planner = Planner()
    task1 = Task("Take out the trash")
    task2 = Task("Walk the dog")
    task3 = Task("Wash the cat")
    planner.add_task(task1)
    planner.add_task(task2)
    planner.add_task(task3)
    assert planner.tasks == [task1, task2, task3]

def test_lists_incomplete_tasks():
    planner = Planner()
    task1 = Task("Take out the trash")
    task2 = Task("Walk the dog")
    task3 = Task("Wash the cat")
    planner.add_task(task1)
    planner.add_task(task2)
    planner.add_task(task3)
    assert planner.list_incomplete_tasks() == [task1, task2, task3]

def test_marks_all_complete():
    planner = Planner()
    task1 = Task("Take out the trash")
    task2 = Task("Walk the dog")
    task3 = Task("Wash the cat")
    planner.add_task(task1)
    planner.add_task(task2)
    planner.add_task(task3)
    planner.clear_all_tasks()
    assert planner.list_incomplete_tasks() == []