from copy import deepcopy

class DefaultLineProcessor(object):

    _params = ''
    _default_value = ''

    def __init__(self):
        self.line = ''

    def retrieve_data(self):
        pass

    @classmethod
    def get_params(cls):
        return cls._params

    @classmethod
    def reset(cls):
        cls._params = deepcopy(cls._default_value)

class InstrNumberLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        instr_number = self._get_number()
        InstrNumberLineProcessor._params = instr_number

    def _get_number(self):
        return float(self.line.split()[2])

class DataNumberLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        data_number = self._get_number()
        DataNumberLineProcessor._params = data_number

    def _get_number(self):
        return float(self.line.split()[2])

class InstrMissRateLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        miss_rate = self._get_miss_rate()
        InstrMissRateLineProcessor._params = miss_rate

    def _get_miss_rate(self):
        return float(self.line.split()[4])

class DataMissRateLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        miss_rate = self._get_miss_rate()
        DataMissRateLineProcessor._params = miss_rate

    def _get_miss_rate(self):
        return float(self.line.split()[4])

class Level2MissRateLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        miss_rate = self._get_miss_rate()
        Level2MissRateLineProcessor._params = miss_rate

    def _get_miss_rate(self):
        return float(self.line.split()[4])

class BroadcastLineProcessor(DefaultLineProcessor):

    # total_broadcast_time = _params[0],  lines_processed = _params[1]
    _params = [0, 0]
    _default_value = [0, 0]

    def retrieve_data(self):
        BroadcastLineProcessor._params[1] += 1
        time = self._get_time()
        BroadcastLineProcessor._params[0] += time

    def _get_time(self):
        return float(self.line.split(':')[1])

class FileReceivedLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        FileReceivedLineProcessor._params = self._get_files_number()

    def _get_files_number(self):
        files_string = self.line.split(',')[1]
        files_number = files_string.split()[0]
        files_number = int(files_number)

        return files_number

class FileLossLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        FileLossLineProcessor._params = self._get_lost_number()

    def _get_lost_number(self):
        return int(self.line.split('=')[1])

class MseSsimLineProcessor(DefaultLineProcessor):

    def __init__(self):
        self._mse_line_processor = MseLineProcessor()
        self._ssim_line_processor = SsimLineProcessor()

    def retrieve_data(self):
        self._mse_line_processor.line = self.line
        self._ssim_line_processor.line = self.line
        self._mse_line_processor.retrieve_data()
        self._ssim_line_processor.retrieve_data()

class MseLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        MseLineProcessor._params += self._get_mse()

    def _get_mse(self):
        mse_string = self._get_mse_string()
        mse = float(mse_string.split(':')[1])
        
        return mse

    def _get_mse_string(self):
        return self.line.split(',')[0]

class SsimLineProcessor(DefaultLineProcessor):

    _params = 0
    _default_value = 0

    def retrieve_data(self):
        SsimLineProcessor._params += self._get_ssim()

    def _get_ssim(self):
        ssim_string = self._get_ssim_string()
        ssim = float(ssim_string.split(':')[1])

        return ssim

    def _get_ssim_string(self):
        return self.line.split(',')[1]

class TestFieldLineProcessor(DefaultLineProcessor):

    _params = ''
    _default_value = ''

    def retrieve_data(self):
        TestFieldLineProcessor._params = self._get_string()

    def _get_string(self):
        raw_string = self.line.split(':')[1]
        return raw_string.strip()

class DataPercentageLineProcessor(DefaultLineProcessor):

    pass

class FileLossRateLineProcessor(DefaultLineProcessor):

    pass
