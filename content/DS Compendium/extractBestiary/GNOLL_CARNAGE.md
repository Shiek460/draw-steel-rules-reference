# GNOLL CARNAGE
```statblock
name: "GNOLL CARNAGE"
level: 2
roles:
  - LEADER
ancestry:
  - Abyssal
  - Gnoll
ev: 16
stamina: 100
speed: 5
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +3
  - +3
  - 0
  - 0
  - +3
actions:
  - name: "Shrapnel Whip"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; A< 1 [[bleeding]] (save ends)
      <br />★ 12–16 11 damage; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 14 damage; A< 3 [[bleeding]] and [[dazed]] (save ends) 
      <br />**Effect:** An ally targeted by this ability makes a free strike instead of taking damage."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target deals an additional 3 damage with their strikes until the start of the carnage’s next turn. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Rampage"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the carnage moves up to their speed and either chooses to target 2 creatures with free strikes or one creature with their shrapnel whip."
  - name: "Endless Hunger" 
    desc: "If the carnage is reduced to 0 stamina while there are still gnolls on the battle map, one gnoll on the map is transformed into the carnage, keeping the gnoll’s stamina."
va:
  - name: "Call Up from The Abyss (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Effect:** The carnage summons 5 gnoll wildlings and 5 abyssal hyenas into unoccupied spaces. "
  - name: "Edacity (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target moves up to their speed and makes a free strike. A creature that takes damage from this villain action is also knocked [[prone]]. "
  - name: "Deepest Wounds (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** Each [[winded]] enemy in the burst 
      <br />**Effect:** The carnage’s eyes and all exposed blood within distance starts to glow bright red. Each target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 The target can’t regain stamina until the end of the encounter
      <br />★ 12–16 The target can’t regain stamina (save ends)
      <br />✸ 17+ No effect 
      <br />**Effect:** Until the end of the encounter, each gnoll has a double edge power rolls that target a [[winded]] enemy."

```
