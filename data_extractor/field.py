from collections import defaultdict
from line_processor import *

class DictionaryHandler(object):

    @classmethod
    def get_column_string(cls, dictionary):
        column_string = ''
        if dictionary:
            columns = list(dictionary.keys())
            column_string = ','.join(columns)

        return column_string

    @classmethod
    def get_value_list(cls, dictionary):
        values = []
        if dictionary:
            values = list(dictionary.values())

        return values

class BroadcastField(object):

    def __init__(self):
        self._broadcast_time = defaultdict(list)
        self._file_name = 'broadcast_time.csv'

    def write_value_of_key(self, key):
        broadcast_numbers = self.get_field_param()[1]
        if broadcast_numbers:
            self._write_field_data(key)

    def get_field_param(self):
        line_processor = LineProcessorFactory.get_broadcast_line_processor()

        return (line_processor.total_broadcast_time, 
                line_processor.lines_processed)

    def _write_field_data(self, key):
        total_broadcast_time, broadcast_numbers = self.get_field_param()
        average_time = total_broadcast_time / broadcast_numbers
        self._broadcast_time[key].append(round(average_time, 5))
 
    def _get_other_fields_param(self):
        pass

    def get_columns(self):
        return DictionaryHandler.get_column_string(self._broadcast_time)

    def get_values(self):
        return DictionaryHandler.get_value_list(self._broadcast_time)

    def get_file_name(self):
        return self._file_name
        
class MseField(object):

    def __init__(self, file_received_field):
        self._file_received_field = file_received_field
        self._mse = defaultdict(list)
        self._file_name = 'mse.csv'

    def write_value_of_key(self, key):
        received_number = self._get_other_fields_param()
        if received_number:
            self._write_field_data(key)

    def get_field_param(self):
        line_processor = LineProcessorFactory.get_mse_line_processor()

        return line_processor.total_mse

    def _write_field_data(self, key):
        total_mse = self.get_field_param()
        received_number = self._get_other_fields_param()
        self._mse[key].append(total_mse / received_number)

    def _get_other_fields_param(self):
        return self._file_received_field.get_field_param()

    def get_columns(self):
        return DictionaryHandler.get_column_string(self._mse)

    def get_values(self):
        return DictionaryHandler.get_value_list(self._mse)

    def get_file_name(self):
        return self._file_name
        
class SsimField(object):

    def __init__(self, file_received_field):
        self._file_received_field = file_received_field
        self._ssim = defaultdict(list)
        self._file_name = 'ssim.csv'

    def write_value_of_key(self, key):
        received_number = self._get_other_fields_param()
        if received_number:
            self._write_field_data(key)

    def get_field_param(self):
        line_processor = LineProcessorFactory.get_ssim_line_processor()

        return line_processor.total_ssim

    def _write_field_data(self, key):
        total_ssim = self.get_field_param()
        received_number = self._get_other_fields_param()
        self._ssim[key].append(total_ssim / received_number)

    def _get_other_fields_param(self):
        return self._file_received_field.get_field_param()

    def get_columns(self):
        return DictionaryHandler.get_column_string(self._ssim)

    def get_values(self):
        return DictionaryHandler.get_value_list(self._ssim)

    def get_file_name(self):
        return self._file_name
        
class FileLossField(object):

    def __init__(self, file_received_field):
        self._file_loss_rate = defaultdict(list)
        self._file_received_field = file_received_field
        self._file_name = 'file_loss_rate.csv'

    def write_value_of_key(self, key):
        lost_number = self.get_field_param()
        received_number = self._get_other_fields_param()
        desired_number = lost_number + received_number
        if desired_number:
            self._write_field_data(key)

    def get_field_param(self):
        line_processor = LineProcessorFactory.get_file_loss_line_processor()

        return line_processor.files_lost

    def _write_field_data(self, key):
        lost_number = self.get_field_param()
        received_number = self._get_other_fields_param()
        desired_number = lost_number + received_number
        loss_rate = lost_number / desired_number
        self._file_loss_rate[key].append(round(loss_rate, 3))

    def _get_other_fields_param(self):
        return self._file_received_field.get_field_param()

    def get_columns(self):
        return DictionaryHandler.get_column_string(self._file_loss_rate)

    def get_values(self):
        return DictionaryHandler.get_value_list(self._file_loss_rate)

    def get_file_name(self):
        return self._file_name
        
class FileReceivedField(object):

    def __init__(self):
        pass

    def write_value_of_key(self, key):
        pass
        
    def get_field_param(self):
        line_processor = LineProcessorFactory.get_file_received_line_processor()

        return line_processor.files_received

    def _write_field_data(self, key):
        pass

    def _get_other_fields_param(self):
        pass

    def get_columns(self):
        pass

    def get_values(self):
        pass

    def get_file_name(self):
        pass

class TestField(object):

    def __init__(self):
        self._file_name = 'test_field.csv'
        self._test_field = defaultdict(list)

    def write_value_of_key(self, key):
        test_field_string = self.get_field_param()
        if test_field_string:
            self._write_field_data(key)
        
    def get_field_param(self):
        line_processor = LineProcessorFactory.get_test_field_line_processor()

        return line_processor.test_field_string

    def _write_field_data(self, key):
        test_field_string = self.get_field_param()
        self._test_field[key].append(test_field_string)

    def _get_other_fields_param(self):
        pass

    def get_columns(self):
        return DictionaryHandler.get_column_string(self._test_field)

    def get_values(self):
        return DictionaryHandler.get_value_list(self._test_field)

    def get_file_name(self):
        return self._file_name
