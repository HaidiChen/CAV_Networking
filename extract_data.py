import os
from collections import defaultdict

class Extractor(object):
    
    def __init__(self):
        self._broadcast_time = defaultdict(list)
        self._file_loss_rate = defaultdict(list)

    def __extract(self, path):
        if os.path.isfile(path):
            with open(os.path.abspath(path), 'r') as f:
                line = f.readline()
                total_time = 0
                time_nums = 0
                received_files, lost_files = 0, 0
                while line:
                    temp_line = line.strip()
                    if temp_line.startswith('Broadcasting Time'):
                        time_nums += 1
                        time = temp_line.split(':')[1]
                        total_time += float(time)

                    elif temp_line.endswith('files'):
                        temp_string = temp_line.split(',')[1]
                        received = temp_string.split()[0]
                        received_files = int(received)

                    elif temp_line.startswith('File Loss'):
                        lost = temp_line.split('=')[1]
                        lost_files = int(lost)

                    line = f.readline()

                if time_nums:
                    average_time = total_time / time_nums
                    self._broadcast_time[path.split('/')[-1]].append(round(average_time, 5))

                desired_files_number = lost_files + received_files
                if desired_files_number:
                    loss_rate = lost_files / desired_files_number
                    self._file_loss_rate[path.split('/')[-1]].append(round(loss_rate, 3))

        elif os.path.isdir(path):
            for f in os.listdir(path):
                self.__extract(os.path.join(path, f))


    def extract_to_csv(self, path):
        self.__extract(path)

        if self._broadcast_time:
            columns = list(self._broadcast_time.keys())
            columns = ','.join(columns)
            filename = 'broadcast.csv'
            self.__write_helper(filename, columns, True)

        if self._file_loss_rate:
            columns = list(self._file_loss_rate.keys())
            columns = ','.join(columns)
            filename = 'file_loss_rate.csv'
            self.__write_helper(filename, columns, False)

    def __write_helper(self, filename, columns, flag):
        with open(filename, 'w') as f:
            f.write("%s\n"%(columns))
            values = []
            if flag:    # True: Broadcast
                values = list(self._broadcast_time.values())
            else:       # False: Loss_rate
                values = list(self._file_loss_rate.values())
            for i in range(len(values[0])):
                data = []
                for v in values:
                    try:
                        data.append(str(v[i]))
                        data.append(',')
                    except:
                        data.append('N/A')
                        data.append(',')

                del data[-1]
                data = ''.join(data)
                f.write("%s\n"%(data))




def main():
    extractor = Extractor()
    print('[INFO] start extracting...')
    extractor.extract_to_csv('log')
    print('[INFO] done')
    

if __name__ == '__main__':
    main()
