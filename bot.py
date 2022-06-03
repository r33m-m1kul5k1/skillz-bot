"""Skillz Bot"""

def move_penguins(target_iceberg, fast=False) -> None:
    """
    Move penguins from mulitple icebergs to the target iceberg
    """
    else
        ...



# Ignore this function its under development
def iceberg_points(iceberg) -> int:
    """
    get_enemy_iceberg
    """
    points = 0
    if iceberg.get_penguins() == 0:
        points = 20
        
    if iceberg.get_enemy

    return 

def get_stratigic_points(iceberg) -> int:
    ...

def iceberg_upgrade_points(iceberg) -> int:
    """
    The best iceberg to upgrade will be:
    1. largest penguins on it after the upgrade
    2. the best current level
    3. the best stratigic place (not in enemy lines?)
    """
    return (iceberg.get_penguins() - icebreg.get_upgrade_cost()) * iceberg.level() * get_stratigic_points(iceberg)

def turn():
    """
    Get the best iceberg and the best move (upgrade or move) and then execute it
    """

    target_iceberg = max(game.get_icebergs(), key=iceberg_points)
    upgrade_iceberg = max(game.get_icebergs(), key=iceberge_upgrade_points)
    
    # I can't really do this, they are not the same scoring machenism
    if iceberg_points(target_iceberg) > iceberg_upgrad_points(upgrade_iceberg):
        move_penguins(target_iceberg)
    else:
        upgrade_iceberg.upgrade()

