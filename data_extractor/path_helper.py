import os

class PathHelper(object):

    def __init__(self):
        pass

    def is_file(self, path):
        return os.path.isfile(path)

    def get_lines_from_file(self, filepath):
        with open(filepath, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        return lines

    def get_files_under_path(self, path):
        return os.listdir(path)

    def get_dictionary_key(self, path):
        return path.split('/')[-1]

    def get_absolute_path(self, path):
        return os.path.abspath(path)

    def join_path(self, parent_path, child_path):
        return os.path.join(parent_path, child_path)
