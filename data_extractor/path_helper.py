import os

class PathHelper(object):

    @classmethod
    def is_file(cls, path):
        return os.path.isfile(path)

    @classmethod
    def get_lines_from_file(cls, filepath):
        with open(filepath, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        return lines

    @classmethod
    def get_files_under_path(cls, path):
        return os.listdir(path)

    @classmethod
    def get_dictionary_key(cls, path):
        return path.split('/')[-1]

    @classmethod
    def get_absolute_path(cls, path):
        return os.path.abspath(path)

    @classmethod
    def join_path(cls, parent_path, child_path):
        return os.path.join(parent_path, child_path)
