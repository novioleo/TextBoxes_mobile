# Train on your own datasets

import argparse
from collections import OrderedDict
from logging import error


def parse_config_file(file_path):
    parameter_dict = OrderedDict()
    line_num = 1
    with open(file_path) as to_read:
        for m_line in to_read:
            try:
                if m_line.startswith('#'):
                    continue
                parameter_name_and_value = m_line.split('=')
                parameter_dict[parameter_name_and_value[0]] = parameter_name_and_value[1]
            except Exception as e:
                error('ERROR occur at line %d "%s":%s'%(line_num,m_line,e))
            line_num += 1
    return parameter_dict

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('--config_file',required = True,help='the train parameter file')
    opt = arg.parse_args()
    parameters = parse_config_file(opt.config_file)
