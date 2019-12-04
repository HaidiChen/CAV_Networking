from line_processor import *
from path_helper import PathHelper
from field_writer import FieldWriter
from field import *

class Extractor(object):
    
    def __init__(self, field_writer):
        self._field_writer = field_writer

    def extract_data_to_csv_from_folder(self, path):
        self._extract_from_path(path)
        self._field_writer.write_data_to_files()

    def _extract_from_path(self, path):
        if PathHelper.is_file(path):
            self._extract_from_file(path)
        else: 
            self._extract_from_folder(path)

    def _extract_from_file(self, path):
        key = PathHelper.get_dictionary_key(path) 
        file_path = PathHelper.get_absolute_path(path)
        lines = PathHelper.get_lines_from_file(file_path)
        self._write_data(lines, key)

    def _extract_from_folder(self, folderPath):
        for named_file in PathHelper.get_files_under_path(folderPath):
            new_path = PathHelper.join_path(folderPath, named_file)
            self._extract_from_path(new_path)

    def _write_data(self, lines, key):
        LineProcessor.process_lines(lines)
        self._field_writer.set_field_key(key)
        LineProcessor.reset_line_processors()

def main():
    file_received_field = FileReceivedField()
    fields = [
            BroadcastField(), 
            file_received_field,
            MseField(file_received_field), 
            SsimField(file_received_field), 
            FileLossField(file_received_field), 
            ]

    field_writer = FieldWriter(fields)
    extractor = Extractor(field_writer)

    print('[INFO] start extracting...')

    path_folder_to_start = '../N2NTest/log'
    extractor.extract_data_to_csv_from_folder(path_folder_to_start)

    print('[INFO] done')

if __name__ == '__main__':
    main()
