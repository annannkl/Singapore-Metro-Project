import csv
import random
from metro_graph import Vertex, Graph, Edge


def load_metro_graph(csv_path):
    g = Graph()
    stations = []
    # Load stations
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            code = row['code']
            name = row['name'].title()
            line = row['line']
            num = int(row['num'])
            v = g.add(code)
            v.data = name
            stations.append({'code': code, 'name': name, 'line': line, 'num': num})
    # Connect same line neighbors
    from collections import defaultdict
    lines = defaultdict(list)
    for s in stations:
        lines[s['line']].append(s)
    for line, lst in lines.items():
        lst.sort(key=lambda x: x['num'])
        for i in range(len(lst)-1):
            a = lst[i]['code']
            b = lst[i+1]['code']
            time = random.randint(2,8)
            g.connect(a, b, weight=time)
    # Connect interchanges (same name)
    names = defaultdict(list)
    for s in stations:
        names[s['name']].append(s['code'])
    for name, codes in names.items():
        if len(codes) > 1:
            for i in range(len(codes)):
                for j in range(i+1, len(codes)):
                    g.connect(codes[i], codes[j], weight=5)
    return g
