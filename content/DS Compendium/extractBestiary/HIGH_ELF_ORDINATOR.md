# HIGH ELF ORDINATOR
```statblock
name: "HIGH ELF ORDINATOR"
level: 3
roles:
  - LEADER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 20
stamina: 120
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - +2
  - +3
  - +2
  - +3
actions:
  - name: "Lightning Rod"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 20
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 lightning damage; R< 1 [[dazed]] (save ends)
      <br />★ 12–16 14 lightning damage; R< 2 [[dazed]] (save ends)
      <br />✸ 17+ 17+ lightning damage; R< 3 [[dazed]] (save ends) 
      <br />**Effect:** High elves have an edge on abilities used against the target until the start of the ordinator’s next turn."
maneuvers:
  - name: "Elemental Uproar"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 Burst
      <br />**Target** Each elemental ally in the burst 
      <br />**Effect:** Each target moves up to their speed or makes a free strike. An elemental mote target can use their Spark of Life trait."
  - name: "Summon Elemental (Free Maneuver)"
    desc: "
      <br />**Cost** 3+ Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Effect:** For every 3 malice spent, the ordinator summons 5 elemental motes, 3 soot crows, 1 ceramic horse, or 1 brambleguard into unoccupied squares within distance."
ta:
  - name: "Enough!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Triggering enemy 
      <br />**Trigger** An enemy targets the ordinator or an ally within distance with an ability. 
      <br />**Effect:** The ordinator uses Lightning Rod against the target. Otherworldly Grace At the start of their turn, the ordinator can turn the duration of one save ends effect they suffer from into EoT. Magic Beacon While using Chaincast, magic abilities that use the Ordinator’s space have a double edge (see Chaincast)."
va:
  - name: "Fountains Roar, Now Free From The Earth (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target glows, ending one condition on themselves and then moving up to twice their speed."
  - name: "And The Sun Forsook Her Children (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 cube within 10
      <br />**Target** All enemies in the cube 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 12 corruption damage; pull 5 towards center of cube
      <br />★ 12–16 9 corruption damage; pull 3 towards center of cube
      <br />✦ 17+ Pull 1 towards center of cube 
      <br />**Effect:** The affected area becomes darkened and its space warps violently in every direction."
  - name: "But We Will Change Her Mind. (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and each ally in the burst 
      <br />**Effect:** All elves radiate wisps of magic. Each target makes a free strike that has the Magic keyword and deals an additional 3 damage."


```
