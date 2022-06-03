"""Skillz Bot"""

def move_penguins(target_iceberg, fast=False) -> None:
    """
    Move penguins from mulitple icebergs to the target iceberg
    """
    else
        ...



def iceberg_points(iceberg) -> int:
    """
    """
    ...

def iceberg_upgrade_points(iceberg) -> int:
    """
    """
    ...

def turn():
    """
    Get the best iceberg and the best move (upgrade or move) and then execute it
    """

    target_iceberg = max(game.get_icebergs(), key=iceberg_points)
    upgrade_iceberg = max(game.get_icebergs(), key=iceberge_upgrade_points)
    
    if iceberg_points(target_iceberg) > iceberg_upgrad_points(upgrade_iceberg):
        move_penguins(target_iceberg)
    else:
        upgrade_iceberg.upgrade()

