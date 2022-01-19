#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
#of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
#run to university. You jog the first mile at 7mph; then run the next two at15mph; before
#jogging the last at 7mph again. Will this be quicker or slower than the bus?

distfrom_uni=4
bus_speed=25
time_bus=(distfrom_uni%bus_speed)*60
#the bus stops at 10 places and takes 2 minutes at every stop. Thus the bus spends 20 minutes idle total
time_stop=20
total_time=time_bus+time_stop
print("the bus journey will take",total_time)
#if user decides to jog
jog_speed_1stmile=7 #jogs the first mile at 7mph
time_jog_1stmile=1/jog_speed_1stmile
time1=time_jog_1stmile*60
jog_speed_next2miles=15 #jogs the next two miles at 15mph
time_jog_next2miles=2/jog_speed_next2miles
time2=time_jog_next2miles*60
jog_speed_lastmile=7    #jogs the last mile again at 7mph
time_jog_lastmile=1/jog_speed_lastmile
time3=time_jog_lastmile*60
total_time1=time1+time2+time3
print("the total time taken for jogging is",total_time1)
if total_time1>total_time:
    print("the bus will reach the university quicker")
else:
    print("the university can be reached quicker by jogging")


