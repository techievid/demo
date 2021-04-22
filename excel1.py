import argparse
import sys
import pandas as pd

class ex_utility:

     def file_read_utility(self, args):

        if args.file_path is not None:
            loc = args.file_path
            reader = pd.read_excel(loc, engine='openpyxl')
            '''print(f"These are Columns in Excel: {reader.columns}")
               print(reader['Name'][0])
               for i in reader:
               print(i)'''
            # new_reader =reader.set_index('Names')['ID'].to_dict()
            # new_reader =reader.to_dict('r')
            new_reader = reader.to_dict(orient = 'records')
            print(new_reader)

            return reader


if __name__ == '__main__':

    obj = ex_utility()
    # print(sys.argv[1])
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_path', help="This reads Excel file")

    args = arg_parser.parse_args()
    sys.stdout.write(str(obj.file_read_utility(args)))
