class InstrNumberLineProcessor(object):

    number = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        instr_number = self._get_number()
        InstrNumberLineProcessor.number = instr_number

    def _get_number(self):
        return float(self.line.split()[2])

    def reset(self):
        InstrNumberLineProcessor.number = 0

class DataNumberLineProcessor(object):

    number = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        data_number = self._get_number()
        DataNumberLineProcessor.number = data_number

    def _get_number(self):
        return float(self.line.split()[2])

    def reset(self):
        DataNumberLineProcessor.number = 0

class InstrMissRateLineProcessor(object):

    miss_rate = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        miss_rate = self._get_miss_rate()
        InstrMissRateLineProcessor.miss_rate = miss_rate

    def _get_miss_rate(self):
        return float(self.line.split()[4])

    def reset(self):
        InstrMissRateLineProcessor.miss_rate = 0

class DataMissRateLineProcessor(object):

    miss_rate = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        miss_rate = self._get_miss_rate()
        DataMissRateLineProcessor.miss_rate = miss_rate

    def _get_miss_rate(self):
        return float(self.line.split()[4])

    def reset(self):
        DataMissRateLineProcessor.miss_rate = 0

class Level2MissRateLineProcessor(object):

    miss_rate = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        miss_rate = self._get_miss_rate()
        Level2MissRateLineProcessor.miss_rate = miss_rate

    def _get_miss_rate(self):
        return float(self.line.split()[4])

    def reset(self):
        Level2MissRateLineProcessor.miss_rate = 0

class DefaultLineProcessor(object):

    def retrieve_data(self):
        pass

    def reset(self):
        pass

class BroadcastLineProcessor(object):

    total_broadcast_time = 0
    lines_processed = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        BroadcastLineProcessor.lines_processed += 1
        time = self._get_time()
        BroadcastLineProcessor.total_broadcast_time += time

    def _get_time(self):
        return float(self.line.split(':')[1])

    def reset(self):
        BroadcastLineProcessor.total_broadcast_time = 0
        BroadcastLineProcessor.lines_processed = 0

class FileReceivedLineProcessor(object):

    files_received = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        FileReceivedLineProcessor.files_received = self._get_files_number()

    def _get_files_number(self):
        files_string = self.line.split(',')[1]
        files_number = files_string.split()[0]
        files_number = int(files_number)

        return files_number

    def reset(self):
        FileReceivedLineProcessor.files_received = 0

class FileLossLineProcessor(object):

    files_lost = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        FileLossLineProcessor.files_lost = self._get_lost_number()

    def _get_lost_number(self):
        return int(self.line.split('=')[1])

    def reset(self):
        FileLossLineProcessor.files_lost = 0

class MseSsimLineProcessor(object):

    def __init__(self, line=None):
        self._mse_line_processor = MseLineProcessor(line)
        self._ssim_line_processor = SsimLineProcessor(line)

    def retrieve_data(self):
        self._mse_line_processor.retrieve_data()
        self._ssim_line_processor.retrieve_data()

    def _update_class_variable(self):
        MseSsimLineProcessor.total_mse = self._mse_line_processor.total_mse
        MseSsimLineProcessor.total_ssim = self._ssim_line_processor.total_ssim

    def reset(self):
        self._mse_line_processor.reset()
        self._ssim_line_processor.reset()

class MseLineProcessor(object):

    total_mse = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        MseLineProcessor.total_mse += self._get_mse()

    def _get_mse(self):
        mse_string = self._get_mse_string()
        mse = float(mse_string.split(':')[1])
        
        return mse

    def _get_mse_string(self):
        return self.line.split(',')[0]

    def reset(self):
        MseLineProcessor.total_mse = 0

class SsimLineProcessor(object):

    total_ssim = 0

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        SsimLineProcessor.total_ssim += self._get_ssim()

    def _get_ssim(self):
        ssim_string = self._get_ssim_string()
        ssim = float(ssim_string.split(':')[1])

        return ssim

    def _get_ssim_string(self):
        return self.line.split(',')[1]

    def reset(self):
        SsimLineProcessor.total_ssim = 0

class TestFieldLineProcessor(object):

    test_field_string = ''

    def __init__(self, line=None):
        self.line = line

    def retrieve_data(self):
        TestFieldLineProcessor.test_field_string = self._get_string()

    def _get_string(self):
        raw_string = self.line.split(':')[1]
        return raw_string.strip()

    def reset(self):
        TestFieldLineProcessor.test_field_string = ''

