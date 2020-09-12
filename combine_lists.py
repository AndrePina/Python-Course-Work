# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

Jamies_list = []
Drews_list = []
newList1 = []
newList2 = []
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  # for i in range(0,10):
  	# print(i)
  	Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
  	Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
  	# print(len(Jamies_list))
  	# print(Drews_list[0])
  	
  	jamies_list = Jamies_list.reverse()
  	newList1.append(Drews_list)
  	newList1.append(Jamies_list)
  	print(newList1)
  	# 
  	# print(Jamies_list)
print(combine_lists(Jamies_list, Drews_list))
