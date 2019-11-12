import os
from collections import defaultdict

class Extractor(object):
    
    def __init__(self):
        self._broadcast_time = defaultdict(list)
        self._file_loss_rate = defaultdict(list)
        self._mse = defaultdict(list)
        self._ssim = defaultdict(list)

    def _extract_helper(self, path):
        key = path.split('/')[-1]
        with open(os.path.abspath(path), 'r') as f:
            line = f.readline()
            total_time, time_nums = 0, 0
            received_files, lost_files = 0, 0
            t_mse, t_ssim = 0, 0

            while line:
                temp_line = line.strip()
                # extract broadcast time
                if temp_line.startswith('Broadcasting Time'):
                    time_nums += 1
                    time = temp_line.split(':')[1]
                    total_time += float(time)
                # extract received files number
                elif temp_line.endswith('files') or temp_line.endswith('file'):
                    temp_string = temp_line.split(',')[1]
                    received = temp_string.split()[0]
                    received_files = int(received)
                # extract lost files number
                elif temp_line.startswith('File Loss'):
                    lost = temp_line.split('=')[1]
                    lost_files = int(lost)
                # extract MSE and SSIM
                elif temp_line.startswith('MSE'):
                    temp_string = temp_line.split(',')
                    mse = float(temp_string[0].split(':')[1])
                    ssim = float(temp_string[1].split(':')[1])
                    t_mse += mse
                    t_ssim += ssim
                line = f.readline()

            self._set_broadcast(key, total_time, time_nums)
            self._set_loss_rate(key, received_files, lost_files)
            self._set_mse_ssim(key, received_files, t_mse, t_ssim)

    def _set_broadcast(self, key, total_time, time_nums):
        if time_nums:
            average_time = total_time / time_nums
            self._broadcast_time[key].append(round(average_time, 5))
    
    def _set_mse_ssim(self, key, received, tmse, tssim):
        if received:
            self._mse[key].append(tmse / received)
            self._ssim[key].append(tssim / received)

    def _set_loss_rate(self, key, received, lost):
        desired = lost + received
        if desired:
            loss_rate = lost / desired
            self._file_loss_rate[key].append(round(loss_rate, 3))

    def _extract(self, path):
        if os.path.isfile(path):
            self._extract_helper(path)
            
        elif os.path.isdir(path):
            for f in os.listdir(path):
                self._extract(os.path.join(path, f))


    def extract_to_csv_from(self, path):
        self._extract(path)

        if self._broadcast_time:
            columns = list(self._broadcast_time.keys())
            columns = ','.join(columns)
            filename = 'broadcast.csv'
            self._write_helper(filename, columns, 0)

        if self._file_loss_rate:
            columns = list(self._file_loss_rate.keys())
            columns = ','.join(columns)
            filename = 'file_loss_rate.csv'
            self._write_helper(filename, columns, 1)

        if self._mse:
            columns = list(self._mse.keys())
            columns = ','.join(columns)
            filename = 'mse.csv'
            self._write_helper(filename, columns, 2)

        if self._ssim:
            columns = list(self._ssim.keys())
            columns = ','.join(columns)
            filename = 'ssim.csv'
            self._write_helper(filename, columns, 3)

    def _write_helper(self, filename, columns, flag):
        with open(filename, 'w') as f:
            f.write("%s\n"%(columns))
            values = []
            if flag == 0:           # 0: Broadcast
                values = list(self._broadcast_time.values())
            elif flag == 1:         # 1: Loss_rate
                values = list(self._file_loss_rate.values())
            elif flag == 2:         # 2: MSE
                values = list(self._mse.values())
            elif flag == 3:         # 3: SSIM
                values = list(self._ssim.values())

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
    extractor.extract_to_csv_from('log')
    print('[INFO] done')
    

if __name__ == '__main__':
    main()
