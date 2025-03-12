# TROLL GLUTTON
```statblock
name: "TROLL GLUTTON"
level: 5
roles:
  - TROOP
  - BRUTE
ancestry:
  - Giant
  - Troll
ev: 28
stamina: 160
weaknesses: Acid 5, Fire 5
speed: 6
size: 2 /
stability: 4
free_strike: 7
characteristics:
  - +3
  - +1
  - -1
  - +0
  - +1
actions:
  - name: "Voracious Mastication"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 18 damage; M< 3 [[slowed]] (save ends) 
      <br />**1 Malice** The glutton regains stamina equal to the damage dealt."
  - name: "Crash Through"
    desc:
      "<br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The glutton shifts up to their speed in a straight line, ignoring difficult terrain. A creature can choose to fall [[prone]] or take 10 damage the first time the glutton passes through their space during the movement. If the glutton moves into a creature or object larger than them and the glutton doesn’t knock the creature [[prone]] or destroy the object, the glutton’s movement stops early and they become [[dazed]] until the end of their next turn."
maneuvers:
  - name: "Food Frenzy"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The glutton has a double edge on strikes and strikes have an edge against them, until the start of their next turn."
ta:
  - name: "Spiteful Retort (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Self 
      <br />**Trigger** The glutton is reduced to 0 stamina but doesn’t die. 
      <br />**Effect:** The glutton uses their Voracious Mastication ability against an adjacent creature."
traits:
  - name: "Insatiable Appetite"
    desc: "- Once per turn, the glutton can take the Charge action as a free maneuver if they target a [[winded]] creature."
  - name: "Relentless Hunger"
    desc: "The glutton only dies when they are reduced to 0 stamina by acid or fire damage, end their turn with 0 stamina, or take acid or fire damage while at 0 stamina."


```
