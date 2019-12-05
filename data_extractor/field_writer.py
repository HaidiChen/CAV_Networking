from line_processor import *
from collections import defaultdict

class FieldWriter(object):

    _fields = []

    @classmethod
    def add_field(cls, field):
        FieldWriter._fields.append(field)

    @staticmethod
    def set_field_key(key):
        for field in FieldWriter._fields:
            field.write_value_of_key(key)

    @staticmethod
    def write_data_to_files():
        for field in FieldWriter._fields:
            FieldWriter._write_field(field)

    @staticmethod
    def _write_field(field):
        columns = field.get_columns()
        if columns:
            FieldWriter._write_header(field)
            FieldWriter._write_body(field)

    @staticmethod
    def _write_header(field):
        columns = field.get_columns()
        with open(field.get_file_name(), 'w') as f:
            f.write("%s\n"%(columns))

    @staticmethod
    def _write_body(field):
        values = field.get_values()
        for value_index in range(len(values[0])):
            data = FieldWriter._get_prepared_data(values, value_index)
            FieldWriter._write_prepared_data(field.get_file_name(), data)

    @staticmethod
    def _get_prepared_data(values, value_index):
        data = []
        for value in values:
            try:
                data.append(str(value[value_index]))
                data.append(',')
            except:
                data.append('N/A')
                data.append(',')

        del data[-1]
        data = ''.join(data)

        return data

    @staticmethod
    def _write_prepared_data(filename, data):
        with open(filename, 'a') as f:
            f.write("%s\n"%(data))

