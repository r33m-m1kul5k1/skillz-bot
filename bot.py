"""Skillz Bot"""

def move_penguins(target_iceberg) -> None:
    """
    Move penguins from mulitple icebergs to the target iceberg
    build a brig when there are spare pengiuens and we need this distance
    """
    else
        ...

def worth_to_use_brig(source_iceberg, destination_iceberg) -> bool:
    """
    Finds whether its worth to use a brig or not
    Note: source_iceberg must be the bot's iceberg, unlike `destination_iceberg` who can be any iceberg (defense, conquer, attack)
    """
    return source_iceberg.turns_till_arrival(destination_iceberg) > 5 and 
           get_spare_pengiuens(source_iceberg) - source_iceberg.brig_cost() >= 0

def get_spare_pengiuens(iceberg) -> int:
    """
    Finds the iceberg's spare pengiuens count
    1. threat to the iceberg
    2. does it need more upgrades? in realation to the other iceberg's levels
    3. does it a startigic place for defense ? -> get_stratigic_points
    4. does it a good thing to attack with? -> get_stratigic_points to enemy icebergs
    maybe remove some cases, doens't need to be complicated
    """
    essential_pengiuens_for_iceberg = 0

    return max(iceberg.get_pengiuens() - essential_pengiuens_for_iceberg, 0)


def iceberg_points(iceberg) -> int:
    """
    The best iceberg for moving to is:
    1. pengiuen factor
    2. stratigic place
    3. threat factor -> for defense
    """
    return (get_stratigic_points(iceberg) + get_pengiuen_factor()) * (1 - get_enemy_iceberg_level())

def get_stratigic_points(iceberg) -> int:
    """
    A stratigic location for an iceberg
    number of iceberges that are neighbors to the given iceberg
    """
    return len(filter(game.get_icebergs(), lambda i: iceberg.turns_till_arrival(i) == 1))

def iceberg_upgrade_points(iceberg) -> int:
    """
    The best iceberg to upgrade will be:
    1. largest penguins on it after the upgrade
    2. the best current level
    3. the best stratigic place 
    """
    return (iceberg.get_penguins() - icebreg.get_upgrade_cost()) * iceberg.level() * get_stratigic_points(iceberg)

def turn():
    """
    Get the best iceberg and the best move (upgrade or move) and then execute it
    Chose move or upgrade:
    1. ratio(max()) > < = ratio(max())
    """

    target_iceberg = max(game.get_icebergs(), key=iceberg_points)
    upgrade_iceberg = max(game.get_icebergs(), key=iceberge_upgrade_points)
    
    # I can't really do this, they are not the same scoring machenism
    if where_in_move_ratio(target_iceberg) > where_in_upgrade_ratio(upgrade_iceberg):
        move_penguins(target_iceberg)
    else:
        upgrade_iceberg.upgrade()

