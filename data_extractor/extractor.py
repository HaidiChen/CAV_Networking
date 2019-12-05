from line_processor import LineProcessor
from path_helper import PathHelper
from field_writer import FieldWriter

class Extractor(object):
    
    @staticmethod
    def extract_data_to_csv_from_folder(path):
        Extractor._extract_from_path(path)
        FieldWriter.write_data_to_files()

    @staticmethod
    def _extract_from_path(path):
        if PathHelper.is_file(path):
            Extractor._extract_from_file(path)
        else: 
            Extractor._extract_from_folder(path)

    @staticmethod
    def _extract_from_file(path):
        key = PathHelper.get_dictionary_key(path) 
        file_path = PathHelper.get_absolute_path(path)
        lines = PathHelper.get_lines_from_file(file_path)
        Extractor._write_data(lines, key)

    @staticmethod
    def _extract_from_folder(folderPath):
        for named_file in PathHelper.get_files_under_path(folderPath):
            new_path = PathHelper.join_path(folderPath, named_file)
            Extractor._extract_from_path(new_path)

    @staticmethod
    def _write_data(lines, key):
        LineProcessor.process_lines(lines)
        FieldWriter.set_field_key(key)
        LineProcessor.reset_line_processors()

