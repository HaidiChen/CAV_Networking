from line_processor_types import *
from collections import defaultdict
from line_processor_types import DefaultLineProcessor

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
        for processor in LineProcessorFactory.get_all_line_processors():
            processor.reset()

class LineProcessorFactory(object):

    processors = defaultdict(DefaultLineProcessor)

    @classmethod
    def get_all_line_processors(cls):
        return list(LineProcessorFactory.processors.values())

    @classmethod
    def get_field_line_processor(cls, field):
        key = cls._get_dictionary_key(field)
        return LineProcessorFactory.processors[key]
        
    @classmethod
    def add_line_processor(cls, field, line_processor):
        key = cls._get_dictionary_key(field)
        LineProcessorFactory.processors[key] = line_processor

    @classmethod
    def _get_dictionary_key(cls, field):
        key = field.get_line_symbol()
        # if 'key' is an empty string, give a random and unique value to it.
        # Because the 'key' is also the 'line_symbol', if we keep it as an empty
        # string, statement in line [57] is always true, and until the end of the
        # program, we will always get the default line processor which does 
        # nothing returned to the call in line [14] and outputs nothing.
        if not key:
            return 'default' 

        return key

    @classmethod
    def get_line_processor(cls, line):
        line_symbols = list(LineProcessorFactory.processors.keys())
        for line_symbol in line_symbols:
            if line.startswith(line_symbol) or line.endswith(line_symbol):
                return cls._get_line_set_processor_from_key(line_symbol, line)

        return DefaultLineProcessor()

    @classmethod
    def _get_line_set_processor_from_key(cls, key, line):
        line_processor = LineProcessorFactory.processors[key]
        line_processor.line = line
        return line_processor
