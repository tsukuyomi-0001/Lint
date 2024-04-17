class map:
    def __init__(self, name='sample', live=False):
        self.live = False
        self.name = name
        self.directory = {'/': []}
        self.file = {}

        if live == True:
            import lint_utility.storage as store
            data = store.load(self.name)

            self.directory = data[0]
            self.file = data[1]

    def load(self, file):
        import lint_utility.storage as store
        data = store.load(file)

        self.directory = data[0]
        self.file = data[1]

    def save(self):
        import lint_utility.storage as store
        store.store(self.directory, self.file, self.name)

    def create_obj(self, file, content=''):
        if '/' not in file:
            self.directory['/'] += [file]
            self.file[file] = content
        else:
            i = file.rfind('/')
            path = file[:i]
            try:
                self.directory[path] += [file[i+1:]]
                self.file[file] = content
            except:
                self.directory[path] = [file[i+1]]
                self.file[file] = content
        if self.live == True:
            import lint_utility.storage as store
            store.store(self.directory, self.file, self.name)

    def view(self):
        for key, item in self.directory.items():
            print('# ',key)
            size = len('#  '+key)
            for i in item:
                print(' '*size+i)

    def read(self, file):
        print('File: '+file+'\n')
        print(self.file[file])

    def write(self, file, content, mode='w'):
        if mode=='w':
            self.file[file] = content
        elif mode == 'a':
            self.file[file] += content
        if self.live == True:
            import lint_utility.storage as store
            store.store(self.directory, self.file, self.name)

    def script(self, file, to='python'):
        if to == 'python':
            import os
            data = self.file[file]
            os.system(f'python -c "{data}"')