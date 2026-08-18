def parse_techsydney(text):
    lines = text.split('\n')
    lines = [x for x in lines if x != '(opens in new tab)']

    # If startup doesnt contain an overview, make it blank
    if len(lines) < 11:
        lines.insert(1, '-')

    startup = {
        "name": lines[0],
        "overview": lines[1],
        "location": lines[2][:-7],
        "industry": "",
        "stage": "",
        "focus": "",
        "type": "",
        "team": "",
        "funding": "",
        "description": lines[-2],
        "url": lines[-1]
    }

    for line in lines:
        if ':' in line:
            split = line.split(':')
            startup[split[0].lower()] = split[1]

    print(startup.get("url"))

    return startup