class LineProcessor(object):

    @classmethod
    def process_lines(cls, lines):
        for line in lines:
            cls._process_single_line(line)

    @classmethod
    def _process_single_line(cls, line):
        line_processor = LineProcessorFactory.get_line_processor(line)
        line_processor.retrieve_data()

    @classmethod
    def reset_line_processors(cls):
        cls.reset()

    @staticmethod
    def reset():
        for processor in LineProcessorFactory.get_all_line_processors():
            processor.reset()

class LineProcessorFactory(object):

    @classmethod
    def get_all_line_processors(cls):
        return [
                BroadcastLineProcessor(),
                FileReceivedLineProcessor(),
                FileLossLineProcessor(),
                MseSsimLineProcessor(),
                TestFieldLineProcessor(),
                ]

    @classmethod
    def get_broadcast_line_processor(cls):
        return BroadcastLineProcessor()

    @classmethod
    def get_file_received_line_processor(cls):
        return FileReceivedLineProcessor()

    @classmethod
    def get_file_loss_line_processor(cls):
        return FileLossLineProcessor()

    @classmethod
    def get_mse_ssim_line_processor(cls):
        return MseSsimLineProcessor()

    @classmethod
    def get_mse_line_processor(cls):
        return MseLineProcessor()

    @classmethod
    def get_ssim_line_processor(cls):
        return SsimLineProcessor()

    @classmethod
    def get_test_field_line_processor(cls):
        return TestFieldLineProcessor()

    @classmethod
    def get_line_processor(cls, line):
        if line.startswith('Broadcasting Time'):
            return BroadcastLineProcessor(line)

        elif line.endswith('files') or line.endswith('file'):
            return FileReceivedLineProcessor(line)

        elif line.startswith('File Loss'):
            return FileLossLineProcessor(line)

        elif line.startswith('MSE'):
            return MseSsimLineProcessor(line)

        elif line.startswith('TestField'):
            return TestFieldLineProcessor(line)

        else:
            return DefaultLineProcessor()

class DefaultLineProcessor(object):

    def retrieve_data(self):
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

