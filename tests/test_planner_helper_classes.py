import pytest
from lib.planner_helper_classes import *

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


def test_initialise_diary_entry():
    diary = DiaryEntry("Monday", _10_words)
    assert diary.name == "Monday"
    assert diary.contents == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a."

def test_diaryentry_refuses_non_string_entries():
    with pytest.raises(Exception) as e:
        diary = DiaryEntry("Monday", 57)
    assert str(e.value) == "Names and contents of entries must be in string format."

def test_diaryentry_correctly_calculates_length():
    diary = DiaryEntry("Monday", _10_words)
    assert diary.calculate_length() == 10

def test_diary_entry_correctly_calculates_length_200():
    diary = DiaryEntry("Monday", _200_words)
    assert diary.calculate_length() == 200

def test_create_contact():
    contact = Contact("John", "1234-123-123")
    assert contact.name == "John"
    assert contact.number == "1234-123-123"

def test_diary_entry_correctly_adds_contact():
    diary = DiaryEntry("Monday", _200_words)
    contact = Contact("John", "1234-123-123")
    diary.add_contact(contact)
    assert diary.contact.name == "John"
    assert diary.contact.number == "1234-123-123"

def test_task_correctly_initialises():
    task = Task("Walk the dog")
    assert task.task == "Walk the dog"
    assert task.complete == False