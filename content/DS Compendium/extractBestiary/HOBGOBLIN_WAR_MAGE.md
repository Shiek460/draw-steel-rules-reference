# HOBGOBLIN WAR MAGE
```statblock
name: "HOBGOBLIN WAR MAGE"
level: 5
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 28
stamina: 120
immunities: fire 5
speed: 5 (teleport, hover)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - 0
  - +2
  - +3
  - +2
  - +2
actions:
  - name: "Hellfire"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 fire damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 9 fire damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 11 fire damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** The war mage can teleport a creature within 10 up to 2 squares before using this ability."
  - name: "Enchantments of War"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 2 allies 
      <br />**Effect:** Each target gains 10 temporary stamina and has a double edge on their next power roll. The war mage can spend any amount of their stamina to increase the temporary stamina each target gains by an equivalent amount."
maneuvers:
  - name: "Unhallowed Ground"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 cube within 10
      <br />**Target** Special 
      <br />**Effect:** The war mage consecrates the affected area and causes it to smolder. Until the end of the encounter, the affected area is considered difficult terrain and enemies have fire weakness 10 while occupying an affected square."
ta:
  - name: "Magic Siphon"
    desc: "
      <br />**Keywords** Magic 
      <br />**Trigger** A creature within distance uses a strike or ability with the magic keyword
      <br />**Distance** Ranged 10
      <br />**Target** Triggering creature 
      <br />**Effect:** Any damage dealt or stamina regained by the attack or ability is halved. The war mage regains stamina equal to the remainder."
traits:
  - name: "Infernal Ichor"
    desc: "If the war mage’s stamina drops to 0, they spray burning blood. Each creature within 1 of the war mage takes 3 fire damage."
  - name: "Despair, You Who Faces Death"
    desc: "Each enemy has -2 on saving throws while within 2 squares of the war mage."


```
