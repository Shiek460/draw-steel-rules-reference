# FIELD OF GROWTH
```statblock
name: "FIELD OF GROWTH"
level: 5
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Elemental
ev: 28
stamina: 120
immunities: poison 5
speed: 8 (climb)
size: 3 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - 0
  - 0
  - +2
  - +2
actions:
  - name: "Hampering Roots"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 8
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 13 damage; R< 1 [[prone]] can’t stand (save ends)
      <br />✸ 17+ 16 damage; [[prone]] R< 2 and can’t stand (save ends) 
      <br />**Effect:** This ability inflicts [[restrained]] (save ends) on targets that are already [[prone]]. When the [[restrained]] condition ends, any can’t stand effects also end."
maneuvers:
  - name: "Convocation of Verdure"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target gains 15 temporary stamina that lasts until the start of the field’s next turn. 
      <br />**3 Malice** The ground within 1 of the target is overgrown with thicket and vines until the end of the encounter. Whenever an enemy attacks the target while within [[Line of Effect]] of the affected area, they are pulled 5 towards the affected area. Whenever an enemy enters the affected area on a turn or starts their turn within it, they are knocked [[prone]]."
ta:
  - name: "Rose Lash"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Melee, Ranged
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object 
      <br />**Trigger** The field takes damage from the target. 
      <br />**Effect:** The field deals 6 damage to the target and A< 2 [[bleeding]] (save ends). Roots Run Deep The field can target creatures touching the ground with abilities, even if they don’t have [[Line of Effect]]." 
traits:
  - name: "Fickle and Free"
    desc: "The field can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


```
