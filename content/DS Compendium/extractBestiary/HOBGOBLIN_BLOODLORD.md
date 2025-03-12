# HOBGOBLIN BLOODLORD
```statblock
name: "HOBGOBLIN BLOODLORD"
level: 6
roles:
  - LEADER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 32
stamina: 180
immunities: fire 6
speed: 6 (teleport)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +4
  - +2
  - +2
  - +3
  - +3
actions:
  - name: "Soul Sword"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 corruption damage; P< 2 [[bleeding]] (save ends)
      <br />★ 12–16 16 corruption damage; P< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 19 corruption damage; P< 4 [[bleeding]] (save ends)
      <br />**2 Malice** Each target is marked until they die or the end of the encounter. Allies have an edge on strikes against marked targets. The bloodlord can only have up to 3 targets marked this way, removing the oldest mark first."
maneuvers:
  - name: "Take Point!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses a signature action."
ta:
  - name: "An Army From Blood"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** — 
      <br />**Trigger** The target takes damage
      <br />**Distance** Ranged 10
      <br />**Target** 1 non  -minion hobgoblin 
      <br />**Effect:** 3 hobgoblin recruits crawl out of the target’s blood and appear in unoccupied spaces adjacent to the target."
traits:
  - name: "Infernal Ichor"
    desc: "If the bloodlord’s stamina drops to 0, they spray burning blood. Each creature within 1 of the bloodlord takes 3 fire damage."
  - name: "End Effect"
    desc: "At the end of their turn, the bloodlord can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
va:
  - name: "Advance! (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target gains 10 temporary stamina, moves up to their speed, and makes a free strike."
  - name: "Skulls Abound (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 aura
      <br />**Target** Self 
      <br />**Effect:** The bloodlord surrounds themselves with a storm of flying skulls until the end of the encounter. An enemy that first enters the aura or starts their turn there takes 8 corruption damage and has a bane on their next power roll until the start of their next turn."
  - name: "I am Fire! I am Death! (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 fire damage; P< 2 2 fire damage; push 2, [[prone]]
      <br />★ 12–16 5 fire damage; P< 3 7 fire damage; push 3, [[prone]]
      <br />✸ 17+ 5 fire damage; P< 4 10 fire damage; push 5, [[prone]] 
      <br />**Effect:** The bloodlord is wreathed in black flames until the end of the encounter. When an adjacent enemy touches or uses a melee ability against the bloodlord, they take 5 corruption damage."

```
