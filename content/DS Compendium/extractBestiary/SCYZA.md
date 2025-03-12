# SCYZA
```statblock
name: "SCYZA"
level: 3
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
  - Orc
ev: 20
stamina: 100
speed: 6
size: 4 /
stability: 3
free_strike: 5
characteristics:
  - +2
  - −1
  - −4
  - 0
  - −1
actions:
  - name: "Clawed Kick"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; [[prone]]
      <br />✸ 17+ 14 damage; [[prone]] 
      <br />**Effect:** The scyza roars and the target is I< 2 [[frightened]] (save ends)."
  - name: "Whiptail"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 13 damage
      <br />✸ 17+ 16 damage; A< 2 [[bleeding]] (save ends) 
      <br />**Effect:** This ability has an edge against a target on top of the scyza and knocks the target [[prone]] into an unoccupied adjacent square."
  - name: "Crestfall"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 cube within 2
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; 1 sonic damage; R< 0 [[dazed]] (save ends)
      <br />★ 12–16 7 damage; 2 sonic damage; R< 1 [[dazed]] (save ends)
      <br />✸ 17+ 9 damage; 3 sonic damage; R< 2 [[dazed]] (save ends)"
maneuvers:
  - name: "Sandstorm"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 3 burst
      <br />**Target** Special 
      <br />**Effect:** The scyza kicks up a sandstorm concealing themselves and each ally in the affected area until the end of the scyza’s next turn. Each enemy in the burst makes a Might test.
      <br />`dice: 2d10 + 2`
      <br />✸ ≤11 10 damage; [[prone]]; [[slowed]] (EoT)
      <br />★ 12–16 7 damage; [[slowed]] (EoT)
      <br />✦ 17+ 4 damage" 
ta:
  - name: "Brace and Bogart"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The scyza or an ally riding the scyza is targeted by an ability. 
      <br />**Effect:** Any damage dealt by the triggering ability is halved. If the creature or object who used the ability is within 3 of the scyza, the scyza makes a free strike against them."
traits:
  - name: "War Harness"
    desc: "Three of the scyza’s size 1 allies can occupy the same space while riding the scyza."
  - name: "Terrible Beast" 
    desc: "The scyza deals an additional 6 damage on strikes and abilities used against objects."


```
