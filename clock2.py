from apscheduler.schedulers.blocking import BlockingScheduler
from economic2 import send_message
from economic2 import send_message2
from economic2 import mandarvariosmensajes

sched = BlockingScheduler()

# Schedules job_function to be run on 
#tener en cuenta q timezone es utc por lo cual hour=10 es 7 am, 3 hs adelantado
#sched.add_job(mandarvariosmensajes, 'interval',second='0',timezone='utc')
sched.add_job(mandarvariosmensajes,"cron",minute=0,timezone="UTC")
sched.start()