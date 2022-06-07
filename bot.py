"""Skillz Bot"""

def move_penguins(target_iceberg) -> None:
    """
    Move penguins from mulitple icebergs to the target iceberg
    build a brig when there are spare pengiuns and we need this distance
    """
    ...

def worth_to_use_brig(source_iceberg, destination_iceberg) -> bool:
    """
    Finds whether its worth to use a brig or not
    Note: source_iceberg must be the bot's iceberg, unlike `destination_iceberg` who can be any iceberg (defense, conquer, attack)
    """
    return source_iceberg.turns_till_arrival(destination_iceberg) > 5 
    and get_spare_pengiuns(game.get_my_icebergs(), source_iceberg) - source_iceberg.brig_cost() >= 0

def get_spare_pengiuns(my_icebergs, iceberg) -> int:
    """
    Finds the iceberg's spare pengiuns count
    1. have above the average pengiuns
    """
    average_pengiuns = sum([my_iceberg.get_pengiun() for my_iceberg in my_icebergs]) / len(my_icebergs)

    return iceberg.get_pengiuns() - average_pengiuns


def iceberg_points(iceberg) -> int:
    """
    The best iceberg for moving to is:
    enemy
    1. smallest amount of pengiuns pengiuen 
    2. stratigic place
    3. threat factor -> for enemy defense
    4. the current bot state is winning -> defense otherwise attack
    my
    1. if the iceberg needs pengiuns
    2. under attack
    3. will survive
    """

    if iceberg in game.get_enemy_icebergs():
        return (get_stratigic_points(iceberg) - iceberg.get_pengiuns()) * (iceberg.get_level())

    # iceberg will die
    survival_factor = 0
    if (iceberg.get_pengiuns() - get_incoming_attacks(iceberg)) < 0:
        survival_factor = 20

    # wining
    wining_factor = 0
    if game.get_my_icebergs() > game.get_enemy_icebergs():
        wining_factor = 20

    return get_incoming_attacks(iceberg) + get_spare_pengiuns(game.get_my_icebergs(), iceberg) * -1 + survival_factor + winning_factor
            

def get_incoming_attacks(iceberg):
    """
    Get the damage from incoming attacks
    """
    damage = 0
    for i in game.get_enemy_penguin_groups():
        if i.destination == iceberg:
            damage += i.penguin_amount
    return damage

def get_stratigic_points(iceberg) -> int:
    """
    A stratigic location for an iceberg
    number of iceberges that are neighbors to the given iceberg
    """
    return len(filter(game.get_my_icebergs(), lambda i: iceberg.turns_till_arrival(i) == 1))

def iceberg_upgrade_points(iceberg) -> int:
    """
    The best iceberg to upgrade will be:
    1. largest penguins on it after the upgrade
    2. the best current level
    3. the best stratigic place 
    """
    return (iceberg.get_penguins() - icebreg.get_upgrade_cost()) * iceberg.level() * get_stratigic_points(iceberg)

def relative_importance(icebergs, iceberg, get_points):
    """
    Finds the relative importance of an iceberg 
    all iceberg points / icebergs points
    """
    return get_points(iceberg) / sum([get_points(iceberg) for iceberg in icebergs]) 

def get_icebergs():
    return game.get_bonus_iceberg() | game.get_netural_icebergs() | game.get_my_icebergs() | game.get_enemy_icebergs()

def do_turn(game):
    """
    Get the best iceberg and the best move (upgrade or move) and then execute it
    """
    global game

    icebergs = get_icebergs(game)
    target_iceberg = max(icebergs, key=iceberg_points)
    upgrade_iceberg = max(game.get_my_icebergs(), key=iceberge_upgrade_points)
    
    if relative_importance(icebergs, target_iceberg, iceberg_points) > relative_importance(game.get_my_icebergs(), target_iceberg, iceberg_points):
        move_penguins(target_iceberg)
    else:
        upgrade_iceberg.upgrade()

