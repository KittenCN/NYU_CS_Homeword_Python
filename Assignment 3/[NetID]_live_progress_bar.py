import time

process_char = '#'
fill_char = '-'
sub_width = 50
times = int(input("How many times should the bar update? "))
total_orders = int(input("How many \"tasks\" should be performed? "))
if times > total_orders:
    done = total_orders
else:
    done = times
begin_orders = 0
per = sub_width // done
permod = sub_width % done

for i in range(1, done + 1):
    if permod > 0:
        divnum = done + 1
    else:
        divnum = done
    sub_string = "Progress |{0}{1}| {2}% completed".format(process_char * i * per, fill_char * (sub_width - (i * per)), "{0:.2f}".format(i / divnum * 100))
    print(sub_string, end='\r')
    time.sleep(0.5)
if permod > 0:
    sub_string = "Progress |{0}{1}| {2}% completed".format(process_char * sub_width, fill_char * 0, "{0:.2f}".format(100))
    print(sub_string, end='\r')
print("")
print("All done: {0} tasks performed".format(total_orders))