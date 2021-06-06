
#!/Users/anna/anaconda3/envs/cron/bin/python3
import os
import sys
from datetime import datetime as date


#
import main_utils as main_utils
import automatic_send.myemail as email
import automatic_send.mytext as text
import td_ameritrade.main_TD as TD
import algos.main_algo as algo


def main():

    args = main_utils.main_argparser()
    daily_mover = main_utils.set_env_variables(args)

    # Runs code for daily mover
    if daily_mover:
        print("Getting Daily Mover")
        # get data from TD
        COMPX_df ,DJI_df, SPX_df = TD.run(flag="Mover")
        # email and text reports
        email.send_email(COMPX_df ,DJI_df, SPX_df,subject = "Daily Movers Report")
        text.send_text(message = "Your Daily Mover Report has been E-mailed to you")
        print("Daily Mover Complete")

    algo.run()

    # TD.run(flag="nOne")
    # sys.exit()

    # email.send_email()
    # text.send_text()

if __name__ == '__main__':
    main()