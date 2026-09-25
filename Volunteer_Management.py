events=[]
volunteers=[]
assignments=[]
def add_event():
 try:
    name=input ("event name:")
    date=input("date:")
    venue=input("venue:")
    events.append([len(events)+1,name,date,venue])
    print("event added successfully!")
 except:
   print("invalid output!")
def add_volunteer():
  name=input("volunteer name:")
  room=input("hostel room:")
  skill=input("skill:")
  volunteers.append([len(volunteers)+1,name,room,skill])
  print("volunteer added successfully!")
def assign_volunteer():
  if not events or not volunteers:
      print("add event and volunteer first.")
      return
  e=int(input("event id:"))
  v=int(input("volunteer id:"))
  role=input("assigned duty:")
  if e <=len(events) and v<=len(volunteers):
     assignments.append([e,v,role])
     print("volunteer assigned!")
  else:
     print("invalid id!")
def report():
     print("\n event report")
     for e in events:
       count=sum(1 for a in assignments if a[0]==e[0])
       print(e[0],e[1],"|",e[2],"| volunteers:",count)      
while True:
   print("\n 1.add event 2.add volunteer")
   print("3.assign volunteer 4.report 5.exit")
   choice = input("enter choice:")
   if choice=="1":
      add_event()
   elif choice=="2":
      add_volunteer()
   elif choice=="3":
      assign_volunteer()
   elif choice=="4":
      report()
   elif choice=="5":
      print("thank you!")
      break
   else:
      print("invalid choice")   
           
        