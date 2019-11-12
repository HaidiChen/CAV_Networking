def read_time():
    with open('broadcast_time.txt', 'r') as f:
        line = f.readline()
        while line:
            temp_line = line.strip()
            if temp_line.startswith("real"):
                t = temp_line.split('\t')[1]
                m = t.split('m')[0]
                m = float(m)
                s = t.split('m')[1]
                s = s.split('s')[0]
                s = float(s)
                print('Broadcasting Time:{}'.format(m * 60 + s))
            line = f.readline()

def main():
    read_time()

if __name__ == '__main__':
    main()
