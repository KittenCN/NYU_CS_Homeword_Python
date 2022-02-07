"""This program makes a BMP file with a plus sign of a specified color
Submitted by Mauricio Arias, NetID ma6918
"""
process_char = '>'
fill_char = '-'
sub_width = 50
total_orders = 10000
begin_orders = 0
per = sub_width / total_orders
finish_orders = int(input("Enter the number of orders to finish(0 - {0}): ".format(total_orders)))

fill_finish = int(per * begin_orders)
sub_string = "Progress |{0}{1}|".format(process_char * fill_finish, fill_char * (sub_width - fill_finish))
print("{0}".format("Snapshot 1"))
print(sub_string)
print()
fill_finish = int(per * finish_orders)
sub_string = "Progress |{0}{1}|".format(process_char * fill_finish, fill_char * (sub_width - fill_finish))
print("{0}".format("Snapshot 2"))
print(sub_string)
