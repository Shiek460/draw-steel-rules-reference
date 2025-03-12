# ESSENCE OF STORMS
```statblock
name: "ESSENCE OF STORMS"
level: 3
roles:
  - TROOP
  - HARRIER
ancestry:
  - Elemental
ev: 20
stamina: 100
immunities: lightning 5
speed: 8 (fly)
size: 1S /
stability: 0
free_strike: 5
characteristics:
  - +1
  - +2
  - −1
  - 0
  - +2
actions:
  - name: "Bluster"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 5 damage; 4 lightning damage; push 1
      <br />✸ 17+ 5 damage; 7 lightning damage; push 3 
      <br />**Effect:** The essence shifts 3 before or after using this ability."
maneuvers:
  - name: "Convocation of Squalls"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target receives lightning immunity 5 until the start of the essence’s next turn if they don’t already have it. 
      <br />**3 Malice** The target emits a 3 aura vortex until the end of the encounter. The aura is considered difficult terrain for enemies. At the end of each of the target’s turns, the target can select 1 creature within the aura to push 5."
ta:
  - name: "Thunderclap"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Melee, Ranged
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object 
      <br />**Trigger** The essence takes damage from the target. 
      <br />**Effect:** The essence deals 5 lightning damage to the target."
traits:
  - name: "Fickle and Free"
    desc: "The essence can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


```
