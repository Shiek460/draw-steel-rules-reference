# TIME RAIDER TYRANNIS
```statblock
name: "TIME RAIDER TYRANNIS"
level: 3
roles:
  - LEADER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 20
stamina: 120
immunities: Psychic 5
speed: 10 (teleport, hover)
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +0
  - +3
  - +3
  - +1
  - +0
actions:
  - name: "Gatling Blaster"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Psionic, Strike, Weapon
      <br />**Distance** Melee 2 or Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 corruption damage
      <br />★ 12–16 12 corruption damage
      <br />✸ 17+ 15 corruption damage 
      <br />**Effect:** Each target’s speed is reduced by 2 until the start of the tyrannis’ next turn."
maneuvers:
  - name: "Air Raid!"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three time raiders 
      <br />**Effect:** Each target is psionically lifted into the air, flies up to their speed, and makes a free strike. If a target doesn’t land in an unoccupied space, they fall."
ta:
  - name: "Precog Reflexes"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature 
      <br />**Trigger** The target strikes the tyrannis. 
      <br />**Effect:** The strike has a bane. After the strike resolves, the tyrannis makes a free strike against the target. 
      <br />**2 Malice** The strike has a double bane instead."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the tyrannis can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Foresight"
    desc: "The tyrannis doesn’t have a bane on strikes against concealed creatures."
va:
  - name: "We Will Win! (Villain Action 1)"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Self and Ranged 10
      <br />**Target** Self and three allies 
      <br />**Effect:** Each target gains 15 temporary stamina and has their speed doubled until the end of their turn."
  - name: "Stick To The Plan! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target can end one effect or condition affecting them or can move up to their speed."
  - name: "Armageddon (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** Special 
      <br />**Effect:** The tyrannis fires a sensor mine into each unoccupied square in the burst and a gravity well (see [[Gravity Well]]) into one of their own squares. Whenever an enemy moves into a square with a sensor mine in it, the mine explodes, dealing 3 damage to the enemy."

```
