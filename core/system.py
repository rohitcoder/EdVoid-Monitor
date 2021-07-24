import ast 

def ReadFile(path, mode, showError=False):
    try:
        f = open(path, "r")
        if mode == 'list':
            lines = f.readlines()
            return list(map(lambda x:x.strip(), lines))
        elif mode == 'json':
            return json.load(f)
        elif mode == 'dict':
            return ast.literal_eval(f.read())
        f.close()
    except Exception as e:
        if showError: 
            raise ValueError(str(e))
        else: 
            if mode == 'list':
                return []
            else:
                return {}