class History:

    def __init__(self):
        self.history_arr = []
        self.score_dupl = 0
        self.score2 = 0

    def is_it_dupe_sequence(self, sequence):
        mas_a = []
        b = 0
        i = 0
        while i < len(self.history_arr) // 500 * 500:
            mas_a.append(self.history_arr[i])
            if len(mas_a) == 2:
                if mas_a == sequence:
                    self.score_dupl += 1
                    return True
                mas_a = []
                b += 1
                i = b - 1
            i += 1
        return False

    def save_history(self, filepath):
        with open( filepath, 'w') as file:
            for i in self.history_arr:
                file.write(str(i) + ' ')
            file.write(f'S{self.score2}')

    def load_history(self, filepath):
        a = str()
        self.history_arr = []
        with open( filepath, 'r') as file:
            for i in file.read():
                if i == 'S':
                    a = ''
                    continue
                if i == ' ':
                    self.history_arr.append(int(a))
                    a = ''
                a += i
            if a == '':
                self.score2 = 0
            else:
                self.score2 = float(a)

    def set_history(self, sequence, score):
        if self.is_it_dupe_sequence(sequence) == True:
            if score < self.score2:
                self.score2 = score
                self.load_history('file.txt')
                for i in sequence:
                    self.history_arr.append(i)
                print(self.history_arr)
                self.save_history('file.txt')
        else:
            self.load_history('file.txt')
            for i in sequence:
                self.history_arr.append(i)
            self.save_history('file.txt')
            self.score2 = score