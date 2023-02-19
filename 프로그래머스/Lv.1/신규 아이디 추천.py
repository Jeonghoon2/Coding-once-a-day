import re

def solution(new_id):

    # One Step
    new_id = new_id.lower()

    # Two Step
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)

    # Three Step
    while new_id.find("..") >= 0:
        new_id = new_id.replace("..",".")

    # Four Step
    new_id = new_id[1:] if new_id[0] == '.' and len(new_id) > 1 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id

    # Five Step
    if len(new_id) == 0:
        new_id += 'a'
    elif len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # Seven Step
    while len(new_id) < 3:
        new_id += new_id[-1]

    answer = new_id
    return answer

print(solution("abcdefghijklmn.p"))