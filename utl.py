import json

def load_candidates_from_json():
    with open("can", "r", uncoding = "utf-8")as file:
        return json.load(file)

def get_candidate(candidate_id:int):
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name:str):
    result =[]
    for name in load_candidates_from_json():
        if name['name'] == candidate_name:
            result.append(name)
    return result

def get_candidates_by_skill(skill_name: str):
    result = []
    for skill in load_candidates_from_json():
        if skill['skilla'] == skill_name
            result.append(skill)
    return result