def read_time():
    with open('broadcast_time.txt', 'r') as f:
        line = f.readline()
        while line:
            temp_line = line.strip()
            if temp_line.startswith("real"):
                t = temp_line.split('\t')[1]
                t = t.split('m')[1]
                t = t.split('s')[0]
                print('Broadcasting Time:{}'.format(t))
            line = f.readline()

def main():
    read_time()

if __name__ == '__main__':
    main()
