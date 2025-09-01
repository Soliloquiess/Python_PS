def solution(hp):
    general_ants = hp // 5
    remaining_hp = hp % 5
    
    soldier_ants = remaining_hp // 3
    remaining_hp = remaining_hp % 3
    
    worker_ants = remaining_hp
    
    return general_ants + soldier_ants + worker_ants