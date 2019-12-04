from line_processor import *
from collections import defaultdict

class FieldWriter(object):

    def __init__(self, fields=None):
        self._fields = fields 

    def add_field(self, field):
        self._fields.append(field)

    def set_field_key(self, key):
        for field in self._fields:
            field.write_value_of_key(key)

    def write_data_to_files(self):
        for field in self._fields:
            self._write_field(field)

    def _write_field(self, field):
        columns = field.get_columns()
        if columns:
            self._write_header(field)
            self._write_body(field)

    def _write_header(self, field):
        columns = field.get_columns()
        with open(field.get_file_name(), 'w') as f:
            f.write("%s\n"%(columns))

    def _write_body(self, field):
        values = field.get_values()
        for value_index in range(len(values[0])):
            data = self._get_prepared_data(values, value_index)
            self._write_prepared_data(field.get_file_name(), data)

    def _get_prepared_data(self, values, value_index):
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

    def _write_prepared_data(self, filename, data):
        with open(filename, 'a') as f:
            f.write("%s\n"%(data))

