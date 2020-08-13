from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from script_imovel import main

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', hours=4)

scheduler.start()