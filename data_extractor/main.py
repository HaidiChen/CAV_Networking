from field import *
from field_writer import FieldWriter
from line_processor import LineProcessorFactory
from extractor import Extractor
from collections import namedtuple

def main():
    fields_and_line_processors = setup_fields_and_line_processors()
    fields = get_fields(fields_and_line_processors)

    setup_line_processors(fields_and_line_processors)
    setup_field_writer(fields)

    print('[INFO] start extracting...')

    Extractor.extract_data_to_csv_from_folder('log')
    Extractor.extract_data_to_csv_from_folder('n2nlog')
    Extractor.extract_data_to_csv_from_folder('assoc1')

    print('[INFO] done')

def setup_fields_and_line_processors():
    fields_and_line_processors = [

            FieldProcessor(TestField(), TestFieldLineProcessor()),

            FieldProcessor(InstrNumberField(), InstrNumberLineProcessor()),
            FieldProcessor(DataNumberField(), DataNumberLineProcessor()),
            FieldProcessor(DataPercentageField(), DataPercentageLineProcessor()),
            FieldProcessor(InstrMissRateField(), InstrMissRateLineProcessor()),
            FieldProcessor(DataMissRateField(), DataMissRateLineProcessor()),
            FieldProcessor(Level2MissRateField(), Level2MissRateLineProcessor()),

            FieldProcessor(BroadcastField(), BroadcastLineProcessor()),
            FieldProcessor(FileLossField(), FileLossLineProcessor()),
            FieldProcessor(FileReceivedField(), FileReceivedLineProcessor()),
            FieldProcessor(FileLossRateField(), FileLossRateLineProcessor()),
            FieldProcessor(SsimField(), SsimLineProcessor()),
            FieldProcessor(MseField(), MseLineProcessor()),
            FieldProcessor(MseSsimField(), MseSsimLineProcessor()),

            ]

    return fields_and_line_processors

def setup_field_writer(fields):
    for field in fields:
        FieldWriter.add_field(field)

def setup_line_processors(fields_and_line_processors):
    for fp in fields_and_line_processors:
        LineProcessorFactory.add_line_processor(fp.field, fp.line_processor)

def get_fields(fields_and_line_processors):
    fields = [item.field for item in fields_and_line_processors]

    return fields

if __name__ == '__main__':
    FieldProcessor = namedtuple('FieldProcessor', ['field', 'line_processor'])
    main()
