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

class _Default(object):

    def __init__(self):
        self._field_dictionary = defaultdict(list)
        self._file_name = ''
        self._line_symbol = ''

    def write_value_of_key(self, key):
        pass

    def get_field_param(self):
        line_processor = LineProcessorFactory.get_field_line_processor(self)

        return line_processor.get_params()

    def get_line_symbol(self):
        return self._line_symbol

    def get_file_name(self):
        return self._file_name

    def get_columns(self):
        return DictionaryHandler.get_column_string(self._field_dictionary)

    def get_values(self):
        return DictionaryHandler.get_value_list(self._field_dictionary)

class _BroadcastField(_Default):

    def __init__(self):
        super().__init__()
        self._file_name = 'broadcast_time.csv'
        self._line_symbol = 'Broadcasting Time'

    def write_value_of_key(self, key):
        broadcast_numbers = self.get_field_param()[1]
        if broadcast_numbers:
            self._write_field_data(key)

    def _write_field_data(self, key):
        total_broadcast_time, broadcast_numbers = self.get_field_param()
        average_time = total_broadcast_time / broadcast_numbers
        self._field_dictionary[key].append(round(average_time, 5))

class _MseField(_Default):

    def __init__(self, file_received_field):
        super().__init__()
        self._file_received_field = file_received_field
        self._file_name = 'mse.csv'
        self._line_symbol = 'mse'

    def write_value_of_key(self, key):
        received_number = self._get_other_fields_param()
        if received_number:
            self._write_field_data(key)

    def _write_field_data(self, key):
        total_mse = self.get_field_param()
        received_number = self._get_other_fields_param()
        self._field_dictionary[key].append(total_mse / received_number)

    def _get_other_fields_param(self):
        return self._file_received_field.get_field_param()
    
class _SsimField(_Default):

    def __init__(self, file_received_field):
        super().__init__()
        self._file_received_field = file_received_field
        self._file_name = 'ssim.csv'
        self._line_symbol = 'ssim'

    def write_value_of_key(self, key):
        received_number = self._get_other_fields_param()
        if received_number:
            self._write_field_data(key)

    def _write_field_data(self, key):
        total_ssim = self.get_field_param()
        received_number = self._get_other_fields_param()
        self._field_dictionary[key].append(total_ssim / received_number)

    def _get_other_fields_param(self):
        return self._file_received_field.get_field_param()

class _MseSsimField(_Default):

    def __init__(self):
        super().__init__()
        self._line_symbol = 'MSE'

class _FileLossField(_Default):

    def __init__(self):
        super().__init__()
        self._line_symbol = 'File Loss'

class _FileLossRateField(_Default):

    def __init__(self,file_loss_field, file_received_field):
        super().__init__()
        self._file_loss_field = file_loss_field
        self._file_received_field = file_received_field
        self._file_name = 'file_loss_rate.csv'

    def write_value_of_key(self, key):
        loss_rate = self.get_field_param()
        if loss_rate != -1:
            self._field_dictionary[key].append(loss_rate)

    def get_field_param(self):
        lost_number, received_number = self._get_other_fields_param()
        desired_number = lost_number + received_number
        if desired_number:
            return round(lost_number / desired_number, 3)
        return -1

    def _get_other_fields_param(self):
        lost_number = self._file_loss_field.get_field_param()
        received_number = self._file_received_field.get_field_param()
        return (lost_number, received_number)

class _FileReceivedField(_Default):

    def __init__(self):
        super().__init__()
        self._line_symbol = 'files'
   
class _TestField(_Default):

    def __init__(self):
        super().__init__()
        self._file_name = 'test_field.csv'
        self._line_symbol = 'TestField'

    def write_value_of_key(self, key):
        test_field_string = self.get_field_param()
        if test_field_string:
            self._write_field_data(key)
        
    def _write_field_data(self, key):
        test_field_string = self.get_field_param()
        self._field_dictionary[key].append(test_field_string)
    
class _InstrMissRateField(_Default):

    def __init__(self):
        super().__init__()
        self._file_name = 'instr_miss_rate.csv'
        self._line_symbol = 'i Demand miss rate'

    def write_value_of_key(self, key):
        miss_rate = self.get_field_param()
        if miss_rate:
            self._write_field_data(key)

    def _write_field_data(self, key):
        miss_rate = self.get_field_param()
        self._field_dictionary[key].append(miss_rate)

class _InstrNumberField(_Default):

    def __init__(self):
        super().__init__()
        self._line_symbol = 'iDemand Fetches'

    def get_line_symbol(self):
        return self._line_symbol

class _DataNumberField(_Default):

    def __init__(self):
        super().__init__()
        self._line_symbol = 'dDemand Fetches'

class _DataPercentageField(_Default):

    def __init__(self, instr_number_field, data_number_field):
        super().__init__()
        self._instr_number_field = instr_number_field
        self._data_number_field = data_number_field
        self._file_name = 'data_percentage.csv'

    def write_value_of_key(self, key):
        percentage = self.get_field_param()
        if percentage != -1:
            self._field_dictionary[key].append(percentage)
    
    def get_field_param(self):
        instr_number, data_number = self._get_other_fields_param()
        total_number = instr_number + data_number
        if total_number:
            percentage = data_number / total_number
            return round(percentage, 4)
        return -1

    def _get_other_fields_param(self):
        instr_number = self._instr_number_field.get_field_param()
        data_number = self._data_number_field.get_field_param()

        return (instr_number, data_number)

class _DataMissRateField(_Default):

    def __init__(self):
        super().__init__()
        self._file_name = 'data_miss_rate.csv'
        self._line_symbol = 'd Demand miss rate'

    def write_value_of_key(self, key):
        miss_rate = self.get_field_param()
        if miss_rate:
            self._write_field_data(key)

    def _write_field_data(self, key):
        miss_rate = self.get_field_param()
        self._field_dictionary[key].append(miss_rate)

class _Level2MissRateField(_Default):

    def __init__(self):
        super().__init__()
        self._file_name = 'l2_miss_rate.csv'
        self._line_symbol = '2 Demand miss rate'

    def write_value_of_key(self, key):
        miss_rate = self.get_field_param()
        if miss_rate:
            self._write_field_data(key)

    def _write_field_data(self, key):
        miss_rate = self.get_field_param()
        self._field_dictionary[key].append(miss_rate)

class DefaultField(object):

    instance = _Default()

    def __new__(cls):
        return cls.instance

class FileReceivedField(DefaultField):

    instance = _FileReceivedField()

class BroadcastField(DefaultField):
    
    instance = _BroadcastField()

class MseField(DefaultField):

    instance = _MseField(FileReceivedField())

class SsimField(DefaultField):

    instance = _SsimField(FileReceivedField())

class FileLossField(DefaultField):

    instance = _FileLossField()
    
class MseSsimField(DefaultField):

    instance = _MseSsimField()

class FileLossRateField(DefaultField):

    instance = _FileLossRateField(FileLossField(), FileReceivedField())

class TestField(DefaultField):

    instance = _TestField()

class InstrMissRateField(DefaultField):

    instance = _InstrMissRateField()

class InstrNumberField(DefaultField):

    instance = _InstrNumberField()

class DataMissRateField(DefaultField):

    instance = _DataMissRateField()

class DataNumberField(DefaultField):

    instance = _DataNumberField()

class DataPercentageField(DefaultField):

    instance = _DataPercentageField(InstrNumberField(), DataNumberField())

class Level2MissRateField(DefaultField):

    instance = _Level2MissRateField()
