tasks = input("Enter your tasks for today separated by a comma\n").split(", ")
done = []
ongoing = []
for each_task in tasks:
    print(each_task)
    responce = input(f"Did you finish {each_task} already? (yes, no) ").strip().lower()
    if responce == "yes":
        print("nice job")
        done.append(each_task)
    else:
        print("try not to put it off")
        ongoing.append(each_task)
    print("----------")
progress_checker = input("Do you want to see your today's progress (yes, no)\n").strip()
if progress_checker == "no":
    print("ok, enjoy your day's rest")
else:
    print(f"Done taks are {done}")
    print(f"ongoing tasks are {ongoing}")
    
