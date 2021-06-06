import argparse
import os
import sys

def main_argparser():

   

    parser = argparse.ArgumentParser()

    parser.add_argument("-daily_mover", 
                        required = False,
                        action = 'store',
                        default = False,
                        help="will send daily mover info")

    # parser.add_argument("-output_path", 
    #                     required = False,
    #                     action = 'store',
    #                     help="path to to store result")



    args = parser.parse_args()

    return args


def set_env_variables(args):
    """[Takes the NameSpaces args and turns them into env args]

    Args:
        args ([Namespace]): [Namespace args]
    """

    daily_mover = args.daily_mover
    #os.environ['daily_mover']  = daily_mover

    return daily_mover
    # if data path does not exist, throw error
    # data_path = args.data_path
    # os.environ['data_path'] = data_path

    # if not os.path.exists(data_path):
    #     print("\nERROR\nThe data_path does not point to a correct data file. Please try again\n")
    #     sys.exit()

    # output_path = args.output_path
    # os.environ['output_path'] = output_path
    # # creates output folder location if it does not already exist
    # if not os.path.isdir(output_path):
    #     os.mkdir(output_path)
