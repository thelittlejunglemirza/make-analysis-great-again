import pandas as pd
import dateutil.parser


def get_date_quarter_label(date_string):
    date = dateutil.parser.parse(date_string)
    quarter_number = pd.Timestamp(date).quarter
    return '%d_Q%d' % (date.year, quarter_number)
