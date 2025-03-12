# LOKRATIX THE MORNINGSTAR
```statblock
name: "LOKRATIX THE MORNINGSTAR"
level: 6
roles:
  - TROOP
  - HARRIER
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 160
immunities: acid 6
speed: 8 (flying)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +1
  - +3
  - +1
  - +2
  - +2
actions:
  - name: "Skewer"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 18 damage; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** Lokratix deals 6 damage to each creature or object in a line up to two squares behind the target."
  - name: "Acidic Stun"
    desc:
      "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 × 1 line within 1
      <br />**Target** All enemies in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 acid damage; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 12 acid damage; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 15 acid damage; M< 3 [[dazed]] (save ends) 
      <br />**Effect:** Lokratix deals an additional 6 damage on abilities targeting enemies [[dazed]] by this ability."
maneuvers:
  - name: "Takeoff"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lokratix lifts off from the ground and flies up to her speed. All creatures adjacent to the square she took off from are A < 2 knocked [[prone]]."
ta:
  - name: "Stay Back!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 2
      <br />**Target** One creature 
      <br />**Trigger**
      <br />**Target** enters a square within distance.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 acid damage; A< 1 speed is 0 (EoT)
      <br />★ 12–16 12 acid damage; A< 2 speed is 0 (EoT)
      <br />✸ 17+ 15 acid damage; A< 3 speed is 0 (EoT) Flighty When Lokratix deals damage to an enemy, the enemy can’t use her as the trigger for any of their triggered actions until the start of her next turn."
traits:
  - name: "Absorbing Scales"
    desc: "When Lokratix takes damage of a type she has an immunity for, she has damage immunity 6 against the next strike made against her."


```
